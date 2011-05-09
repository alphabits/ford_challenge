import json

import numpy as np
from scikits.learn.metrics import auc

from src.extended_data import D_ex
from src.utils import L_ex, sigmoid, roc_curve, get_path


path = get_path(__file__) + '/..'

w = np.array([-410.6073, 0.1494, 4.4185])

idxs = [L_ex.index(f) for f in ['sdE5', 'V11', 'E9']]
Xf = D_ex[:, idxs]

num_tests = 5
results = []

for i in range(num_tests):
    test_rows = np.random.random_integers(0, D_ex.shape[0]-1, 1e5)

    X = Xf[test_rows, :]
    y = D_ex[test_rows, 2]

    lin = np.dot(X, w)
    probs = sigmoid(lin)

    fpr, tpr, thresholds = roc_curve(y, probs, thresholds=np.linspace(0,1,1e3))

    results.append(auc(fpr, tpr))


json_path = '{0}/data/hard-coded-results-{1}-tests.json'.format(path, num_tests)
with open(json_path, 'w') as f:
    json.dump(results, f, indent=4)
