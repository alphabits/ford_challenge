import json
import random

import numpy as np

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets.classification import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SigmoidLayer

import src.dataloaders as d
from src.utils2 import c


D = d.testset()

a = range(D.shape[0])
random.shuffle(a)

num_train_rows = 10000
num_test_rows = 5000

tr_rows = a[:num_train_rows]
ts_rows = a[num_train_rows:(num_train_rows+num_test_rows)]

features = ['V11', 'sdE5', 'E9']

X = D[tr_rows, c(*features)]
Y = D[tr_rows, c('IsAlert')]
Xt = D[ts_rows, c(*features)]
Yt = D[ts_rows, c('IsAlert')]

nn = buildNetwork(3, 3, 1, outclass=SigmoidLayer)
ds = ClassificationDataSet(3, 1)
for i, row in enumerate(X):
    ds.addSample(row, Y[i])
trainer = BackpropTrainer(nn, ds)
