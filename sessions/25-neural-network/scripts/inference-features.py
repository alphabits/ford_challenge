from __future__ import division

import json

import numpy as np
import matplotlib.pyplot as plt

from src.utils2 import c_ex as c, get_path, get_bins, get_random_subset
from src.neural_network import train_network, calculate_auc_score
import src.dataloaders as d


path = get_path(__file__) + '/..'


num_bins = 10
hidden_units = 12
learningrate = 0.04
max_epochs = 8
continue_epochs = 2
training_size = 100000
feature_set = 'winner'

if feature_set == 'winner':
    features = ['sde5', 'v11', 'e9']
elif feature_set == 'forward':
    features = ['sde1', 'v11', 'e9']
else:
    raise Exception('Unknown feature set')


if training_size == 'all':
    D = d.trainingset_extended()
    training_size = int(D.shape[0])
else:
    D = get_random_subset(d.trainingset_extended(), training_size)
T = d.testset_extended()

cols = c(*features)

Xt = T[:, cols]
yt = T[:, c.isalert]


bins = get_bins(T.shape[0], num_bins)

neural_network = train_network(D[:, cols], D[:, c.isalert], 
        hidden_units=hidden_units, learningrate=learningrate, 
        max_epochs=max_epochs, continue_epochs=continue_epochs)

auc = num_bins*[0]
fpr = num_bins*[0]
tpr = num_bins*[0]

for i in range(num_bins):
    rows = bins[i]
    auc[i], fpr[i], tpr[i] = calculate_auc_score(neural_network, Xt[rows,:], yt[rows])



def save_result(save_path):
    with open(save_path, 'w') as f:
        json.dump(get_result(), f, indent=4)

def get_result():
    save_data = dict(zip(
        ['auc', 'num_bins', 'dataset_size', 'generator', 'fpr', 'tpr',
         'hidden_units', 'learningrate', 'max_epochs', 'continue_epochs',
         'training_size', 'features'], 
        [auc, num_bins, D.shape[0], __file__, [a.tolist() for a in fpr], 
         [a.tolist() for a in tpr], hidden_units, learningrate, max_epochs,
         continue_epochs, training_size, features]
    ))
    return save_data

def plot_roc_curve(run, title):
    plt.plot(fpr[run], tpr[run], linewidth=3)
    plt.xlabel('False positive rate', {'size': 16})
    plt.ylabel('True positive rate', {'size': 16})
    plt.title(title, {'size': 18})

def save_plot(filename):
    plt.savefig(path+'/plots/'+filename+'.pdf')

