===================================
Session 5: First classifier attempt
===================================

Start time
    07-03-2011 23:01

Pause time
    08-03-2011 02:11

I will try to create my first classifier. I am by no means ready, but I was a bit shocked, when I realised that the official competition is going to end in two days. I can't finish this project without a single contribution to the original competition. Before I can start making a classifier, I am going to find a couple of features that looks promising.

.. note::

    Apparently trials 469-479 (both inclusive) is missing...


Feature safari
==============

First I am trying to find some interesting features. P3 and P4 looks promising. But after i plotted a scatter plot of 80 random inputs, I realised that the product of P3 and P4 is a constant (approx. 60000). Further investigations shows that the data varies between the different trials. I think that some of the features is corrupted in some of the trials. To get a better view of the data I will plot some of the features for 10-15 random trials. Links to the results:

First filtered by feature

.. toctree::

    E1
    E10
    E2
    E4
    E5
    E6
    IsAlert
    P1
    P4
    P5
    P6
    P7
    V1
    V11
    V2
    V3
    V6
    V8

And then by trial

.. toctree::

    t12
    t47
    t86
    t89
    t147
    t201
    t203
    t204
    t252
    t268
    t288
    t294
    t313
    t316
    t328
    t333
    t411
    t435
    t442
    t490
    t494
    t500
