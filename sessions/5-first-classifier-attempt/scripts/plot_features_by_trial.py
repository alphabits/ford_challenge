import numpy as np
from matplotlib import pyplot as plt

from src.data import L
from src.utils import get_trial, get_path


sess_root = get_path(__file__) + '/..'

rnd_trials = [12, 328, 288, 89, 47, 494, 313, 500, 201]

features_to_plot = [3, 6, 7, 8, 9, 11, 12, 14, 15, 16, 20, 
        22, 23, 24, 27, 29, 32]
#features_to_plot = [2]

for trial_id in rnd_trials:
    t = get_trial(trial_id)
    for feature in features_to_plot:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        #ax.set_ylim(-1, 2)
        ax.plot(range(len(t)), t[:, feature])
        ax.set_title('Feature: %s - Trial: %s' % (L[feature], trial_id))
        ax.set_ylabel(L[feature])
        rel_path = 'plots/t%s-%s.png' % (trial_id, L[feature])
        fig.savefig(sess_root + '/' + rel_path)
    
