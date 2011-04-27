import json, pickle

from src.data import A


f = open('data/training_trial_ids.json', 'r')
ttk = json.load(f)
f.close()

rtk = []
ttk.reverse()

cur = ttk.pop() 
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

f = open('data/my_training_data_set_row_ids.pckl', 'wb')
pickle.dump(rtk, f)
f.close()
