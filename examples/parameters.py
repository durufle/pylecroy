#!/usr/bin/env python3

from pylecroy.pylecroy import Lecroy, Parameters
import sys

USAGE = '''settings: parameters settings usage
Usage:
    python parameters.py -a "IP:10.67.16.22"
    python parameters.py -a VXI11:10.67.0.211
    
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
    print(f"Identifier               : {scope.identifier}")

    # get all parameters
    print("--> ALL Parameters")
    print("     --> By enum")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,Parameters.Param.ALL)}")
    print("     --> By string")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,'ALL')}")
    print("-->")

    # get  AMPL parameters
    print("--> AMPL Parameter")
    print("     --> By enum")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,Parameters.Param.AMPL)}")
    print("     --> By string")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,'AMPL')}")
    print("-->")

    # get  DLY parameters
    print("--> DLY Parameter")
    print("     --> By enum")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,Parameters.Param.DELAY)}")
    print("     --> By string")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,'DLY')}")
    print("-->")

    # get  RISE parameters
    print("--> RISE Parameter")
    print("     --> By enum")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,Parameters.Param.RISE)}")
    print("     --> By string")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,'RISE')}")
    print("-->")

    # get  FALL parameters
    print("--> FALL Parameter")
    print("     --> By enum")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,Parameters.Param.FALL)}")
    print("     --> By string")
    for channel in Parameters.Channels:
        print(f"{channel} : {scope.get_parameter(channel,'FALL')}")
    print("-->")

    scope.close()


if __name__ == '__main__':
    sys.exit(main())

