import numpy as np
from estimate_price import estimate_price


def normalize_data(data):
    """
    Normalize data using Z-Score Normalization to use scaled data.
    Data_norm = (Data - Data_mean) / Data_std
    """
    data = [(float(km), float(price)) for km, price in data]

    km_values = np.array([km for km, _ in data])
    mean_km = np.mean(km_values)
    std_km = np.std(km_values)

    price_values = np.array([price for _, price in data])
    mean_price = np.mean(price_values)
    std_price = np.std(price_values)

    normalized_data = [((km - mean_km) / std_km, (price - mean_price) / std_price) for km, price in data]
    return normalized_data, mean_km, std_km, mean_price, std_price

def linear_regresion(data_file):
    """
    Read a dataset and perform a linear regression on the data. 
    Once the linear regression has completed, get the variables theta0 and theta1
    for use in the estimate_price() program.
    """
    theta_0 = 0
    theta_1 = 0
    learning_rate = 0.01
    iterations = 1000

    normalized_data, mean_km, std_km, mean_price, std_price = normalize_data(data_file)

    m = len(normalized_data)

    for _ in range(iterations):
        temp_error0 = 0
        temp_error1 = 0
        for km, price in normalized_data:
            error = estimate_price(theta_0, theta_1, km) - price
            temp_error0 += error
            temp_error1 += error * km
        theta_0 -= learning_rate * (temp_error0 / m)
        theta_1 -= learning_rate * (temp_error1 / m)

    theta_1 = (theta_1 * std_price ) / std_km
    theta_0 = (theta_0 * std_price) + mean_price - (theta_1 * mean_km)
    return theta_0, theta_1