# Session: 1-initial-data-visualization

from data import *
import matplotlib.pyplot as plt

SESSION_PATH = 'sessions/1-initial-data-visualization/plots'

plt.cla()

for i in range(len(L)):
    plt.title('Boxplot for {0}'.format(L[i]))
    plt.boxplot(A[:, i])
    plt.savefig('{0}/boxplot-{1}.png'.format(SESSION_PATH, L[i]), format='png', dpi=100)
    plt.cla()
