from pylecroy import PyLecroy
import sys
import logging

VERSION = '1.0'

USAGE = '''pylecroy_tst_01: execute the lecroy test 01
Usage:
    python pylecroy_tst_01.py [options]

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

    scope = PyLecroy(address)
    # Get identify
    scope.identify()
    print("scope identifier   : " + scope.identifier)

    # Test trigger mode
    scope.set_trigger_mode(scope.AUTO)
    scope.get_trigger_mode()
    print("scope trigger mode : " + scope.trigger_mode)
    scope.set_trigger_mode(scope.NORM)
    scope.get_trigger_mode()
    print("scope trigger mode : " + scope.trigger_mode)
    scope.set_trigger_mode(scope.SINGLE)
    scope.get_trigger_mode()
    print("scope trigger mode : " + scope.trigger_mode)
    scope.set_trigger_mode(scope.STOP)
    scope.get_trigger_mode()
    print("scope trigger mode : " + scope.trigger_mode)

    try:
        scope.set_trigger_mode("NONE")
    except ValueError as msg:
        print(msg)

    scope.close()


if __name__ == '__main__':
    sys.exit(main())
