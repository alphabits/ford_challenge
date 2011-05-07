import os

from numpy import nonzero

from src.data import A

def nz(bool_array):
    return nonzero(bool_array)[0]

def get_trial(trial_id):
    return A[A[:, 0]==trial_id, :]

def get_path(path):
    return os.path.abspath(os.path.dirname(path))

def bool_to_color(bool):
    return 'blue' if bool!=0 else 'red'
