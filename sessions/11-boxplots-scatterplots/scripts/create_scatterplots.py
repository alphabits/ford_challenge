import itertools as it

import matplotlib.pyplot as plt
import numpy as np

from src.data_interface import d, L
from src.utils import get_path

L = list(L)
D = d.view()

path = get_path(__file__) + '/..'
savepath_template = '{0}/plots/scatterplots/{1}-{2}.pdf'

rows = np.random.random_integers(1,200000,400)

data = D[rows,:]

def is_alert_colors(is_alert):
    return 'blue' if is_alert==1 else 'red'

colors = map(is_alert_colors, data[:,L.index('IsAlert')])

#features = ['P6', 'V1', 'V3', 'V6']
features = L[4:]

for f1, f2 in it.combinations(features, 2):
    idx1, idx2 = L.index(f1), L.index(f2)
    plt.title('Feature {0} vs {1}'.format(f1, f2), {'size': 20})
    plt.scatter(data[:,idx1], data[:,idx2], c=colors)
    plt.gca().set_xlabel(f1, {'size': 18})
    plt.gca().set_ylabel(f2, {'size': 18})
    plt.savefig(savepath_template.format(path,f1,f2), format='pdf', papertype='a4')
    plt.cla()

