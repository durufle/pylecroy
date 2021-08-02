#!/usr/bin/env python3

from pylecroy.pylecroy import Lecroy
import sys

VERSION = '0.1.0'

USAGE = '''
Return information from Lecroy

Usage:
    python lecroy_info.py -a 10.67.16.22

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
        print("scope IP address must be provide...")
        print(USAGE)
        return 2

    scope = Lecroy(address)

    # Get scope identifier identify
    scope.identify()
    print("scope identifier             : {} ".format(scope.identifier))
    scope.get_trigger_mode()
    print("get trigger mode             : {} ".format(scope.trigger_mode))
    print("get auto calibration         : {} ".format(scope.get_auto_calibration()))

    print("Channel C1 Parameters        : ", scope.get_parameter(scope.C1, "ALL"))
    scope.close()


if __name__ == '__main__':
    sys.exit(main())

