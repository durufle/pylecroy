from pylecroy import PyLecroy
import sys
import logging

VERSION = '1.0'

USAGE = '''pylecroy_tst_02: execute the lecroy test 02
Usage:
    python pylecroy_tst_02.py [options]

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

    # Test identify
    scope.identify()
    print("scope identifier   : " + scope.identifier)

    # print all C1 parameters
    print("Channel C1 Parameters : ", scope.get_parameter(scope.C1, "ALL"))

    # grid state
    for state in scope.GRID_STATE:
        print("Grid state : " + state)
        scope.show_grid(state)
        input("Press a key to continue...")
    # single grid
    scope.show_grid(scope.SINGLE)

    # Set  C1 to C4 to off
    print("Channels  OFF...")
    for channel in scope.WAVEFORM_CHANNELS:
        scope.show_trace(channel, "OFF")
    print("Memory  OFF...")
    for channel in scope.INTERNAL_MEMORY:
        scope.show_trace(channel, "OFF")

    input("Press a key to continue...")
    print("Channel C1 ON...")
    scope.show_trace(scope.C1, "ON")

    input("Get a signal on C1 and press a key to continue...")
    # save C1 to M1
    print("Channel C1 save in M1...")
    scope.save_memory(scope.C1, scope.M1)
    print("Channel C1 OFF...")
    scope.show_trace(scope.C1, "OFF")
    print("Show M1...")
    scope.show_trace(scope.M1, "ON")

    scope.close()


if __name__ == '__main__':
    sys.exit(main())
