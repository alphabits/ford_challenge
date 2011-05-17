import os

import numpy as np

from src.data import A
from src.utils_common import nz, get_path, bool_to_color, sigmoid, \
        get_test_and_training_data, roc_curve


# Load labels duplicate in src/data.py
# For backward compability the duplicate code
# is kept in src/data.py
L = np.loadtxt('data/labels.csv', delimiter=',', dtype=str)
L = list(L)
L_clean = [l for l in L if l not in ['P8','V7','V9','ObsNum','TrialID']]

# Extended labels
prefix = 30*[''] + 30*['m'] + 30*['sd']
L_ex = L[:3] + [a+b for a,b in zip(prefix, 3*L[3:])]


def get_trial(trial_id):
    return A[A[:, 0]==trial_id, :]
