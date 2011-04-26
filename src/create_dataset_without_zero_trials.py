import pickle

from src.data import A


f = open('data/trials_to_keep.pckl', 'rb')
ttk = pickle.load(f)
f.close()

rtk = []
ttk.reverse()

cur = 0 # The trial with id 0 is missing from ttk
match = False

for i in range(A.shape[0]):
    if A[i,0] == cur:
        rtk.append(i)
        match = True
    else:
        if match:
            if len(ttk) == 0:
                break
            match = False
            cur = ttk.pop()
            if A[i,0] == cur:
                rtk.append(i)
                match = True

f = open('data/fordTrainNoZeroTrials.pckl', 'wb')
pickle.dump(rtk, f)
f.close()
