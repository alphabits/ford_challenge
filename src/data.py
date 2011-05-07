import pickle
import numpy as np

# Load training data set. The name A is kept for backward compability
A = np.load('data/fordTrain.npy')
D = A

# Load row numbers of cleaned data set
f = open('data/fordTrainNoZeroTrials.pckl', 'rb')
_clean_data_rows = pickle.load(f)
f.close()

# Load row number of training data set
f = open('data/my_training_data_set_row_ids.pckl', 'rb')
_training_data_rows = pickle.load(f)
f.close()

# Clean data array
CD = A[_clean_data_rows, :]

# Training data set
TRD = A[_training_data_rows, :]

# Load labels
L = np.loadtxt('data/labels.csv', delimiter=',', dtype=str)
L_clean = [l for l in L if l not in ['P8','V7','V9','ObsNum','TrialID']]


