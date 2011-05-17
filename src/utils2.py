import os

import numpy as np

from src.utils_common import nz, get_path, bool_to_color, sigmoid, \
        get_test_and_training_data, roc_curve


L = np.loadtxt('data/labels_new.csv', delimiter=',', dtype=str)
L = list(L)
L_clean = [l for l in L if l not in ['P8','V7','V9','ObsNum','TrialID','RowNum']]


# Extended labels
prefix = 30*[''] + 30*['m'] + 30*['sd']
postfix = 30*[''] + 60*['r']
L_ex = L[:4] + [a+b+c for a,b,c in zip(prefix, 3*L[4:], postfix)]


class LabelIndex(object):

    def __init__(self, labels):
        self.labels = map(lambda l: l.lower(), labels)

    def __getattr__(self, name):
        name = name.lower()
        return self.labels.index(name)

    def __getitem__(self, name):
        if hasattr(name, '__iter__'):
            return map(self.__getattr__, name)
        return self.__getattr__(name)
    
    def __call__(self, *args):
        return map(self.__getattr__, args)

c = LabelIndex(L)


def create_extended_dataset(D):
    cnt = 0
    D_ex = np.zeros((D.shape[0], 94))
    std_first_row = np.zeros((1,30))

    for i in range(D.shape[0]):
        if D[i,c.obsnum] == 0: 
            cnt = 0
            sums = np.zeros((1,30))
            sums_sq = np.zeros((1,30))
        
        cnt += 1
        sums += D[i,4:]
        sums_sq += D[i,4:]**2

        D_ex[i,:34] = D[i,:]

        # Calculate running mean
        D_ex[i,34:64] = sums/cnt
        
        # Calculate running std
        # Avoid dividing by zero in first row
        if cnt > 1:
            D_ex[i,64:94] = (cnt*sums_sq - sums**2)/(cnt*(cnt-1))
        else:
            D_ex[i,64:94] = std_first_row

    return D_ex


def create_extended_dataset_window(D, window_size=30):
    cnt = 0
    D_ex = np.zeros((D.shape[0], 94))
    std_first_row = np.zeros((1,30))

    for i in range(D.shape[0]):
        obsnum = D[i,c.obsnum]

        if obsnum == 0: 
            cnt = 0
            sums = np.zeros((1,30))
            sums_sq = np.zeros((1,30))
        
        if obsnum < window_size:
            cnt += 1

        sums += D[i,4:]
        sums_sq += D[i,4:]**2

        if obsnum >= window_size:
            sums -= D[i-window_size,4:]
            sums_sq -= D[i-window_size,4:]

        D_ex[i,:34] = D[i,:]

        # Calculate window mean
        D_ex[i,34:64] = sums/cnt
        
        # Calculate window std
        # Avoid dividing by zero in first row
        if cnt > 1:
            D_ex[i,64:94] = (cnt*sums_sq - sums**2)/(cnt*(cnt-1))
        else:
            D_ex[i,64:94] = std_first_row

    return D_ex