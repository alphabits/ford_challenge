from __future__ import division

import os
import random

import numpy as np
from scipy.stats import t

from src.utils_common import nz, get_path, bool_to_color, sigmoid, \
        get_test_and_training_data, roc_curve


L = np.loadtxt('data/labels_new.csv', delimiter=',', dtype=str)
L = list(L)
L_clean = [l for l in L if l not in ['P8','V7','V9','ObsNum','TrialID','RowNum']]


# Extended labels
prefix = 30*[''] + 30*['m'] + 30*['sd']
L_ex = L[:4] + [a+b for a,b in zip(prefix, 3*L[4:])]


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
c_ex = LabelIndex(L_ex)


def confidence_interval_t_distribution(estimates):
    l = len(estimates)
    t_value = t.ppf(0.975, l-1)
    m = estimates.mean()
    std = estimates.std(ddof=1)
    statistic = t_value*std/np.sqrt(l)
    low = m - statistic
    high = m + statistic
    return low, high, statistic

def get_bins(dataset_size, num_bins):
    a = range(int(dataset_size))
    random.shuffle(a)
    bin_size = int(np.ceil(dataset_size/num_bins))
    return [a[i*bin_size:(i+1)*bin_size] for i in range(num_bins)]

def get_random_subset(data, subset_size):
    a = range(int(data.shape[0]))
    random.shuffle(a)
    return data[a[:subset_size], :]


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
            tmp_var = (cnt*sums_sq - sums**2)/(cnt*(cnt-1))
            tmp_var[:,np.nonzero(tmp_var<0)[1]] = 0
            D_ex[i,64:94] = np.sqrt(tmp_var)
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
            sums_sq -= D[i-window_size,4:]**2

        D_ex[i,:34] = D[i,:]

        # Calculate window mean
        D_ex[i,34:64] = sums/cnt
        
        # Calculate window std.
        # Avoid dividing by zero in first row.
        # And ensure that variance is non negative.
        # Guess negative values occur because 
        # of rounding errors
        if cnt > 1:
            tmp_var = (cnt*sums_sq - sums**2)/(cnt*(cnt-1))
            tmp_var[:,np.nonzero(tmp_var<0)[1]] = 0
            D_ex[i,64:94] = np.sqrt(tmp_var)
        else:
            D_ex[i,64:94] = std_first_row

    return D_ex
