import numpy as np

from estimate_price import estimate_price


def linear_regression_precision(theta_0, theta_1, data):
    """
    Calculates precision from a linear regression.
    Coefficient of Determination:
    R**2 =  1 - (sum(Real_value - Calculate_value)**2) / (sum(Real_value - mean_value)**2)
    """
    cast_data = [(float(km), float(price)) for km, price in data]
    error = 0
    var = 0 

    price_values = np.array([price for _, price in cast_data])
    mean_price = np.mean(price_values)

    for km, price in cast_data:
        est_price = estimate_price(theta_0, theta_1, km)
        error += (price - est_price) ** 2
        var += (price - mean_price) ** 2
    
    r_2 = 1 - (error / var)
    print("The precision of the algorithm is: ", r_2)
    return r_2
