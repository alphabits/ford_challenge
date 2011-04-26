===========================
Session 9: Data exploration
===========================

Start time
    26-04-2011 12:00

End time
    27-04-2011 05:00

This may be the first real working session. 

First I will calculate summary statistics for every feature across the whole data set. That leads to the abandoning of three features that turns out to be 0 in all rows.

After that I create scatter plots of all combination of features, to find possible good features for classification. Also it is found that some of the features are inversely proportional to each other, and hopefully some of the features turns out to be useful for use in the classifier. The total number of unique combinations of features are given by

.. math::

    C = \frac{25!}{2!23!} = \frac{25\cdot 24}{2} = 12\cdot 25 = 300

Which isn't totally unmanagable...
