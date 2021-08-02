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

        # Get scope identifier identify
        device.identify()
        print("scope identifier : {} ".format(device.identifier))
        # get current Hardcopy file name
        print("Get Current Hardcopy file name : {} ".format(device.get_hardcopy(device.FILE)))

        device.close()