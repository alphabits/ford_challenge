=====================
Session: Next Meeting
=====================

Start time:
    19-05-2011 15:00

End time:
    19-05-2011 16:00

Questions for this meeting:

    * When I calculate the running standard deviation, I sometimes get negative values. The values can be e.g. -1e-10. Should I do something about this, or just do the fast solution. Test if the value is negative. If yes, set value to 0.

    * The new PCA shows some promising clusters of primarily alert or not-alert points. Is it worth investigating further?

    * Is there any point in using a penalty, if I am only doing regression on 3 features? If I only use 3 features, I have already made a feature selection, and then the penalty should not be needed? ... Just found out that scikits.learn will not allow a penalty-value of 0... Hmmm

    * When doing crossvalidation on LogisticRegression with Inferences features, I got auc scores around 0.98 when I used only the first 10000 rows in the training data set. If I only used the first 1000 auc was aroun 0.75, and if I used the whole data set the auc was approx 0.82? OK found the reason. As already discovered the feature E9 is equal to isalert about 70% of the time. In the first 10000 rows E9 is equal to IsAlert 99% of the time!

    * Should I use the same rows when doing forward selection? I think it makes sense to use the same rows, so the feature selection isn't prematurely stopped, because of the randomly selected data.
