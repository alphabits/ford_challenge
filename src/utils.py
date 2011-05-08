import os

import numpy as np

from src.data import A

def nz(bool_array):
    return np.nonzero(bool_array)[0]

def get_trial(trial_id):
    return A[A[:, 0]==trial_id, :]

def get_path(path):
    return os.path.abspath(os.path.dirname(path))

def bool_to_color(bool):
    return 'blue' if bool!=0 else 'red'

def sigmoid(x):
    return 1/(1+np.exp(-x))
