import numpy as np

from src.trainingset import D as TrnD
from src.testset import D as TstD
from src.utils2 import create_extended_dataset


TrnD_ex = create_extended_dataset(TrnD)
TstD_ex = create_extended_dataset(TstD)

np.save('data/trainingset_extended.npy', TrnD_ex)
np.save('data/testset_extended.npy', TstD_ex)
