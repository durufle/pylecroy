Overview
********

This package encapsulates the access to a Lecroy oscilloscope. It provide basic function in order to communicate
with the device.

This package can be used only on Windows 32/64 platform.

Installation
============
You will need `Python 3+ <https://www.python.org>`_

This package use the ActiveDSO active X control from lecroy, you need to install it in your PC workstation.

This package is available under devpi server. So you can install it using pip tools as follow:

.. code-block:: bash

    pip install ragnarok-pylecroy


.. note::

    Refer to initialize pip application note in order to point on internal jfrog server.

You can install it from the wheel distribution package:

.. code-block:: bash

    pip install ragnarok-pylecroy-x.y.z-py3-none-any.whl

.. note::

    Replace x.y.z by the package version number.



Development
===========

The code of the package is developed under :file:`pylecroy` directory.

If you are developing new features inside the package, please follow `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_

Note that package will be used by other people, so stability matters.

* Follow `PEP20 <https://www.python.org/dev/peps/pep-0020/>`_

.. code-block:: rest

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

All necessary packages to develop are identified in the requirements.txt and development.txt files.

Clone the repository under you workspace

.. code-block:: bash

    $ cd ./workspace
    $ ~/workspace $ git clone https://github.com/durufle/pylecroy.git

After cloning, create a virtual environment, activate it and install necessary package:

.. code-block:: bash

    $ ~/workspace $ cd pylecroy
    $ ~/workspace/pylecroy $ python -m python -m venv venv
    $ ~/workspace/pylecroy $ source ./venv/bin/activate
    $ (venv) ~/workspace/pylecroy $

Install al required packages

.. code-block:: bash

    (venv) ~/workspace/pylecroy $ pip install -r requirements.txt
    (venv) ~/workspace/pylecroy $ pip install -r development.txt

To generate python package

.. code-block:: bash

    (venv) ~/workspace/pylecroy $ python -m build



