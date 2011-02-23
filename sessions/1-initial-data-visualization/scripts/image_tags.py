from numpy import loadtxt

L = loadtxt('data/labels.csv', delimiter=',', dtype=str)

for i in range(len(L)):
    print '''.. image:: plots/boxplots-{0}.png
    :width: 750px
    '''.format(L[i])

