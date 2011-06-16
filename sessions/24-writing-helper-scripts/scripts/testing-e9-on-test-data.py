from __future__ import division
import numpy as np

from src.dataloaders import testset
from src.utils2 import c


T = testset()
length = T.shape[0]

fails_e9 = np.abs(T[:,c('E9')]-T[:,c('IsAlert')]).sum()
fails_v5 = np.abs(T[:,c('V5')]-T[:,c('IsAlert')]).sum()

print "Percent classified by E9: %.2f" % ((length - fails_e9)/length,) 
print "Percent classified by V5: %.2f" % ((length - fails_v5)/length,) 
