import numpy as np
from open_file import open_file

def estimate_price(theta_0, theta_1, mileage):
    """
    Predict the price for a given mileage.
    Use the following hypothesis to predict the price :
    estimatePrice(mileage) = θ0 + (θ1 * mileage)
    """
    return theta_0 + (theta_1 * mileage)

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

def linear_regresion():
    """
    Read a dataset and perform a linear regression on the data. 
    Once the linear regression has completed, get the variables theta0 and theta1
    for use in the estimate_price() program.
    """
    theta_0 = 0
    theta_1 = 0
    learning_rate = 0.01
    iterations = 1000
    np.seterr(all='raise')

    try:
        data_file = open_file("data.csv")
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
        np.save('train_values.npy', [theta_0, theta_1])
        print("-> Trained model!! <-")
    except FileNotFoundError as error:
        print("Error: {}".format(error))
    except ZeroDivisionError as error:
        print("Error: {}".format(error))
    except Exception as error:
        print("Unexpected error: {}".format(error))

if __name__ == "__main__":
    linear_regresion()