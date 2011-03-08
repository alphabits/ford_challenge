import os

import numpy as np
from matplotlib import pyplot as plt

from src.data import L
from src.utils import get_trial, get_path


sess_root = get_path(__file__) + '/..'
plot_dir = sess_root + '/plots'

by_trial = {}
by_feature = {}

def get_plotname(trial, feature):
    return '%s-%s.png' % (trial, feature)

for f in os.listdir(plot_dir):
    (t_str, rest) = f.split('-')
    (f_str, ext) = rest.split('.')
    if not by_trial.has_key(t_str):
        by_trial[t_str] = []
    if not by_feature.has_key(f_str):
        by_feature[f_str] = []
    by_trial[t_str].append(f_str)
    by_feature[f_str].append(t_str)

for k in by_feature:
    trials = by_feature[k]
    lines = []
    lines.append(len(k)*'=')
    lines.append(k)
    lines.append(len(k)*'=')
    lines.append('')
    for t in trials:
        lines.append('.. image:: plots/%s' % (get_plotname(t, k),))
        lines.append('    :width: 550px')
        lines.append('')
    path = sess_root + '/' + k + '.rst'
    page = open(path, 'w')
    page.write("\n".join(lines))

for t in by_trial:
    features = by_trial[t]
    lines = []
    lines.append(len(t)*'=')
    lines.append(t)
    lines.append(len(t)*'=')
    lines.append('')
    for feat in features:
        lines.append('.. image:: plots/%s' % (get_plotname(t, feat),))
        lines.append('    :width: 550px')
        lines.append('')
    path = sess_root + '/' + t + '.rst'
    page = open(path, 'w')
    page.write("\n".join(lines))
