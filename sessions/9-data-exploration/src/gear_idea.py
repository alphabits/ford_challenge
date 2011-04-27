import numpy as np
from matplotlib import pyplot as plt

from src.data_interface import d
from src.utils import get_path


path = get_path(__file__) + '/../plots/gear_idea'
V10_idx = 31
IsAlert_idx = 2

for trial_id in d.trial_id_list:
    t = d.get_trial(trial_id)
    v = t.view()
    unique_values = t.V10.unique_values()
    if unique_values in [1,4,5]:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        #ax.set_ylim(-1, 2)
        ax.plot(range(len(v)), v[:, V10_idx])
        ax.plot(range(len(v)), v[:, IsAlert_idx])
        ax.set_title('V10 vs IsAlert - Trial: %s' % (trial_id,))
        file_name = '/t%s.png' % (trial_id,)
        fig.savefig(path + '/' + file_name)
