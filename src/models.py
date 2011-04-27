from __future__ import division

from random import random

import numpy as np
import matplotlib.pyplot as plt



class Trial(object):
    _instances = {}

    def __init__(self, trial_id=None, data=None):
        self.trial_id = trial_id
        self.data = data if data is not None else A

        if self.trial_id is None:
            self._view = self.data
        else:
            self._view = self.data[np.nonzero(self.data[:,0]==self.trial_id)[0],:]

        self.trial_id_list = np.unique(self._view[:, 0])

        self.features = {}

    def num_rows(self):
        return self._view.shape[0]

    def get_feature(self, feature_id):
        if not feature_id in L:
            raise AttributeError("No feature with name %s exists" % (feature_id,))
        if not self.features.has_key(feature_id):
            self.features[feature_id] = Feature(self, feature_id)
        return self.features[feature_id]

    def get_trial(self, trial_id):
        if not trial_id in self.trial_id_list:
            raise AttributeError("No trial with id %s" % (trial_id,))
        return Trial.get(trial_id)

    def view(self):
        return self._view

    def __getattr__(self, name):
        if name.startswith('t'):
            trial_id = int(name[1:])
            return self.get_trial(trial_id)
        elif name in L:
            return self.get_feature(name)

    def __getitem__(self, name):
        return self.__getattr__(name)

    def __repr__(self):
        if self.trial_id is None:
            return '<Whole data set>'
        else:
            return '<Trial %s>' % (self.trial_id,)

    @classmethod
    def get(cls, trial_id):
        if not cls._instances.has_key(trial_id):
            cls._instances[trial_id] = cls(trial_id)
        return cls._instances[trial_id]


class Feature(object):
    def __init__(self, trial, feature_id):
        self.trial = trial
        self.feature_id = feature_id
        self.feature_index = np.nonzero(L==feature_id)[0][0]
        self._view = None

    def num_rows(self):
        return self.trial.num_rows()

    def plot(self):
        x = np.r_[0:self.num_rows()]
        return plt.plot(x, self.trial.view()[:,self.feature_index])

    def mean(self):
        return self.view().mean()

    def min(self):
        return self.view().min()

    def max(self):
        return self.view().max()

    def std(self):
        return self.view().std()

    def unique_values(self):
        return np.unique(self.view()).size

    def scatter_plot(self, other_feature, obs_nums=None):
        if obs_nums is None:
            obs_nums = random.sample(range(self.num_rows()), 50)
        v = self.view()

    def MI(self, nbins=10):
        v = self.view()
        tv = self.trial.view()
        bin_borders = np.linspace(v.min(), v.max(), nbins+1)
        bin_counts = np.zeros((nbins, 2))
        cur_bin = 0
        is_alert_col = 2
        total_alerts = sum(tv[:, is_alert_col])

        '''
        sv = tv[np.argsort(v),:]
        # Loop through each row in the sorted trial data set
        for i in range(sv.shape[0]):
            # If needed, update the current bin
            while cur_bin < nbins and sv[i,self.feature_index] >= bin_borders[cur_bin]:
                cur_bin += 1
            # And increment the right bin count
            bin_counts[cur_bin-1,sv[i,np.nonzero(L=='IsAlert')[0][0]]] += 1
        '''
        row_cnt = 0
        alert_cnt = 0
        for i in range(nbins):
            select = v <= bin_borders[i+1]
            if i != 0:
                select = np.logical_and(v > bin_borders[i], select)
            temp = tv[np.nonzero(select)[0], :]
            num_in_bin = temp.shape[0]
            num_alert_in_bin = sum(temp[:,2])
            bin_counts[i,:] = [num_in_bin - num_alert_in_bin, num_alert_in_bin]
        

    def _calc_MI_from_bin_count(bin_count):
        pass

    def view(self):
        if self._view is None:
            self._view = self.trial.view()[:, self.feature_index]
        return self._view
    
    def __repr__(self):
        return '<Feature %s of %s>' % (self.feature_id, self.trial)
