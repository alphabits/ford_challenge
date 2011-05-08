import json

import matplotlib.pyplot as plt
import numpy as np
from scikits.learn.linear_model import LogisticRegression

from src.data_interface import d, L_clean, L
from src.utils import get_path, bool_to_color, sigmoid


path = get_path(__file__) + '/..'
L = list(L)

X = d.view()[:,3:]
y = d.view()[:,2]

# Learning rate when estimating parameters
C = 0.1

classifier = LogisticRegression(C=C, penalty='l2')

training_rows = range(int(1e5))

classifier.fit(X[training_rows,:], y[training_rows,:])

coef_dict = dict(zip(L[3:], list(classifier.coef_[0])))
coef_dict['intercept'] = classifier.intercept_[0]

with open('{0}/data/coefs_train_0-1e5.json'.format(path), 'w') as f:
    json.dump(coef_dict, f, indent=4, sort_keys=True)
