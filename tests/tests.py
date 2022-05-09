from pylecroy.pylecroy import Lecroy
from pylecroy.pylecroy import TriggerModes
from pylecroy.pylecroy import Channels
from pylecroy.pylecroy import GridStates
from pylecroy.pylecroy import Memories

import time

ADDRESS_USB = "USBTMC:USB0::0x05ff::0x1023::2816N63170::INSTR"
ADDRESS_TCP = "IP:10.67.0.35"

if __name__ == '__main__':
    # Connection
    device = Lecroy(ADDRESS_USB)

    # Get scope identifier
    print("scope identifier     : {} ".format(device.identifier))

    # Display channels
    print("Channels  OFF...")
    for channel in [Channels.C1, Channels.C2, Channels.C3, Channels.C4]:
        device.display_channel(channel, "OFF")
        time.sleep(0.5)

    print("Channels  ON...")
    for channel in [Channels.C1, Channels.C2, Channels.C3, Channels.C4]:
        device.display_channel(channel, "ON")
        time.sleep(0.5)

    print("Channels  OFF...")
    for channel in [Channels.C1, Channels.C2, Channels.C3, Channels.C4]:
        device.display_channel(channel, "OFF")
        time.sleep(0.5)

    device.display_channel(Channels.C1, "ON")
    print("Grid : {0}".format(device.grid))

    input("Get a signal on C1 and press a key to continue...")

    # grid state
    for state in GridStates.STATES:
        print("Grid state : " + state)
        device.grid = state
        time.sleep(0.5)

    device.grid = GridStates.SINGLE

    # Controlling Waveform capture
    for trigger in TriggerModes.MODES:
        device.trigger_mode = trigger
        print("scope trigger mode   : {}".format(device.trigger_mode))
        time.sleep(0.5)

    try:
        device.trigger_mode = "NONE"
    except ValueError as msg:
        print(msg)

    print("scope sequence       : {}".format(device.sequence))

    # HARDCOPY - Printing the Display/Screen Capture
    print("hardcopy : {0}".format(device.get_hardcopy()))
    new_cfg = {'DEV': 'JPEG', 'FORMAT': 'LANDSCAPE'}
    device.set_hardcopy(new_cfg)
    print("hardcopy : {0}".format(device.get_hardcopy()))
    device.store_hardcopy("C1")
    new_cfg = {'DEV': 'BMP', 'FORMAT': 'PORTRAIT'}
    device.set_hardcopy(new_cfg)
    print("hardcopy : {0}".format(device.get_hardcopy()))
    device.store_hardcopy("C1")

    # Preserving and Restoring Waveforms
    print("Set Trigger Single...")
    device.trigger_mode = TriggerModes.SINGLE
    # save C1 to M1
    print("Channel C1 save in M1...")
    device.save_memory(Channels.C1, Memories.M1)
    print("Show M1...")
    device.display_channel(Memories.M1, "ON")
    device.close()
