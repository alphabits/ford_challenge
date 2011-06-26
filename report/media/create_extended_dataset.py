import numpy as np


def create_extended_dataset(D):
    cnt = 0
    D_ex = np.zeros((D.shape[0], 94))
    std_first_row = np.zeros((1,30))

    for i in range(D.shape[0]):
        if D[i,c.obsnum] == 0: 
            cnt = 0
            sums = np.zeros((1,30))
            sums_sq = np.zeros((1,30))
        
        cnt += 1
        sums += D[i,4:]
        sums_sq += D[i,4:]**2

        D_ex[i,:34] = D[i,:]

        # Calculate running mean
        D_ex[i,34:64] = sums/cnt
        
        # Calculate running std
        # Avoid dividing by zero in first row
        if cnt > 1:
            tmp_var = (cnt*sums_sq - sums**2)/(cnt*(cnt-1))
            tmp_var[:,np.nonzero(tmp_var<0)[1]] = 0
            D_ex[i,64:94] = np.sqrt(tmp_var)
        else:
            D_ex[i,64:94] = std_first_row

    return D_ex