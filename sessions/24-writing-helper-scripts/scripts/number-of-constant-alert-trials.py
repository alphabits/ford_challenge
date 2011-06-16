from __future__ import division

import numpy as np

from src.data_interface import trd

suc = 0

for t in trd.trial_id_list:
    v = trd.get_trial(t).IsAlert.view()
    if v.min() == v.max() == 0:
        suc += 1

print suc/len(trd.trial_id_list)
