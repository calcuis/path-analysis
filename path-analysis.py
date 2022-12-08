import numpy as np
from sklearn.linear_model import LinearRegression

def perform_path_analysis(data, paths):
    # Create the LinearRegression object
    regressor = LinearRegression()

    # Initialize the output dictionary
    results = {}

    # Loop over the paths
    for path in paths:
        # Extract the predictor and outcome variables for the current path
        predictor = data[path[0]]
        outcome = data[path[1]]

        # Fit the predictor and outcome variables to the regressor
        regressor.fit(predictor, outcome)

        # Get the coefficients and store them in the results dictionary
        results[path] = regressor.coef_

    # Return the results
    return results
