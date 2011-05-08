====================================
Session 13: Recreating Winning Entry
====================================

Start time:
    08-05-2011 09:44

End time:
    08-05-2011 09:44

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
