import json
import random

import numpy as np

from src.utils2 import c_ex as c, get_path
import src.dataloaders as d
from src.logistic import fit_logistic_regression


path = get_path(__file__) + '/..'

D = d.trainingset_extended()
Dt = d.testset_extended()

cols = c('sde5', 'v11', 'e9')

a = range(D.shape[0])
random.shuffle(a)

X = D[:, cols]
X = X[a[:320000], :]
y = D[a[:320000], c('isalert')]
y = y.astype(int)^1

Xt = D[:, cols]
Xt = Xt[a[320000:], :]
yt = D[a[320000:], c('isalert')]
yt = yt.astype(int)^1

num_tests = 1
auc = num_tests*[0]
fpr = num_tests*[0]
tpr = num_tests*[0]
w = num_tests*[0]
b = num_tests*[0]

for i in range(num_tests):
    auc[i], fpr[i], tpr[i], w[i], b[i] = fit_logistic_regression(X, y, Xt, yt, C=10**(i+3))


def save_result(append=''):
    wl = [a[0].tolist() for a in w]
    save_data = dict(zip(['weights', 'auc', 'intercepts'], [wl, auc, b]))
    save_path = '{0}/session/17-recreating-winning-entry'\
            '/data/regression-result.json'.format(path)
    with open(save_path, 'w') as f:
        json.dump(save_data, f)
        
