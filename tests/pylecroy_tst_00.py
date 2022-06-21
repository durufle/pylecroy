#!/usr/bin/env python3

from pylecroy.pylecroy import *
import sys

VERSION = '1.0'

USAGE = '''pylecroy_tst_00: execute the lecroy test 00
Usage:
    python pylecroy_tst_00.py [options]

Options:
    -h, --help              this help message.
    -v, --version           version info.
    -a, --address           device IP address
'''


def main(argv=None):
    import getopt

    if argv is None:
        argv = sys.argv[1:]
    try:
        opts, args = getopt.gnu_getopt(argv, 'hva:', ['help', 'version', 'address='])
        address = None

        for o, a in opts:
            if o in ('-h', '--help'):
                print(USAGE)
                return 0
            if o in ('-v', '--version'):
                print(VERSION)
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
        sys.stderr.write("scope address is mandatory..."+ "\n")
        sys.stderr.write(USAGE + "\n")

    scope = Lecroy(address)

    # Get scope identifier property
    print("scope identifier : {} ".format(scope.identifier))

    # Test trigger mode
    scope.trigger_mode = TriggerModes.NORM
    print("scope trigger mode : " + scope.trigger_mode)
    scope.set_hardcopy(Hardcopy.BMP, "D:\\TEST_PYLECROY", "TEST_PYLECROY.bmp")
    print(scope.get_hardcopy_all())
    # scope.print_screen()

    # waveform is a byte array
    # waveform = (scope.get_wave(scope.NATIVE, scope.C1, 10000, 0))

    # print all C1..C4 parameters
    print("Channel C1 Parameters : ", scope.get_parameter(Channels.C1, "ALL"))
    print("Channel C2 Parameters : ", scope.get_parameter(Channels.C2, "ALL"))
    print("Channel C3 Parameters : ", scope.get_parameter(Channels.C3, "ALL"))
    print("Channel C4 Parameters : ", scope.get_parameter(Channels.C4, "ALL"))

    # Test panel functions
    panel = scope.panel
    scope.panel = panel

    input("Press a key to continue...")
    scope.grid= TriggerModes.SINGLE
    print("ALL Waveform OFF...")
    for trace in Channels.NAMES:
        scope.display_channel(trace, scope.OFF)
    input("Set calibration signal to C2 and Press a key to continue...")
    # Visualize C2
    scope.display_channel(Channels.C2, scope.ON)

    scope.close()


if __name__ == '__main__':
    sys.exit(main())
