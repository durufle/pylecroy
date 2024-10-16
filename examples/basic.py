#!/usr/bin/env python3

from pylecroy.pylecroy import Lecroy
import sys

USAGE = '''basic: basic usage
Usage:
    python basic.py -a "IP:10.67.16.22"
    python basic.py -a VXI11:10.67.0.211
    
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
    print(f"Scope identifier             : {scope.identifier}")
    print(f"Trigger mode                 : {scope.trigger_mode}")
    print(f"Auto calibration             : {scope.auto_calibration}")
    print(f"Display state                : {scope.display}")
    print(f"Grid mode                    : {scope.grid}")
    print(f"Sequence condition           : {scope.sequence}")
    print(f"Waveform Transfer            : {scope.waveform_transfer}")
    print(f"Hardcopy                     : {scope.hardcopy}")
    scope.close()


if __name__ == '__main__':
    sys.exit(main())

