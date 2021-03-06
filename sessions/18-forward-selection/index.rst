=============================
Session 18: Forward Selection
=============================

Start time:
    18-05-2011 16:14

End time:
    18-05-2011 22:02

In this session I will try to find the features that makes the best classifier. Maybe I can find some features that achieve a higher auc than the winning entry's. The script that I use to make forward selection is shown here

.. literalinclude:: scripts/forward_selection.py

First the script was run for 3000 training samples and 1000 test samples; both taken from the training dataset. The result was

.. literalinclude:: data/forward-selection-results-1-for-docs.json
    :language: javascript

And after that the script was run one more time for 10000 training samples and 5000 test samples. The results

.. literalinclude:: data/forward-selection-results-2-for-docs.json
    :language: javascript

In both results, the script was allowed to run as long as the auc score increased in every iteration. In the first run some 20 features were selected, and in the second run some 40 was selected. The second run took about 100 minutes to finish, and I think that the last 30 features is overfitting galore. If i need to do another run the number of features to select should be capped. Maybe 10 features max? 20?


Testing the top 4 features
==========================

In this section I will test the performance of a model, consisting of the top 4 features from the second feature selection. The same script as was used in :doc:`../17-recreating-winning-entry/index` is used here to make a cross validation of the performance. The results for the top 4 features are

.. literalinclude:: data/top-4-features-auc-score.json
    :language: javascript

Likewise the top three features was tested and here the results was

.. literalinclude:: data/top-3-features-auc-score.json
    :language: javascript


