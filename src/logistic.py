import numpy as np
from scikits.learn.linear_model import LogisticRegression
from scikits.learn.metrics import auc

from src.utils2 import roc_curve, sigmoid



def fit_logistic_regression(X, y, Xt, yt, C=0.1):
    classifier = LogisticRegression(C=C)
    classifier.fit(X, y)

    w = classifier.coef_
    b = classifier.intercept_[0]

    lin = np.dot(Xt, w.T) + b

    probabilities = sigmoid(lin)

    fpr, tpr, thresholds = roc_curve(yt, probabilities, 
            thresholds=np.linspace(0,1,1e3))

    auc_score = auc(fpr, tpr)

    return auc_score, fpr, tpr, w, b
