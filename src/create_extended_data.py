import numpy as np

from data import D

trial_id = -1
cnt = 0

D_ex = np.zeros((D.shape[0], 93))

for i in range(D.shape[0]):
    if trial_id != D[i,0]:
        cnt = 0
        trial_id = D[i,0]
        sums = np.zeros((1,30))
        sums_sq = np.zeros((1,30))
    
    cnt += 1
    sums += D[i,3:]
    sums_sq += D[i,3:]**2

    D_ex[i,:33] = D[i,:]
    D_ex[i,33:63] = sums/cnt
    D_ex[i,63:93] = sums_sq/cnt - (sums/cnt)**2

np.save('data/fordTrainExtended.npy', D_ex)
