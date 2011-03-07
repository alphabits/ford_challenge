import numpy as np

# Load training data set
A = np.load('data/fordTrain.npy')

# Load labels
L = np.loadtxt('data/labels.csv', delimiter=',', dtype=str)
