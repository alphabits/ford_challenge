import matplotlib.pyplot as plt
from matplotlib import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scikits.learn.pca import PCA

from src.data_interface import d, L_clean, L
from src.utils import get_path, bool_to_color


path = get_path(__file__) + '/..'
L = list(L)

# Remove trial_id, obsnum and is alert
# I change notation here from D to X
X = d.view()[:,3:]

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

rnd_rows = np.random.random_integers(0, X.shape[0], 120)

colors = map(bool_to_color, d.view()[rnd_rows,L.index('IsAlert')])
plt.scatter(X_p[rnd_rows,0], X_p[rnd_rows,1], c=colors)
plt.title('Scatter plot of 1. and 2. pricipal component')
ax = plt.gca()
ax.set_xlabel('1. Pricipal component')
ax.set_ylabel('2. Principal component')
plt.savefig('{0}/plots/scatter-principal-components.pdf'.format(path), papertype='a4', format='pdf')
plt.cla()

for i in range(8):
    rnd_rows = np.random.random_integers(0, X.shape[0], 120)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X_p[rnd_rows,0], X_p[rnd_rows,1], X_p[rnd_rows,2], c=colors)
    plt.title('Scatter of 1., 2. and 3. pricipal component')
    ax = plt.gca()
    ax.set_xlabel('1. Comp')
    ax.set_ylabel('2. Comp')
    ax.set_zlabel('3. Comp')
    fig.savefig('{0}/plots/scatter-principal-components-3d-{1}.pdf'.format(path,i), papertype='a4', format='pdf')
    pylab.close()
