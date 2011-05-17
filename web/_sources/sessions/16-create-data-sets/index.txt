============================
Session 16: Create Data Sets
============================

Start time:
    16-05-2011 22:55

End time:
    16-05-2011 23:32

I am going to create the official training set and test set. First the unique line number is added as the first column. That way new data sets can be created, without duplicating all the original data. The training data set consists of all trials that has an id not divisible by 5. Trials with an id divisible with 5 is in the test data set. The code to generate the two data sets is

.. literalinclude:: /src/create_test_and_training_data_set.py

After the training- and test dataset was created, I made the corresponding extended datasets. The function that creates the extended datasets is in the `utils2` module

.. literalinclude:: /src/utils2.py
    :pyobject: create_extended_dataset


Creating the window dataset
===========================

Now it is time to create the window dataset. This dataset includes features for the window mean and window standard deviation. I will start with a window size of 30. The function to create a dataset with window features is a lot like the function to create the dataset with running features.

.. literalinclude:: /src/utils2.py
    :pyobject: create_extended_dataset_window
