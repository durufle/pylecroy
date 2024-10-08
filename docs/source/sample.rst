Examples
********
You can found here some examples.

Connection to the device can be made using different type of interface:

- TCP/IP:   IP:a.b.c. (a,b,c,d := 0 to 255)
- LXI   :   VXI11:a.b.c.d (a,b,c,d := 0 to 255)
- USBTMC:   USBTMC:<VISA-Resource Name)

At oscilloscope level, interface can be change using the <Utility><Remote> menu.

Note that for TCP/IP and LXI interfaces, the oscilloscope Host name can be used instead.


Basic
=====

Basic example, showing how to connect and get some device parameter values.

.. literalinclude:: ../../examples/basic.py


Multiple
========

Multiples command such display channel, Set grid format, ...

.. literalinclude:: ../../examples/multiple.py


Parameters
==========

Parameter related command usage.

.. literalinclude:: ../../examples/parameters.py


settings
========

settings parameters examples.

.. literalinclude:: ../../examples/settings.py

single
======

Get wave from a single channel.

.. literalinclude:: ../../examples/single.py


sequence
========

Acquisition using sequence

.. literalinclude:: ../../examples/sequence.py
