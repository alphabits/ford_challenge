from __future__ import division

import json
import random

import numpy as np
import matplotlib.pyplot as plt

from src.utils2 import c_ex as c, get_path
import src.dataloaders as d
from src.logistic import fit_logistic_regression


path = get_path(__file__) + '/..'

with open(path+'/data/forward-selection-results-2-for-docs.json') as f:
    _tmp = json.load(f)
    features = _tmp['labels_chosen']

# Controls how many of the 48
# features from feature selection
# that are included in the log reg.
features = features[:3]

D = d.testset_extended()

cols = c(*features)

a = range(int(D.shape[0]))
random.shuffle(a)

C = 10000
num_bins = 10
bin_size = int(np.ceil(len(a)/num_bins))
bins = [a[i*bin_size:(i+1)*bin_size] for i in range(num_bins)]

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
        ['weights', 'auc', 'intercepts', 'C', 'num_bins', 'dataset_size', 'generator', 'features'], 
        [wl, auc, b, C, num_bins, D.shape[0], __file__, features]
    ))
    return save_data

def save_roc_curve(run, title, filename):
    plt.plot(fpr[run], tpr[run], linewidth=3)
    plt.xlabel('False positive rate', {'size': 16})
    plt.ylabel('True positive rate', {'size': 16})
    plt.title(title, {'size': 18})
    plt.savefig(path+'/plots/'+filename+'.pdf')
