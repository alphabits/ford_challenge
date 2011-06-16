import numpy as np


L = np.loadtxt('data/labels.csv', delimiter=',', dtype=str)
L_clean = [l for l in L if l not in ['P8','V7','V9','ObsNum','TrialID']]

if len(L_clean) % 2 != 0:
    L_clean.append(None)


def gen_graphic_string(feature):
    return r'\includegraphics[width=.5\textwidth]{../sessions/11-boxplots-scatterplots/plots/boxplots/%s-t0-t50.pdf}' % (feature,)

lines = []

for i in range(len(L_clean)/2):
    left = gen_graphic_string(L_clean[2*i])
    right = gen_graphic_string(L_clean[2*i+1]) if L_clean[2*i+1] != None else ''
    lines.append('{0} &\n {1}'.format(left, right))

print '\\\\\n'.join(lines)
