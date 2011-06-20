import json
import random

import numpy as np

from src.utils2 import c_ex as c, get_path, L_ex, LabelIndex
import src.dataloaders as d
from src.logistic import fit_logistic_regression


path = get_path(__file__) + '/..'

#D = d.trainingset_extended()
D = d.testset_extended()

a = range(D.shape[0])
random.shuffle(a)

num_train_rows = 10000
num_test_rows = 5000

tr_rows = a[:num_train_rows]
ts_rows = a[num_train_rows:(num_train_rows+num_test_rows)]

X = D[:, 4:]
X = X[tr_rows, :]
y = D[tr_rows, c('isalert')]

Xt = D[:, 4:]
Xt = Xt[ts_rows, :]
yt = D[ts_rows, c('isalert')]

auc = np.zeros((90,90));

# Remove P3, P6, P8, V7 and V9 and 
# the corresponding running features.
# See session 9 on data exploration
# for details
cc = LabelIndex(L_ex[4:])
exclude = cc('p3', 'p6', 'p8', 'v7', 'v9', 
             'mp3', 'mp6', 'mp8', 'mv7', 'mv9',
             'sdp3', 'sdp6', 'sdp8', 'sdv7', 'sdv9')
candidates = [i for i in range(90) if i not in exclude]

chosen = []

for i in range(90):
    for c in candidates:
        features = chosen + [c]
        result = fit_logistic_regression(X[:, features], y, Xt[:, features], yt)
        auc[i, c] = result[0]
    
    chosen_feature = auc[i,:].argmax()

    if auc[i,chosen_feature] <= auc[i-1,:].max():
        break

    candidates.remove(chosen_feature)
    chosen.append(chosen_feature)
