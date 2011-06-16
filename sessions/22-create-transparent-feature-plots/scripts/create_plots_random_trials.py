from random import shuffle

import numpy as np
import matplotlib.pyplot as plt

from src.utils2 import get_path
from src.data_interface import trd, L


path = get_path(__file__) + '/..'

plots = [
    ('E1', 0, 50), ('E4', -100, 100), ('P1', 20, 90), ('P2', 0, 30), ('P5', 0, 3),
    ('P7', 20, 150), ('V2', -1, 1), ('V4', 0, 20), ('V6', 500, 1000),
    ('V11', 0, 25), ('P5', 0, 0.5), ('P6', 100, 1400), ('V6', 620, 680)
]

trials = list(trd.trial_id_list)
shuffle(trials)

for feature, min, max in plots:
#for feature in L[2:]:
    for tid in trials[:20]:
        v = trd.get_trial(tid).get_feature(feature).view()
        plt.plot(range(len(v)), v, 'b-', alpha=0.2)
    ax = plt.gca()
    ax.set_xlim(0,1200)
    ax.set_ylim(min, max)
    ax.set_xlabel('Observation number')
    ax.set_ylabel(feature)
    ax.set_title('{0} in 20 trials overlayed'.format(feature))
    plot_path = '{0}/plots/{1}_{2}-{3}_20-trials.'.format(path, feature, min, max)
    plt.savefig(plot_path + 'pdf', format='pdf')
    plt.savefig(plot_path + 'png', format='png', dpi=300)
    plt.cla()
