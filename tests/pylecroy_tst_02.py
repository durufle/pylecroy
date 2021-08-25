from pylecroy.pylecroy import *
import sys
import time

VERSION = '1.0'

USAGE = '''pylecroy_tst_02: execute the lecroy test 02
Usage:
    python pylecroy_tst_02.py [options]

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
    # Stop Trigger
    scope.trigger_mode = TriggerModes.STOP

    input("Get a signal on C1 and press a key to continue...")

    # grid state
    for state in GridStates.STATES:
        print("Grid state : " + state)
        scope.grid = state
        time.sleep(1)

    # Dual grid
    scope.grid = GridStates.DUAL

    # Set  C1 to C4 to off
    print("Channels  OFF...")
    for channel in Channels.NAMES:
        scope.display_channel(channel, "OFF")
    print("Memory  OFF...")
    for Memory in Memories.NAMES:
        scope.display_channel(Memory, "OFF")

    print("Channel C1 ON...")
    scope.display_channel(Channels.C1, "ON")

    print("Set Trigger Single...")
    scope.trigger_mode = TriggerModes.SINGLE

    # save C1 to M1
    print("Channel C1 save in M1...")
    scope.save_memory(Channels.C1, Memories.M1)
    print("Show M1...")
    scope.display_channel(Memories.M1, "ON")

    scope.close()


if __name__ == '__main__':
    sys.exit(main())
