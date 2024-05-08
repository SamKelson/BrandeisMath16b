# %%
import pandas as pd
import numpy as np
# %%
def train_test_split(X, y, test_size=0.2, random_state=None):
    """
    Split the data into training and testing sets.

    Parameters:
    - X (array-like): The input features.
    - y (array-like): The target variable.
    - test_size (float, optional): The proportion of the data to include in the test set. Default is 0.2.
    - random_state (int, optional): The seed value for the random number generator. Default is None.

    Returns:
    - X_train (array-like): The training set input features.
    - X_test (array-like): The test set input features.
    - y_train (array-like): The training set target variable.
    - y_test (array-like): The test set target variable.
    """
    if random_state is not None:
        np.random.seed(random_state)
    
    # Shuffle the indices
    indices = np.arange(len(X))
    np.random.shuffle(indices)
    
    # Calculate the number of samples for the test set
    test_samples = int(len(X) * test_size)
    
    # Split the indices into train and test sets
    test_indices = indices[:test_samples]
    train_indices = indices[test_samples:]
    
    # Split the data based on the indices and return them
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]


# %%
def predict_from_model(training, target, testing):
    """
    Predicts the values of the target variable using an affine model fitted to the training data.

    Args:
        training (numpy.ndarray): Array of shape (n, m) containing the training data.
        target (numpy.ndarray): Array of shape (n, 1) containing the target variable.
        testing (numpy.ndarray): Array of shape (k, m) containing the testing data.

    Returns:
        numpy.ndarray: Array of shape (k, 1) containing the predicted values of the target variable.
    """
    # Add a column of ones to the training data
    training = np.column_stack((training, np.ones(len(training))))
    testing = np.column_stack((testing, np.ones(len(testing))))

    # Compute the least squares solution
    theta, _, _, _ = np.linalg.lstsq(training, target)

    # Predict the values of the target variable
    return testing @ theta


# %%
def moore(file_path: str) -> float:
    """
    Calculates the doubling time (in years) for transistor counts estimated via least squares
    for the data points in the given CSV file.

    Args:
        file_path (str): The path of the CSV file containing the data.

    Returns:
        float: The doubling time (in years) for transistor counts.

    """
    # Read the data from the CSV file
    data = pd.read_csv(file_path)

    # Extract the data from the DataFrame
    A = data['Year'].to_numpy()
    
    b = data['Transistors'].to_numpy()
    # Compute the base 2 logarithm of the transistor counts
    b = np.log2(b)

    # Fit an affine model to the data
    training = np.column_stack((A, np.ones(len(A))))
    gamma, _, _, _ = np.linalg.lstsq(training, b)

    return 1/gamma[0]

# %%
def min_validation_error(features, b) -> int:
    """
    Finds the value of k that minimizes the sum of squared residuals on the validation set.

    Args:
        features (numpy array): Array of shape (n, m) containing the dataset features.
        b (numpy array): Array of shape (n,) containing the target values.

    Returns:
        int: The value of k that minimizes the sum of squared residuals on the validation set.
    """

    # Split the data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(features, b, test_size=0.5, random_state=42)

    min_error = 0
    best_k = 0
    for k in range(features.shape[1]):
        selected_features = X_train[:, :k+1]

        # Compute the least squares solution for the training set
        theta, _, _, _ = np.linalg.lstsq(selected_features, y_train)

        # Compute the sum of squared residuals on the validation set
        val_features = X_val[:, :(k+1)]
        val_predictions = val_features @ theta # use the model to predict CMEDV values for the validation set
        residuals = val_predictions - y_val
        error = (residuals**2).sum()

        if k == 1 or error < min_error:
            min_error = error
            best_k = k
    
    return best_k

