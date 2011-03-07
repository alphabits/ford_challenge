import os, sys

from src.data import A, L
import numpy as np
import matplotlib.pyplot as plt

cwd = os.path.abspath(os.path.dirname(__file__))

for i in range(5, len(L)):
    f = open(cwd + '/../' + L[i] + '.rst.auto', mode='w')
    label_len = len(L[i])
    hist_rel_path = 'plots/' + L[i] + '-hist.png'
    hist_path = cwd + '/../' + hist_rel_path
    box_rel_path = 'plots/' + L[i] + '-box.png'
    box_path = cwd + '/../' + box_rel_path
    stats = {}
    stats["a-Min"] = np.min(A[:, i])
    stats["b-Max"] = np.max(A[:, i])
    stats["c-Mean"] = np.mean(A[:, i])
    stats["d-Std"] = np.std(A[:, i])
    lines = []
    lines.append(label_len*'=')
    lines.append(L[i].upper())
    lines.append(label_len*'=')
    lines.append('')
    keys = stats.keys()
    keys.sort()
    for k in keys:
        lines.append('**%s**: %s' % (k[2:], stats[k]))
    lines.append('')
    lines.append('.. image:: %s' % (hist_rel_path,))
    lines.append('    :width: 550px')
    lines.append('')
    lines.append('.. image:: %s' % (box_rel_path,))
    lines.append('    :width: 550px')
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(A[:,i], bins=30)
    fig.savefig(hist_path)
    fig.clear()
    ax = fig.add_subplot(111)
    ax.boxplot(A[:,i])
    fig.savefig(box_path)
    '''
    f.write("\n".join(lines))
    f.close()

