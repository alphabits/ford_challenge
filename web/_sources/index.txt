======================================================
Detection of human alertness using supervised learning
======================================================

.. toctree::
    :maxdepth: 2

    sessions/index

Some examples
=============

.. code-block:: python

    import numpy as np

    def my_func():
        print 'Hallo'

And maybe I want to talk a bit about some math related issues

.. math::

    \int_a^b \exp{(x^2)}\, dx

That was some math. What about a plot?

.. plot::

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0,2,1000)

    plt.figure()
    plt.plot(x, np.sqrt(x), label=r"Skiing $\sqrt{x}$")
    plt.title("Learning curves")
    plt.show()

It should work to. But what about literal includes of code?

.. literalinclude:: src/__init__.py
    :pyobject: my_func

Yep it worked. Now some tables

.. table:: Truth table for "not"

    =====  =====
      A    not A
    =====  =====
    False  True
    True   False
    =====  =====
    
Did that work? Yes and what about a csv-table?

.. csv-table:: CSV-table
    :header: "Opgave", "Uge 1", "Uge 2", "Uge 3"
    :widths: 70, 10, 10, 10
    
    "Dataundersøgelse", "\•", "\•", ""
    "Teorilæsning", "\•", "\•", ""
    
Oh it did work!
