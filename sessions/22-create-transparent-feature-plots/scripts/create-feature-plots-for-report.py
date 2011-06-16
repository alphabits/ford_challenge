import numpy as np
import matplotlib.pyplot as plt

from src.utils2 import get_path
from src.data_interface import trd, L


path = get_path(__file__) + '/..'

plots = {
    'V11': [1,35,29],
    'P5': [0,92,29],
    'E4': [1,2,101],
    'E1': [288,333,147],
    'E10': [442,333,89],
    'V2': [490,494,442]
}


for feature, trials in plots.items():
    for tid in trials:
        v = trd.get_trial(tid).get_feature(feature).view()
        plt.plot(range(len(v)), v)
        ax = plt.gca()
        ax.set_xlim(0,1200)
        ax.set_xlabel('Observation number')
        ax.set_ylabel(feature)
        ax.set_title('Feature {0} in trial {1}'.format(feature, tid))
        plot_path = '{0}/plots/report/{1}_trial-{2}.'.format(path, feature, tid)
        plt.savefig(plot_path + 'pdf', format='pdf')
        plt.savefig(plot_path + 'png', format='png', dpi=300)
        plt.cla()
