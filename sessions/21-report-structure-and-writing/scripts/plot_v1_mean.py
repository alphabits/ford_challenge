import matplotlib.pyplot as plt
import numpy as np

from src.data_interface import trd
from src.utils2 import get_path


path = get_path(__file__) + '/..'

trials = trd.trial_id_list

means = [trd.get_trial(i).get_feature('V1').view().mean() for i in trials]

plt.title('Mean pr. trial of feature V1')
plt.plot(range(len(trials)), means)
plt.gca().set_xticklabels(trials)
plt.savefig('{0}/plots/mean_pr_trial_v1.pdf'.format(path), format="pdf")
plt.cla()
