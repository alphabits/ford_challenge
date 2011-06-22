import numpy as np

from pybrain.structure import SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets.classification import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork

from scikits.learn.metrics import auc

from src.utils2 import roc_curve



def train_network(X, y, hidden_units=3, learningrate=0.04, max_epochs=8, continue_epochs=2):
    indim = X.shape[1]
    nn = buildNetwork(indim, hidden_units, 1, outclass=SigmoidLayer)
    ds = ClassificationDataSet(indim, 1)
    for i, row in enumerate(X):
        ds.addSample(row, y[i])
    trainer = BackpropTrainer(nn, ds, learningrate=learningrate)
    trainer.trainUntilConvergence(maxEpochs=max_epochs, continueEpochs=continue_epochs)
    return nn

def calculate_auc_score(nn, X, y):
    probabilities = np.array([nn.activate(row).tolist() for row in X])
    fpr, tpr, thresholds = roc_curve(y, probabilities, 
            thresholds=np.linspace(0,1,1e3))
    auc_score = auc(fpr, tpr)
    return auc_score, fpr, tpr

