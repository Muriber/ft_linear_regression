def estimate_price(theta_0, theta_1, mileage):
    """
    Predict the price for a given mileage.
    Use the following hypothesis to predict the price :
    estimatePrice(mileage) = θ0 + (θ1 * mileage)
    """
    return theta_0 + (theta_1 * mileage)