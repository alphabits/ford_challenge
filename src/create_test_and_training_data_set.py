import numpy as np

from src.data import D


test_rows = []
training_rows = []

for i in xrange(D.shape[0]):
    if D[i,0] % 5 == 0:
        test_rows.append(i)
    else:
        training_rows.append(i)

to_save = [
    ('data/trainingset.npy', training_rows),
    ('data/testset.npy', test_rows)
]

for path, rows in to_save:
    tmp = np.zeros((len(rows), 34))
    tmp[:,1:] = D[rows,:]
    tmp[:,0] = np.array(rows)
    np.save(path, tmp)