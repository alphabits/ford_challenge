# Session: 1-initial-data-visualization

from data import *
import matplotlib.pyplot as plt

SESSION_PATH = 'sessions/1-initial-data-visualization/plots'

plt.cla()

for i in range(len(L)):
    plt.title('Histogram for {0}'.format(L[i]))
    plt.hist(A[:, i], 50)
    plt.savefig('{0}/hist-{1}.png'.format(SESSION_PATH, L[i]), format='png', dpi=100)
    plt.cla()
