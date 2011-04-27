import json
import matplotlib.pyplot as plt
import numpy as np

from src.data_interface import trd, L
from src.utils import get_path


path = get_path(__file__) + '/..'

json_file = open(path + '/src/unique_values_pr_trial.json', 'r')
vals_pr_trial = json.load(json_file)
json_file.close()

for k in vals_pr_trial:
    data = vals_pr_trial[k]["trial_results"].values()
    plt.title('Histogram for unique values of {0}'.format(k))
    plt.hist(data, 10)
    plt.savefig('{0}/plots/unique_values_hists/{1}.png'.format(path, k), format='png', dpi=150)
    plt.cla()
