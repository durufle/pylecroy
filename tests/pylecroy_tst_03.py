#!/usr/bin/env python3

from pylecroy.pylecroy import Lecroy
import logging
import sys

VERSION = '1.0'

USAGE = '''pylecroy_tst_03: execute the lecroy test 03
Usage:
    python pylecroy_tst_03.py [options]

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
        sys.stderr.write("scope address is mandatory..."+ "\n")
        sys.stderr.write(USAGE + "\n")

    if log is True:
        logging.basicConfig(level=logging.INFO)

    scope = Lecroy(address)

    # Get identify
    scope.identify()
    print("scope identifier   : " + scope.identifier)

    # Get current hardcopy setup
    print(scope.get_hardcopy_full_setup())
    # get current hardcopy directory
    print("Hardcopy directory : " + scope.get_hardcopy(9))

    # Test trigger mode
    scope.set_trigger_mode(scope.AUTO)

    # Set new hardcopy environment (dir, file)
    scope.set_hardcopy(scope.BMP, "D:\\TEST_PYLECROY", "TEST")
    print("Hardcopy directory : " + scope.get_hardcopy(9))

    input("Display signal on channel C1 and press a key to continue...")
    scope.display_channel(scope.C1, "ON")
    # Perform a print screen
    scope.print_screen()
    input("Check print screen file in scope and press a key to continue...")

    scope.close()


if __name__ == '__main__':
    sys.exit(main())

