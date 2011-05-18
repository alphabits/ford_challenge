===========================
Session 19: Window Features
===========================

Start time:
    18-05-2011 22:09

End time:
    18-05-2011 23:40

In this session I try to test whether a better performance can be achieved, when the running features are exchanged with windows instead. It is more or less a copy of the work done in :doc:`../17-recreating-winning-entry/index` and :doc:`../18-forward-selection/index`.


Using Inference's features
==========================

First of the features of Inference are used to train a model. Cross validation is used, just like the previous sessions. The result is

.. literalinclude:: data/inferences-features-4-bins.json
    :language: javascript

It is seen that the auc scores are decreased a little compared to the results when the running features was used.


Forward selection
=================

Forward selection was done on the data set with the window features. The results are

.. literalinclude:: data/feature-selection-for-docs.json
    :language: javascript

Testing the features selected
-----------------------------

To test the features selected, a cross validation on the model with the top 4 features is performed.

.. literalinclude:: data/testing-top-4-features-selected-4-bins.json
    :language: javascript


