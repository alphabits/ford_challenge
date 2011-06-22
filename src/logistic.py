import numpy as np
from scikits.learn.linear_model import LogisticRegression
from scikits.learn.metrics import auc

from src.utils2 import roc_curve, sigmoid


def _fit_logistic_regression(X, y, C=0.1):
    classifier = LogisticRegression(C=C)
    classifier.fit(X, y)
    return classifier

def _calculate_auc(classifier, Xt, yt):
    w = classifier.coef_
    b = classifier.intercept_[0]
    lin = np.dot(Xt, w.T) + b
    prob = sigmoid(lin)
    fpr, tpr, thresholds = roc_curve(yt, prob, 
            thresholds=np.linspace(prob.min(),prob.max(),1e3))
    auc_score = auc(fpr, tpr)
    return auc_score, fpr, tpr


def fit_logistic_regression(X, y, Xt, yt, C=0.1):
    classifier = _fit_logistic_regression(X, y, C)
    w = classifier.coef_
    b = classifier.intercept_[0]
    auc, fpr, tpr = _calculate_auc(classifier, Xt, yt)
    return auc, fpr, tpr, w, b
