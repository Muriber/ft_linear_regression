import numpy as np
from plott_data_and_precision import display_graph

def estimate_price():
    """
    Predict the price for a given mileage.
    Use the following hypothesis to predict the price :
    estimatePrice(mileage) = θ0 + (θ1 * mileage)
    """
    try:
        mileage = int(input("Please enter the Km: "))
        assert mileage > 0, "Please enter a positive value and greater than zero"
        theta_values = np.load('train_values.npy')
        theta_0 = theta_values[0]
        theta_1 = theta_values[1]
        estimated_price = theta_0 + (theta_1 * mileage)
        print("Estimated price for {}km is: {}$".format(mileage, estimated_price))
        input("Press any key to Bonus...")
        display_graph(mileage, estimated_price, theta_0, theta_1)
    except AssertionError as error:
        print("AssertionError: {}".format(error))
    except FileNotFoundError:
        print("Estimated price for {}km is: {}$".format(mileage, 0))
    except Exception as error:
        print("Unexpected error: {}".format(error))



if __name__ == "__main__":
    estimate_price()