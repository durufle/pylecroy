Examples
========

Connection
----------
Basic example, showing how to connect and get some device parameter values.

Connection to the device can be made using different type of interface:

- TCP/IP:   IP:a.b.c. (a,b,c,d := 0 to 255)
- LXI   :   VXI11:a.b.c.d (a,b,c,d := 0 to 255)
- USBTMC:   USBTMC:<VISA-Resource Name)

At oscilloscope level, interface can be change using the <Utility><Remote> menu.

Note that for TCP/IP and LXI interfaces, the oscilloscope Host name can be used instead.

.. code-block:: python

    from pylecroy.pylecroy import Lecroy

    ADDRESS_IP = "IP:10.67.16.26"
    ADDRESS_VXI = "VXI11:10.67.16.26"
    ADDRESS_USB = "USBTMC:USB0:00x5ff::0x0123::2814N62236::INSTR"

    if __name__ == '__main__':

        device = Lecroy(ADDRESS_IP)
        ...
        device.close()

Controlling Display
-------------------
This command domain allow to control the Display

.. code-block:: python

    from pylecroy.pylecroy import Lecroy
    from pylecroy.pylecroy import TriggerModes
    from pylecroy.pylecroy import Channels

    ADDRESS= "USBTMC:USB0:00x5ff::0x1023::2814N63170::INSTR"

    if __name__ == '__main__':
        device = Lecroy(ADDRESS)
        # Display channels
        print("Channels  ON...")
        for channel in [Channels.C1, Channels.C2, Channels.C3, Channels.C4]:
            device.display_channel(channel, "ON")
         device.close()
        ...
        print("Channels  OFF...")
        for channel in [Channels.C1, Channels.C2, Channels.C3, Channels.C4]:
            device.display_channel(channel, "OFF")
        ...
        print("Channels  C1,C2,C3 ON...")
        device.display_channel(Channels.C1, "ON")
        ...
        # Grid
        for state in GridStates.STATES:
            print("Grid state : " + state)
            device.grid = state
            time.sleep(0.5)
        device.grid = GridStates.SINGLE


Printing the Display/Screen Capture
-----------------------------------

.. code-block:: python

    from pylecroy.pylecroy import Lecroy
    from pylecroy.pylecroy import TriggerModes
    from pylecroy.pylecroy import Channels

    ADDRESS= "USBTMC:USB0:00x5ff::0x1023::2814N63170::INSTR"

    if __name__ == '__main__':

        device = Lecroy(ADDRESS)
        # Get current configuration
        print("hardcopy : {0}".format(device.get_hardcopy()))

        new_cfg = {'DEV': 'JPEG', 'FORMAT': 'LANDSCAPE'}
        device.set_hardcopy(new_cfg)

        # Get current configuration
        print("hardcopy : {0}".format(device.get_hardcopy()))

        new_cfg = {'DEV': 'BMP', 'FORMAT': 'PORTRAIT'}
        device.set_hardcopy(new_cfg)

        # Get current configuration
        print("hardcopy : {0}".format(device.get_hardcopy()))

        device.close()

Preserving and Restoring Waveforms
----------------------------------

.. code-block:: python

    from pylecroy.pylecroy import Lecroy
    from pylecroy.pylecroy import TriggerModes
    from pylecroy.pylecroy import Channels

    ADDRESS= "USBTMC:USB0:00x5ff::0x1023::2814N63170::INSTR"

    if __name__ == '__main__':

        device = Lecroy(ADDRESS)
        input("Get a signal on C1 and press a key to continue...")

        print("ShowChannels C1...")
        scope.display_channel(Channels.C1, "ON")

        # save C1 to M1
        print("Channel C1 save in M1...")
        device.save_memory(Channels.C1, Memories.M1)
        print("Show M1...")
        device.display_channel(Memories.M1, "ON")
        ...

