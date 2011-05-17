import os

import numpy as np


def nz(bool_array):
    return np.nonzero(bool_array)[0]

def get_path(path):
    return os.path.abspath(os.path.dirname(path))

def bool_to_color(bool):
    return 'blue' if bool!=0 else 'red'

def sigmoid(x):
    return 1/(1+np.exp(-x))

def get_test_and_training_data(X, y, num_training, num_test):
    rows = np.random.random_integers(0,X.shape[0]-1,num_training+num_test)
    test_rows = rows[:num_test]
    training_rows = rows[num_test:]
    X_test = X[test_rows,:]
    X_training = X[training_rows,:]
    y_test = y[test_rows]
    y_training = y[training_rows]
    return X_test, y_test, X_training, y_training

def roc_curve(y, probas_, thresholds=None):
    """compute Receiver operating characteristic (ROC)

    Parameters
    ----------

    y : array, shape = [n_samples]
        true targets

    probas_ : array, shape = [n_samples]
        estimated probabilities

    Returns
    -------
    fpr : array, shape = [n]
        False Positive Rates

    tpr : array, shape = [n]
        True Positive Rates

    thresholds : array, shape = [n]
        Thresholds on proba_ used to compute fpr and tpr

    References
    ----------
    http://en.wikipedia.org/wiki/Receiver_operating_characteristic
    """
    y = y.ravel()
    probas_ = probas_.ravel()
    if thresholds is None:
        thresholds = np.sort(np.unique(probas_))[::-1]
    else:
        thresholds = np.sort(np.unique(thresholds))[::-1]
    n_thresholds = thresholds.size

    tpr = np.empty(n_thresholds) # True positive rate
    fpr = np.empty(n_thresholds) # False positive rate
    n_pos = float(np.sum(y == 1)) # nb of true positive
    n_neg = float(np.sum(y == 0)) # nb of true negative

    for i, t in enumerate(thresholds):
        tpr[i] = np.sum(y[probas_ >= t] == 1) / n_pos
        fpr[i] = np.sum(y[probas_ >= t] == 0) / n_neg

    return fpr, tpr, thresholds
