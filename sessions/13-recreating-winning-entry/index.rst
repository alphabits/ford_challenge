====================================
Session 13: Recreating Winning Entry
====================================

Start time:
    08-05-2011 09:44

Pause time:
    08-05-2011 12:05

Resume time:
    09-05-2011 08:30

Pause time:
    09-05-2011 11:24

In this session I will try to emulate the approach that got Inference his first place in the ford competition. Some of the key elements extracted from :download:`his description</documents/inference_on_winning.pdf>` are that he:

    * Trained logistic model with 20% of (random?) training trials, which means 100 trials. I am going to use 25% as my training data set only have 400 trials.

    * He measured performance on remaining 400 trials, which for me is going to be 300 trials.

    * First he used aggregate features based on whole trials, but midway through the competition demanded that an online model was constructed, so Inference had to use running features instead. It hurt his performance a little bit.

    * Conducted feature selection on diagnostics of logistic regression.

    * Also trained some models on the whole training set using "a generalised-linear-model training approach and also the model obtained by optimising the training set AUC by numerical optimisation of the model parameters"


Logistic Regression on first 1e5 rows
=====================================

First I try to train a logistic regression on the first 1e5 rows of the training data set. I haven't added any features. The code is shown below

.. literalinclude:: scripts/inferences_approach.py
    :language: python

When run it saves the fitted parameters in a json file shown next

.. literalinclude:: data/coefs_train_0-1e5.json
    :language: javascript


ROC-curve calculation interlude
===============================

When I tried to calculate the ROC of af test set with 1e5 records python froze. The ROC implementation in scikits.learn calculates the FPR and TPR for **every unique** value of the prediction score. I have altered the implementation a little bit, by adding af third input "thresholds", so the user can specify the steps between each calculation of FPR, TPR. Around 1000 steps seems to give a nice picture of the ROC.


Calculate running mean and std
==============================

To be able to recreate the winning entry from Inference I have to create an extended data set, with the running mean and std of every feature. The data set therefore ends as a 90-dimensional dataset. The code to calculate the extra features is

.. note::

    There are errors in the following code. The right way to calculate the extended data set can be seen in :doc:`../16-create-data-sets/index`

.. literalinclude:: /src/create_extended_data.py


Check that I get approx the same AUC as inference
=================================================

.. note::

    This code is based on the extended data set with errors in the calculation. The following results are therefore wrong.

Before I try to recreate the winning approach, I want to test that I actually get the same AUC as Inference, if I just hardcode the coefficients into the model. The code to calculate the AUC of the hard coded model is

.. literalinclude:: scripts/hard_coded_coefficients.py

And gave the results

.. literalinclude:: data/hard-coded-results-5-tests.json
    :language: javascript

.. note::

    Check that I have calculated the running features correct
