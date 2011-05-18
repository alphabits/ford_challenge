====================================
Session 17: Recreating Winning Entry
====================================

Start time:
    17-05-2011 20:45

Pause time:
    17-05-2011 22:00

Resume time:
    18-05-2011 09:30

End time
    18-05-2011 13:23

In this session I will try to recreate Inference' winning entry. In :doc:`../13-recreating-winning-entry/index` I used Inference' coefficients directly, but as we discussed in :doc:`../14-meeting-with-morten/index` that is probably not a great idea, since the result will probably be overfitted. Also Inference do not tell his intercept-coefficient, so his approach can't be copied precisely anyway. Instead I'll start by doing a logistic regression on the same features as Inference used, and then see how good my classifier performs.


Testing performance on Inference' features with cross validation
================================================================

To test the performance of Inference' features a logistic regression is performed, with feature selection. The script to run the regression is

.. literalinclude:: scripts/inferences_features_cv.py

The script was run a couple of times and gave the results

.. literalinclude:: data/inference-features-cv-2.json
    :language: javascript

.. literalinclude:: data/inference-features-cv-3.json
    :language: javascript
