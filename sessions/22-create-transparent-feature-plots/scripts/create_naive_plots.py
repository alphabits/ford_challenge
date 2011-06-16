import numpy as np
import matplotlib.pyplot as plt

from src.utils2 import get_path
from src.data_interface import trd, L


path = get_path(__file__) + '/..'

for fname in L[2:]:
    for tid in trd.trial_id_list:
        v = trd.get_trial(tid).get_feature(fname).view()
        plt.plot(range(len(v)), v, 'b-', alpha=0.1)
    ax = plt.gca()
    ax.set_xlim(0,1200)
    ax.set_xlabel('Observation number')
    ax.set_ylabel(fname)
    ax.set_title('{0} in 500 trials overlayed'.format(fname))
    plot_path = '{0}/plots/naive_{1}.'.format(path, fname)
    plt.savefig(plot_path + 'png', format='png', dpi=300)
    plt.savefig(plot_path + 'pdf', format='pdf')
    plt.cla()
