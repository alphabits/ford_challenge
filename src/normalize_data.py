from __future__ import division

import numpy as np

# Load training data set. The name A is kept for backward compability
D = np.load('data/fordTrain.npy')

trial_ids = range(511)
trial_ids = trial_ids[:469] + trial_ids[480:]


for tid in trial_ids:
    rows = np.nonzero(D[:,0]==tid)[0]
    for fid in range(3,33):
        min_ = D[rows,fid].min()
        max_ = D[rows,fid].max()
        range_ = max_ - min_
        if range_ == 0.0:
            D[rows,fid] = 1.0
        else:
            D[rows,fid] = (D[rows,fid] - min_) / range_

np.save('data/fordTrainNormalized.npy', D)



# self.data[np.nonzero(self.data[:,0]==self.trial_id)[0],:]
