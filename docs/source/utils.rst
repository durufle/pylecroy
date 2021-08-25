Utils
=====

Utils script are installed during package installation process

lecroy_info
-----------
This utility return some lecroy's parameter. It's useful to check if everything is setup properly.

.. code-block::

    (venv) lecroy_info
    scope IP address must be provide...

    Return information from Lecroy

    Usage:
        python lecroy_info.py -a "IP:10.67.16.22"

    Options:
        -h, --help              this help message.
        -v, --version           version info.
        -a, --address           device IP address
