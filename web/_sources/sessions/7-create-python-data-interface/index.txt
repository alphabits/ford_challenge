=======================================
Session 7: Create Python data interface
=======================================

Start time
    15-03-2011 16:40

Pause time
    15-03-2011 17:53

Resume time
    15-03-2011 21:35

End time
    15-03-2011 23:02

In this session, I will try to create a simple interface to the dataset, to make it easier to work with the data. To illustrate the point, I would like to be able to do things like::

    from data import d

    # Plot feature P5 from trial 210
    d.t210.p5.plot()

    # Show my notes for a feature
    d.p5.notes()
    # or
    d.t210.p5.notes()

    # And of cause notes for trial 210
    d.t210.notes()

Which I managed to get done, sooner than I thought. Python is really nice! The source for the data_interface module is here

.. literalinclude:: /src/data_interface.py
    :language: python

.. note::

    Found a pretty serious bug in my first version of this code. Had coded the data_interface module as if the trial id was in the second column. It is in the first column!

Decided to make another data set without all trials where the IsAlert feature is zero in the whole trial. This leaves 339 trials. I had some trouble creating a script that would take a list of trial ids, and return all rows with a trial id in the list. The inefficient solution is to loop through the data on row at a time, and for every iteration, check if the trial id is in the list. I ended up with this

.. literalinclude:: /src/create_dataset_without_zero_trials.py
    :language: python
