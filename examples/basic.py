"""
Basic example module
"""
import sys
import argparse
from pylecroy.pylecroy import Lecroy

ADDRESS_USB = "USBTMC:USB0::0x05ff::0x1023::4609N02794::INSTR"
ADDRESS_TCP = "IP:10.64.61.56"
ADDRESS_VXI11 = "VXI11:10.64.61.56"
ADDRESS = ADDRESS_USB


def main():
    """
    Main entry
    """
    parser = argparse.ArgumentParser(description='Get information from Lecroy scope')
    parser.add_argument('-n', '--name', default=ADDRESS, help='device visa name or address.')
    args = parser.parse_args()

    scope = Lecroy(args.name)

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
