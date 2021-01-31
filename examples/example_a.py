#!/usr/bin/env python3

from scope.pylecroy import Lecroy
import logging
import sys

SCOPE_LASER = "10.67.16.21"
SCOPE_SCA = "10.67.16.22"
ADDRESS = SCOPE_LASER

VERSION = '1.0'

USAGE = '''example_a: execute the lecroy class example a
Usage:
    python example_a.py -a 10.67.16.22

Options:
    -h, --help              this help message.
    -v, --version           version info.
    -l, --logging           enable logging
    -a, --address           device IP address
'''


def main(argv=None):
    import getopt

    if argv is None:
        argv = sys.argv[1:]
    try:
        opts, args = getopt.gnu_getopt(argv, 'hvla:', ['help', 'version', 'logging', 'address='])
        address = None
        log = False

        for o, a in opts:
            if o in ('-h', '--help'):
                print(USAGE)
                return 0
            if o in ('-v', '--version'):
                print(VERSION)
                return 0
            elif o in ('-l', '--logging'):
                log = True
            elif o in ('-a', '--address'):
                address = a

    except getopt.GetoptError:
        e = sys.exc_info()[1]  # current exception
        sys.stderr.write(str(e) + "\n")
        sys.stderr.write(USAGE + "\n")
        return 1

    # Load default value
    if address is None:
        print("scope IP address must be provide...")
        print(USAGE)
        return 2

    if log is True:
        logging.basicConfig(level=logging.INFO)

    scope = PyLecroy(address)

    # Get scope identifier identify
    scope.identify()
    print("scope identifier : {} ".format(scope.identifier))

    print("Set trigger AUTO...")
    scope.set_trigger_mode(scope.AUTO)

    print("Channels  OFF...")
    for channel in scope.WAVEFORM_CHANNELS:
        scope.show_trace(channel, "OFF")

    for channel in scope.INTERNAL_MEMORY:
        scope.show_trace(channel, "OFF")

    print("ShowChannels C1 and Z1 ...")
    scope.show_trace(scope.C1, "ON")
    scope.show_trace(scope.Z1, "ON")

    input("Set calibration signal to C1 and Press a key to continue...")
    input("Select Zoom area on Z1 and Press a key to continue...")

    scope.get_wave_to_file("./zoom_area.bin", scope.BYTE, scope.Z1, 500000)
    scope.display_wave("./zoom_area.bin")
    input("press a key to exit...")

    scope.close()


if __name__ == '__main__':
    sys.exit(main())

