Utils
*****

Utils script are installed during package installation process

lcry_info
=========

This utility return some lecroy's parameter. It's useful to check if everything is setup properly
after package installation.

.. code-block::

    (venv) lcry_info
    scope address must be provide...

    Return information from Lecroy

    Usage:
        python lcry_info.py -a "IP:10.67.16.22"
        python lcry_info.py -a "USBTMC:<Host Name>"
        python lcry_info.py -a "VXI11:10.67.0.211"
        python lcry_info.py -a "ALIAS NAME"

    Options:
        -h, --help              this help message.
        -v, --version           version info.
        -a, --address           device IP address
