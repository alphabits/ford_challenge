=========================================
Session 12: Principal Components Analysis
=========================================

Start time:
    07-05-2011 16:36

Pause time:
    07-05-2011 17:40

Resume time:
    07-05-2011 21:40

End time:
    08-05-2011 01:46

In this session I am going to create a PCA of the raw data set. It will be interesting to se how much variation, that can be explained in just a few variables. I also need to find out what assumptions, about the data, that are made when a PCA is analyzed. First I need to use some time to get into the theory about PCA.

Many hours later...

I have read some theory and I like the descriptions of Bishop and Alpaydin the most. I need to write some theory when I get the time.


Simple PCA on whole data set
============================

First of I am going to calculate a PCA based on the whole data set, using the PCA implementation in the scikits.learn module.

.. note::

    Should I include the IsAlert feature when I make the PCA?

I am a bit surprised by the fact that the first pricipal component caries more than 90% of the total variance in the data. When the second and third principal component are included they account for more than 98% og all variantion.

I have made a couple of scatter plots in 2- and 3-dimensions and there dont seem to be a simple relation between the principal coordinates and the IsAlert feaeture. Instead there seems to be some "outliers" in the data, with data points having a first principal coefficient much higher than most datapoints.
