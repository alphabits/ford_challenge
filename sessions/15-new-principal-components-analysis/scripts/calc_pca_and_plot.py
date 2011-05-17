from __future__ import division

import sys

import json
import matplotlib.pyplot as plt
from matplotlib import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scikits.learn.pca import PCA

from src.data_normalized_2 import DN, L
from src.utils import get_path, bool_to_color


path = get_path(__file__) + '/..'
L = list(L)

rotation_axis = 'x'
rotation_amount = 0
if len(sys.argv) == 3:
    rotation_axis = sys.argv[1]
    rotation_amount = int(sys.argv[2])
rotation_amount *= 2*np.pi/360


# Remove trial_id, obsnum and is alert
# I change notation here from D to X
X = DN[:,3:]

pca = PCA(n_components=30)
pca.fit(X)

plt.plot(np.cumsum(pca.explained_variance_ratio_), marker='o')
ax = plt.gca()
plt.title('Cumulative percentage of total variation explained by principal components')
ax.set_xlabel('Principal component')
ax.set_ylabel('% of total variation')
plt.savefig('{0}/plots/pca-variation-explained.pdf'.format(path), papertype='a4', format='pdf')
plt.cla()

W = pca.components_[:,0:3]
X_p = np.dot(X,W)

num_points = 800

rnd_rows = np.random.random_integers(0, X.shape[0], num_points)

colors = map(bool_to_color, DN[rnd_rows,L.index('IsAlert')])
plt.scatter(X_p[rnd_rows,0], X_p[rnd_rows,1], c=colors)
plt.title('Scatter plot of 1. and 2. pricipal component')
ax = plt.gca()
ax.set_xlabel('1. Pricipal component')
ax.set_ylabel('2. Principal component')
plt.savefig('{0}/plots/scatter-principal-components-{1}-points.pdf'.format(path, num_points), papertype='a4', format='pdf')
plt.cla()

for i in range(2):
    rnd_rows = np.random.random_integers(0, X.shape[0], num_points)
    colors = map(bool_to_color, DN[rnd_rows,L.index('IsAlert')])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X_p[rnd_rows,0], X_p[rnd_rows,1], X_p[rnd_rows,2], c=colors)
    plt.title('Scatter of 1., 2. and 3. pricipal component')
    ax = plt.gca()
    #ax.view_init(30, -60+i*90)
    ax.set_xlabel('1. Comp')
    ax.set_ylabel('2. Comp')
    ax.set_zlabel('3. Comp')
    fig.savefig('{0}/plots/scatter-principal-components-3d-{1}-{2}points.pdf'.format(path,i, num_points), papertype='a4', format='pdf')
    #fig.savefig('{0}/plots/scatter-principal-components-3d-rotated-{1}.pdf'.format(path, i*90), papertype='a4', format='pdf')
    pylab.close()

with open('{0}/data/calculated_pca.json'.format(path), 'w') as f:
    f.write(json.dumps(pca.components_.transpose().tolist(), indent=4))
