import numpy as np

from src.data import D


test_rows = []
training_rows = []

for i in xrange(D.shape[0]):
    if D[i,0] % 5 == 0:
        test_rows.append(i)
    else:
        training_rows.append(i)

TrD = np.zeros((len(training_rows), 34))
TrD[:,1:] = D[training_rows,:]
TrD[:,0] = np.array(training_rows)

TsD = np.zeros((len(test_rows), 34))
TsD[:,1:] = D[test_rows,:]
TsD[:,0] = np.array(test_rows)

np.save('data/trainingset.npy', TrD)
np.save('data/testset.npy', TsD)
