import pickle
import numpy as np

# Load training data set. The name A is kept for backward compability
A = np.load('data/fordTrain.npy')
D = A

# Load row numbers of cleaned data set
f = open('data/fordTrainNoZeroTrials.pckl', 'rb')
_clean_data_rows = pickle.load(f)
f.close()

# Clean data array
CD = A[_clean_data_rows, :]

# Load labels
L = np.loadtxt('data/labels.csv', delimiter=',', dtype=str)

