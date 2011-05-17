from __future__ import division

import numpy as np

from src.utils import nz



D = np.load('data/fordTrain.npy')

means = D.mean(0)
stds = D.std(0)

cols = nz(stds != 0)[3:]

for i in xrange(D.shape[0]):
    D[i,cols] = (D[i,cols] - means[cols])/stds[cols]

np.save('data/fordTrainNormalized2.npy', D)
