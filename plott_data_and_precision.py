import sys as sys
import numpy as np
import matplotlib.pyplot as plt
from open_file import open_file
from linear_regresion import estimate_price


def linear_regression_precision(theta_0, theta_1, data):
    """
    Calculates precision from a linear regression.
    Coefficient of Determination:
    R**2 =  1 - (sum(Real_value - Calculate_value)**2) / (sum(Real_value - mean_value)**2)
    """
    error = 0
    var = 0 

    price_values = np.array([price for _, price in data])
    mean_price = np.mean(price_values)

    for km, price in data:
        est_price = estimate_price(theta_0, theta_1, km)
        error += (price - est_price) ** 2
        var += (price - mean_price) ** 2
    
    r_2 = 1 - (error / var)
    print("The precision of the algorithm is: ", r_2)
    return r_2

def linear_values(theta_0, theta_1, data):
    """
    Use linear values from dataset to get the line resulting
    from the linear regression
    """
    new_data = []
    for km, _ in data:
        new_data.append([km, estimate_price(theta_0, theta_1, km)])
    return new_data

def display_graph(mileage, estimated_price, theta_0, theta_1):
    """
    Display a graph with data from the selected country.
    Set a title and scales for the x and y axes.
    """
    data_file = open_file("data.csv")
    data = [(int(km), int(price)) for km, price in data_file]
    linear_data = linear_values(theta_0, theta_1, data)

    sorted_data = sorted(data, key=lambda x: x[0])
    
    km, price = zip(*sorted_data)
    ln_km, ln_price = zip(*linear_data)

    min_price = min(price)
    max_price = max(price)
    fig, ax = plt.subplots()
    ax.set_xlabel("Kms")
    ax.set_yticks(range(min_price, max_price + 1, 200))
    ax.set_ylabel("Price")
    
    ax.plot(ln_km, ln_price, color="r")
    ax.scatter(mileage, estimated_price, color="y")
    ax.scatter(km, price)
    plt.show()
    linear_regression_precision(theta_0, theta_1, data)
