D = csvread('../../../data/fordTrain.csv', 2, 0);
[eigvec, transformed, eigval] = princomp(D(:,4:end));

eigval
