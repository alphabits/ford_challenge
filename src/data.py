from numpy import *

# Load training data set
A = loadtxt('data/fordTrain.csv', delimiter=',', skiprows=1)

# Load labels
L = loadtxt('data/labels.csv', delimiter=',', dtype=str)
