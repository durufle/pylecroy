"""
Multiple command module
"""
import argparse
import time
import sys
from pylecroy.pylecroy import Lecroy
from pylecroy.pylecroy import Trigger
from pylecroy.pylecroy import WaveForm
from pylecroy.pylecroy import Display
from pylecroy.pylecroy import Grid


ADDRESS_USB = "USBTMC:USB0::0x05ff::0x1023::2816N63170::INSTR"
ADDRESS_TCP = "IP:10.67.0.35"
ADDRESS_VXI11 = "VXI11:10.67.0.211"


def main():
    """
    Main entry
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', help='device visa name or address.')
    args = parser.parse_args()

    device = Lecroy(args.name)

    # Get scope identifier
    print(f"scope identifier     : {device.identifier} ")
    device.display_channel('C1', 'OFF')

    # Display channels
    print("Channels  OFF...")
    for channel in [Display.Channels.C1, Display.Channels.C2, Display.Channels.C3, Display.Channels.C4]:
        device.display_channel(channel, "OFF")
        time.sleep(0.5)

    print("Memories  OFF...")
    for memory in [Display.Channels.M1, Display.Channels.M2, Display.Channels.M3, Display.Channels.M4]:
        device.display_channel(memory, "OFF")
        time.sleep(0.5)

    print("Channels  ON...")
    for channel in [Display.Channels.C1, Display.Channels.C2, Display.Channels.C3, Display.Channels.C4]:
        device.display_channel(channel, "ON")
        time.sleep(0.5)

    print("Channels  OFF...")
    for channel in [Display.Channels.C1, Display.Channels.C2, Display.Channels.C3, Display.Channels.C4]:
        device.display_channel(channel, "OFF")
        time.sleep(0.5)

    device.display_channel(Display.Channels.C1, "ON")
    print(f"Grid : {device.grid}")
    input("Get a signal on C1 and press a key to continue...")
    # grid state
    for state in Grid.States:
        print(f"Grid state : {state.value}")
        device.grid = state
        time.sleep(0.5)

    device.grid = Grid.States.SINGLE

    # Controlling Waveform capture
    for trigger in Trigger.Modes:
        device.trigger_mode = trigger
        print(f"scope trigger mode   : {device.trigger_mode}")
        time.sleep(0.5)

    try:
        device.trigger_mode = "NONE"
    except ValueError as msg:
        print(msg)

    print(f"scope sequence       : {device.sequence}")

    # HARDCOPY - Printing the Display/Screen Capture
    print(f"hardcopy : {device.hardcopy}")
    new_cfg = {'DEV': 'BMP', 'FORMAT': 'LANDSCAPE'}
    device.hardcopy = new_cfg
    print(f"hardcopy : {device.hardcopy}")
    device.store_hardcopy("C1")
    new_cfg = {'DEV': 'JPEG', 'FORMAT': 'PORTRAIT'}
    device.hardcopy = new_cfg
    print(f"hardcopy : {device.hardcopy}")
    device.store_hardcopy("C1.jpeg")
    # Preserving and Restoring Waveforms
    print("Set Trigger Single...")
    device.trigger_mode = Trigger.Modes.SINGLE
    # save C1 to M1
    print("Channel C1 save in M1...")
    device.save_memory(WaveForm.Channels.C1, WaveForm.Channels.M1)
    print("Show M1...")
    device.display_channel(Display.Channels.M1, "ON")
    device.close()


if __name__ == '__main__':
    sys.exit(main())
