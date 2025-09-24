import numpy as np


def feature_normalize(X):
    # You need to set these values correctly
    n = X.shape[1]  # the number of features
    X_norm = X
    mu = np.zeros(n)
    sigma = np.zeros(n)

    # ===================== Your Code Here =====================
    # Instructions : First, for each feature dimension, compute the mean
    #                of the feature and subtract it from the dataset,
    #                storing the mean value in mu. Next, compute the
    #                standard deviation of each feature and divide
    #                each feature by its standard deviation, storing
    #                the standard deviation in sigma
    #
    #                Note that X is a 2D array where each column is a
    #                feature and each row is an example. You need
    #                to perform the normalization separately for
    #                each feature.
    #
    # Hint: You might find the 'np.mean' and 'np.std' functions useful.
    #       To get the same result as Octave 'std', use np.std(X, 0, ddof=1)
    #
    # ===========================================================

    # means
    house_size_mean = np.mean(X[:, 0])
    num_bedrooms_mean = np.mean(X[:, 1])
    mu = np.array([house_size_mean, num_bedrooms_mean])

    # standard deviations
    house_size_std = np.std(X[:, 0], ddof=1)
    num_bedrooms_std = np.std(X[:, 1], ddof=1)
    sigma = np.array([house_size_std, num_bedrooms_std])

    X_norm = (X - mu) / sigma

    return X_norm, mu, sigma
