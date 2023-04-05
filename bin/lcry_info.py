#!/usr/bin/env python3

from pylecroy.pylecroy import Lecroy

import sys

VERSION = '0.1.0'

USAGE = '''
Return information from Lecroy

Usage:
    python lcry_info.py -a "IP:10.67.16.22"
    python lcry_info.py -a "USBTMC:<Host Name>"
    python lcry_info.py -a "VXI11:10.67.0.211"
    python lcry_info.py -a "ALIAS NAME"
    ...
        
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
        opts, args = getopt.gnu_getopt(argv, 'hvla:', ['help', 'version', 'address='])
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
        sys.stderr.write("scope address must be provide...\n")
        print(USAGE)
        return 2

    scope = Lecroy(address)

    # Get scope parameters
    print(f"Scope identifier             : {scope.identifier}")
    print(f"Scope mode                   : {scope.mode}")
    print(f"Trigger mode                 : {scope.trigger_mode}")
    print(f"Trigger                      : {scope.trigger}")
    print(f"Auto calibration             : {scope.auto_calibration}")
    print(f"Display state                : {scope.display}")
    print(f"Grid mode                    : {scope.grid}")
    print(f"Sequence condition           : {scope.sequence}")
    print(f"Waveform Transfer            : {scope.waveform_transfer}")
    print(f"Hardcopy                     : {scope.hardcopy}")


if __name__ == '__main__':
    sys.exit(main())

