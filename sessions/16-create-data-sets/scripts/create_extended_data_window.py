import numpy as np

import src.dataloaders as d
from src.utils2 import create_extended_dataset_window


TrnD_ex = create_extended_dataset_window(d.trainingset())
TstD_ex = create_extended_dataset_window(d.testset())

np.save('data/trainingset_extended_window_30.npy', TrnD_ex)
np.save('data/testset_extended_window_30.npy', TstD_ex)
