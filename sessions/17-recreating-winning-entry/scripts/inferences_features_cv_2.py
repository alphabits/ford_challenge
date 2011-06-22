from __future__ import division

import json

import numpy as np
import matplotlib.pyplot as plt

from src.utils2 import c_ex as c, get_path, get_bins
import src.dataloaders as d
from src.logistic import _fit_logistic_regression,\
        _calculate_auc


path = get_path(__file__) + '/..'

D = d.trainingset_extended()
T = d.testset_extended()

cols = c('sde5', 'v11', 'e9')

Xt = T[:, cols]
yt = T[:, c.isalert]

C = 1000000
num_bins = 10

bins = get_bins(T.shape[0], num_bins)

classifier = _fit_logistic_regression(D[:, cols], D[:, c.isalert], C)

auc = num_bins*[0]
fpr = num_bins*[0]
tpr = num_bins*[0]

for i in range(num_bins):
    rows = bins[i]
    auc[i], fpr[i], tpr[i] = _calculate_auc(classifier, Xt[rows,:], yt[rows])

def save_result(save_path):
    with open(save_path, 'w') as f:
        json.dump(get_result(), f, indent=4)

def get_result():
    save_data = dict(zip(
        ['weights', 'auc', 'intercepts', 'C', 'num_bins', 
         'dataset_size', 'generator', 'fpr', 'tpr'], 
        [classifier.coef_[0].tolist(), auc, classifier.intercept_[0], C, 
         num_bins, D.shape[0], __file__, [a.tolist() for a in fpr], 
         [a.tolist() for a in tpr]]
    ))
    return save_data

def plot_roc_curve(run, title):
    plt.plot(fpr[run], tpr[run], linewidth=3)
    plt.xlabel('False positive rate', {'size': 16})
    plt.ylabel('True positive rate', {'size': 16})
    plt.title(title, {'size': 18})

def save_plot(filename):
    plt.savefig(path+'/plots/'+filename+'.pdf')

