===========================
Session 9: Data exploration
===========================

Start time
    26-04-2011 12:00

Pause time
    27-04-2011 04:20

This may be the first real working session. 

First I will calculate summary statistics for every feature across the whole data set. That leads to the abandoning of three features that turns out to be 0 in all rows.

.. literalinclude:: src/calculate_summary_statistics.py
    :language: python

.. literalinclude:: src/summary_statistics.json
    :language: javascript

As can be seen the result is saved to a json data file. What is worth noticing...

    * P8, V7, V9 is zero in all rows and can be discarded
    
    * V5, E9 could be binary

    * It looks like a little over half the time the drivers is alert... hmm... a little less than expected


Unique values
=============

To continue the exploration I wil try to calculate how many different values the various features span. That is done in a simple script

.. literalinclude:: src/calculate_unique_values.py
    :language: python

.. literalinclude:: src/unique_values.json
    :language: javascript

And what do we get? A couple of things

    * V5 and E9 are binary

    * E3 has 3 levels and V10 has 5 levels. That ain't that many and could be interesting to look closer into

    * 20 (not counting the three features with only one unique value) of the features have under 500 unique values, which actually surprises me a bit

    * P3 and P4 has exactly the same number of unique values. The same is true for P6 and P7. There also exists a couple of groups with almost the same number of unique values: (E10, E11), (E4, E5, E6) and (V4, V8)

Somehow the number of unique values for the different features seems interesting. The next thing to test how many unique values a feature assumes within a single trial. A script is created that for every feature and every trial calculates the number of unique values. The script is

.. literalinclude:: src/calculate_unique_values_pr_trial.py
    :language: python

The data is a bit to large to show here (about 15000 lines), so another script extracts the maximum unique values pr. trial for each feature and combines it with the number of unique values over the whole data set. The result is

.. literalinclude:: src/unique_values_combined.json
    :language: javascript

This did not create that many interesting results. A few things can be commented

    * P3 and P4 continues to have an equal number of unique values and so do P6 and P7

    * On the contrary the three groups (E10, E11), (E4, E5, E6) and (V4, V8) seems to have been separated more by the per trial count.

Now an interesting thing to notice is the feature V10. It has 5 unique values also when we calculate pr. trial. What are these 5 different values

.. code-block:: python

    import numpy as np
    from src.data_interface import trd

    np.unique(trd.V10.view())

Gives the following result

.. code-block:: python

    array([ 1.,  2.,  3.,  4.,  7.])

.. note::

    Could V10 be the gear? Maybe 7 is reverse?

Yet another thing to notice is the unique values of V3

.. code-block:: python

    >> np.unique(trd.V3.view())
    array([  240.,   241.,   242.,   243.,   244.,   253.,   254.,   255.,
         496.,   497.,   498.,   499.,   508.,   509.,   510.,   511.,
         752.,   753.,   754.,   755.,   756.,   764.,   765.,   766.,
         767.,  1008.,  1009.,  1010.,  1011.,  1020.,  1021.,  1022.,
        1023.])


They somehow seems to appear in groups of 3, 4 or 5: 240-244, 253-255, 496-499, 508-511, 752-756, 764-767, 1008-1011, 1020-1023


Binary features
===============

The features E9 and V5 are binary. I will try to see if they are in any way correlated to the IsAlert feature. A quick way to test it, is to calculate a new feature given as the distance between the feature (E9/V5) and IsAlert. The mean value of the calculated feature gives a hint about a possible correlation.

.. code-block:: python
    
    from numpy import abs
    from src.data_interface import trd

    >> diffE9 = abs(trd.E9.view() - trd.IsAlert.view())
    >> diffE9.mean()
    0.3071811343466328

    >> diffV5 = abs(trd.V5.view() - trd.IsAlert.view())
    >> diffV5.mean()
    0.53159132414897114

It actually looks as if E9 might be a good feature for the classifier


The gear idea
=============

Before I talked about the possibility that V10 is the gear placement. Can I test my idea in any way? Well it depends... First of all let's say that it is the gear. Then it could be an automatic gear or it could be a manual gear. Does it matter? If it is manual, you could hypothesise that if the gear level is changing the driver is somehow alert. It takes a little attention to manually change gear. On the other hand if the gear is automatic, it requires no attention to change it. But if it is automatic and it changes rapidly, the driver is probably accelerating. Maybe he is breaking because he was inattentive a moment ago. What do I get from all this? If the gear level has been constant for some time the probability of an inattentive driver increases... Sounds ok...


The big correlation hunt
========================

It is now time for the big correlation hunt which means I have to plot way to many scatter plots. More precisely there are 27 features and I like to create scatter plots of all pairs of features. This gives a total of

.. math::

    C = \frac{27!}{2!25!} = \frac{27\cdot 26}{2} = 13\cdot 27 = 351

Which isn't totally unmanagable... But how should I select which rows are included? There should probably only be between 50 and 100 rows in one scatter plot, and I would like about an equal number of rows with IsAlert=0 and IsAlert=1. Should the rows come from the same trial? And if they are from different trials shouldn't I normalize the features first. Speaking of normalization... I will try to normalize the features. Read more


Finding important features by logistic regression
=================================================
    


