=======================================
Session: 20 Meeting with Morten and Ole
=======================================

Start time:
    19-05-2011 15:00

End time:
    19-05-2011 15:40

Questions for this meeting:

    * When I calculate the running standard deviation, I sometimes get negative values. The values can be e.g. -1e-10. Should I do something about this, or just do the fast solution. Test if the value is negative. If yes, set value to 0.

    * The new PCA shows some promising clusters of primarily alert or not-alert points. Is it worth investigating further?

    * Is there any point in using a penalty, if I am only doing regression on 3 features? If I only use 3 features, I have already made a feature selection, and then the penalty should not be needed? ... Just found out that scikits.learn will not allow a penalty-value of 0... Hmmm

    * When doing crossvalidation on LogisticRegression with Inferences features, I got auc scores around 0.98 when I used only the first 10000 rows in the training data set. If I only used the first 1000 auc was aroun 0.75, and if I used the whole data set the auc was approx 0.82? OK found the reason. As already discovered the feature E9 is equal to isalert about 70% of the time. In the first 10000 rows E9 is equal to IsAlert 99% of the time!

    * Should I use the same rows when doing forward selection? I think it makes sense to use the same rows, so the feature selection isn't prematurely stopped, because of the randomly selected data.

    * When doing forward selection, does it make sense to limit the number of features selected?


Result of this meeting
======================

I thought that I would just meet with Morten, but instead we went to see Ole. I told Ole about the status of my work so far (i have made data visualization, pca, tried to recreate the winning approach, tried forward selection, and tried to use windows features instead of running features). Ole suggested that I tried an L1 regularized logistic regression (Lasso) to see what results that would give. Since scikits.learn have an build-in option for this, it should be no problem to play with. An idea then, is to do a cross-validation on the regularization parameter, to see what gives the smallest error.
Also, I got to show Morten a couple of my results from the last 3-4 sessions. Morten remarked that the normal precedure is to do a 10-fold cross validation for every candidate feature for every step in the forward selection. As the forward selection already takes 1.5 hours I think I will skip this step. Morten also noted that I should try to use all the features from the forward selection, even though it seems to be overfitting when it selects 23 features. It could be interesting to compare with the lasso approach.
