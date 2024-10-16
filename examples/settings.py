#!/usr/bin/env python3

from pylecroy.pylecroy import Lecroy, Grid, Trigger, Calibration, Display
import sys
import time

USAGE = '''settings: parameters settings usage
Usage:
    python settings.py -a "IP:10.67.16.22"
    python settings.py -a VXI11:10.67.0.211
    
Options:
    -h, --help              this help message.
    -a, --address           device address
'''


def main(argv=None):
    import getopt

    if argv is None:
        argv = sys.argv[1:]
    try:
        opts, args = getopt.gnu_getopt(argv, 'ha:', ['help', 'address='])
        address = None

        for o, a in opts:
            if o in ('-h', '--help'):
                print(USAGE)
                return 0
            elif o in ('-a', '--address'):
                address = a

    except getopt.GetoptError:
        e = sys.exc_info()[1]  # current exception
        sys.stderr.write(str(e) + "\n")
        sys.stderr.write(USAGE + "\n")
        return 1

    # Load default value
    if address is None:
        sys.stderr.write("scope address must be provide...\n")
        print(USAGE)
        return 2

    scope = Lecroy(address)

    # Get scope parameters
    print(f"Identifier               : {scope.identifier}")

    # Trigger setting
    print(f"Trigger mode             : {scope.trigger_mode}")
    for mode in Trigger.Modes:
        scope.trigger_mode = mode
        print(f"Trigger mode             : {scope.trigger_mode}")
    scope.trigger_mode = Trigger.Modes.STOP

    for mode in ['NORM', 'AUTO', 'SINGLE']:
        scope.trigger_mode = mode
        print(f"Trigger mode             : {scope.trigger_mode}")
    scope.trigger_mode = "STOP"
    print(f"Trigger mode             : {scope.trigger_mode}")

    # Auto calibration
    scope.auto_calibration = Calibration.States.OFF
    print(f"Auto calibration         : {scope.auto_calibration}")
    scope.auto_calibration = Calibration.States.ON
    print(f"Auto calibration         : {scope.auto_calibration}")
    scope.auto_calibration = 'OFF'
    print(f"Auto calibration         : {scope.auto_calibration}")
    scope.auto_calibration = 'ON'
    print(f"Auto calibration         : {scope.auto_calibration}")
    scope.auto_calibration = 'OFF'
    print(f"Auto calibration         : {scope.auto_calibration}")
    # Grid
    print(f"Grid                     : {scope.grid}")
    for state in Grid.States:
        scope.grid = state
        print(f"Grid                     : {scope.grid}")
        time.sleep(0.5)
    scope.grid = Grid.States.SINGLE

    for state in ['SINGLE', 'QUAD']:
        scope.grid = state
        print(f"Grid                     : {scope.grid}")
        time.sleep(0.5)
    scope.grid = Grid.States.SINGLE

    # Display
    print(f"Display                    {scope.display}")
    for state in Display.States:
        scope.display = state
        print(f"Display                    {scope.display}")

    # Display channel
    for channel in Display.Channels:
        scope.display_channel(channel, Display.States.OFF)

    for channel in Display.Channels:
        scope.display_channel(channel, Display.States.ON)

    for channel in ["C1", "C2", "C3", "C4", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "M1", "M2", "M3", "M4"]:
        scope.display_channel(channel, Display.States.OFF)

    for channel in ["C1", "C2", "C3", "C4", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "M1", "M2", "M3", "M4"]:
        scope.display_channel(channel, Display.States.ON)

    for channel in Display.Channels:
        scope.display_channel(channel, 'OFF')

    for channel in ["C1", "C2", "C3", "C4", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "M1", "M2", "M3", "M4"]:
        scope.display_channel(channel, 'ON')

    for channel in ["C1", "C2", "C3", "C4", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "M1", "M2", "M3", "M4"]:
        scope.display_channel(channel, 'OFF')

    scope.close()


if __name__ == '__main__':
    sys.exit(main())

