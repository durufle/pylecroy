#!/usr/bin/env python3
import time

from pylecroy.pylecroy import *
import numpy as np
import matplotlib.pyplot as plt
import sys

VERSION = '0.1.0'

USAGE = '''basic: parameters settings usage
Usage:
    python basic.py -a "IP:10.67.16.22"

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
        sys.stderr.write("scope address must be provide...\n")
        print(USAGE)
        return 2

    scope = Lecroy(address)

    # Get scope parameters
    print(f"Identifier               : {scope.identifier}")

    # Trigger setting
    trigger = scope.trigger_mode
    print(f"Trigger mode             : {trigger}")
    for mode in Trigger.Modes:
        scope.trigger_mode = mode.value
        print(f"Trigger mode             : {scope.trigger_mode}")

    # Auto calibration
    cal = scope.auto_calibration
    print(f"Auto calibration         : {cal}")
    scope.auto_calibration = Calibration.States.OFF
    print(f"Auto calibration         : {scope.auto_calibration}")
    scope.auto_calibration = Calibration.States.ON
    print(f"Auto calibration         : {scope.auto_calibration}")

    # Grid

    scope.close()


if __name__ == '__main__':
    sys.exit(main())

