import pickle
import numpy as np

# Load training data set. The name A is kept for backward compability
DN = np.load('data/fordTrainNormalized2.npy')

# Load labels
L = np.loadtxt('data/labels.csv', delimiter=',', dtype=str)

