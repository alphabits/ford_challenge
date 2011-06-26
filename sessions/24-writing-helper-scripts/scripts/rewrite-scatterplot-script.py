import itertools as it

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

from src.dataloaders import trainingset
from src.utils2 import get_path, c, L


L = list(L[4:])
D = trainingset()

path = get_path(__file__) + '/..'
savepath_template = '{0}/plots/scatterplots/{1}-{2}.pdf'
num_points = 100

rows = np.random.random_integers(0,D.shape[0]-1, num_points)
data = D[rows,:]

colors = map(lambda x: 'blue' if x==1 else 'red', data[:,c('IsAlert')])
blue = Rectangle((0,0),1,1,fc='b')
red = Rectangle((0,0),1,1,fc='r')

exclude = ['V7', 'V9', 'P8', 'E3', 'E7', 'E8', 'E9', 'V3', 'V5', 'V10']
features = [f for f in L if f not in exclude]

for f1, f2 in it.combinations(features, 2):
    plt.title('Feature {0} vs {1} ({2} points)'.format(f1, f2, num_points), 
            {'size': 20})
    plt.legend((blue, red), ('Alert', 'Not Alert'))
    plt.scatter(data[:,c(f1)], data[:,c(f2)], c=colors)
    plt.gca().set_xlabel(f1, {'size': 18})
    plt.gca().set_ylabel(f2, {'size': 18})
    plt.savefig(savepath_template.format(path,f1,f2), format='pdf', 
            papertype='a4')
    plt.cla()
