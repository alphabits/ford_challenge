from __future__ import division

import json
import random

import numpy as np
import matplotlib.pyplot as plt

from src.utils2 import c_ex as c, get_path, get_bins
import src.dataloaders as d
from src.logistic import fit_logistic_regression


path = get_path(__file__) + '/..'

D = d.trainingset_extended()
#D = d.testset_extended()

cols = c('sde5', 'v11', 'e9')

C = 1000000

num_bins = 10
bins = get_bins(D.shape[0], num_bins)

X = D[:, cols]
y = D[:, c.isalert]

auc = num_bins*[0]
fpr = num_bins*[0]
tpr = num_bins*[0]
w = num_bins*[0]
b = num_bins*[0]
for i in range(num_bins):
    train = [item for j in range(num_bins) if j != i for item in bins[j]]
    test = bins[i]
    auc[i], fpr[i], tpr[i], w[i], b[i] = fit_logistic_regression(
            X[train,:], y[train,:], X[test,:], y[test,:], C=C)

def save_result(save_path):
    with open(save_path, 'w') as f:
        json.dump(get_result(), f, indent=4)

def get_result():
    wl = [a[0].tolist() for a in w]
    save_data = dict(zip(
        ['weights', 'auc', 'intercepts', 'C', 'num_bins', 'dataset_size', 'generator'], 
        [wl, auc, b, C, num_bins, D.shape[0], __file__]
    ))
    return save_data
