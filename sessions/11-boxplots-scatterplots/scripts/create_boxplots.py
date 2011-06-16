import matplotlib.pyplot as plt
import numpy as np

from src.data_interface import d, L_clean
from src.utils import get_path


path = get_path(__file__) + '/..'

trials = range(0,51)

ticklabels = []
for i in trials:
    if i==trials[0] or i%10 == 0:
        ticklabels.append(i)
    else:
        ticklabels.append('')

font = {'weight': 'normal', 'size': 16}

#for label in ['V1']:
for label in L_clean:
    data = [d.get_trial(i).get_feature(label).view() for i in trials]
    plt.title('Boxplot of feature {0} in the trials {1}-{2}'.format(
            label, trials[0], trials[-1]), font)
    plt.boxplot(data)
    ax = plt.gca()
    ax.set_xticklabels(ticklabels)
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(10)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(10)
    ax.set_xlabel('Trial Id', font)
    ax.set_ylabel(label, font)
    plt.savefig(
            '{0}/plots/boxplots/{1}-t{2}-t{3}.pdf'.format(
                    path, label, trials[0], trials[-1]), 
            format='pdf', papertype='a4')
    plt.cla()

