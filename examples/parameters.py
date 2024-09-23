"""
parameters example module
"""
import sys
import argparse
from pylecroy.pylecroy import Lecroy, Parameters


def main():
    """
    Main entry
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', help='device visa name or address.')
    args = parser.parse_args()

    scope = Lecroy(args.name)
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
