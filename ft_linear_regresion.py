from open_file import open_file
from linear_regresion import linear_regresion
from estimate_price import estimate_price
from precision import linear_regression_precision
import sys as sys
import matplotlib.pyplot as plt

def display_graph(data_file, linear_data, mileage, estimated_price):
    """
    Display a graph with data from the selected country.
    Set a title and scales for the x and y axes.
    """

    data = [(int(km), int(price)) for km, price in data_file]

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

def linear_values(theta_0, theta_1, data_file):
    """
    Use linear values from dataset to get the line resulting
    from the linear regression
    """
    data = [(int(km), int(price)) for km, price in data_file]
    new_data = []
    for km, _ in data:
        new_data.append([km, estimate_price(theta_0, theta_1, km)])
    return new_data

def main():
    n_arg = len(sys.argv)
    try:
        assert n_arg == 2, "the arguments are bad"
        mileage = sys.argv[1]
        data_file = open_file("data.csv")
        theta_0, theta_1 = linear_regresion(data_file)
        linear_data = linear_values(theta_0, theta_1, data_file)
        price = estimate_price(theta_0, theta_1, int(mileage))
        print("Estimate price to {}km: {}$".format(mileage, price))
        display_graph(data_file, linear_data, int(mileage), price)
        linear_regression_precision(theta_0, theta_1, data_file)
    except AssertionError as error:
        print("AssertionError: {}".format(error))
    except Exception as error:
        print("Unexpected error: {}".format(error))

    

if __name__ == "__main__":
    main()