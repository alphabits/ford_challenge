==============================
Session 6: Meeting with Morten
==============================

Start time
    08-03-2011 09:10

End time
    08-03-2011 10:30

This morning I had a great meeting with Morten where I showed him plots from :doc:`session 5 <../5-first-classifier-attempt/index>`, I got some feedback about the next step in the project. We agreed that I should look into these subjects:

    * Get a thorough understanding of the data. Especially I need to find out how many trials have most features in good shape. Based on how many trials are in good shape, I need to pick out a subset of trials as test data.

    * The range of some of the features varies alot between different trials. I should try to normalize features across the different trials, so the range of a feature is consistent.

    * To test the effect of the normalization, I should try to calculate the mutual information between each feature and the IsAlert-feature. The mutual information rising after the normalization, indicates that the normalization will enhance the classifier performance.

    * And finally I should get my first classifier up and running! This is high up on the todo-list. Six weeks have passed and still no classifier...
