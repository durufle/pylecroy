from pylecroy.pylecroy import *
import sys
import time

VERSION = '1.0'

USAGE = '''pylecroy_tst_01: execute the lecroy test 01
Usage:
    python pylecroy_tst_01.py [options]

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
        opts, args = getopt.gnu_getopt(argv, 'hva:', ['help', 'version',  'address='])
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

    for trigger in TriggerModes.MODES:
        scope.trigger_mode = trigger
        print("scope trigger mode : " + scope.trigger_mode)
        time.sleep(1)

    try:
        scope.trigger_mode = "NONE"
    except ValueError as msg:
        print(msg)

    scope.close()


if __name__ == '__main__':
    sys.exit(main())
