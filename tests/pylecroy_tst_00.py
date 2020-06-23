#!/usr/bin/env python3

from pylecroy import PyLecroy
import logging
import sys
import intelhex

VERSION = '1.0'

USAGE = '''pylecroy_tst_00: execute the lecroy test 00
Usage:
    python pylecroy_tst_00.py [options]

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

    # Test trigger mode
    scope.set_trigger_mode(scope.NORM)
    scope.get_trigger_mode()
    print("scope trigger mode : " + scope.trigger_mode)
    scope.set_hardcopy(scope.BMP, "D:\\TEST_PYLECROY", "TEST_PYLECROY.bmp")
    print(scope.get_hardcopy_full_setup())
    # scope.print_screen()

    # waveform is a byte array
    # waveform = (scope.get_wave(scope.NATIVE, scope.C1, 10000, 0))

    # print all C1..C4 parameters
    print("Channel C1 Parameters : ", scope.get_parameter(scope.C1, "ALL"))
    print("Channel C2 Parameters : ", scope.get_parameter(scope.C2, "ALL"))
    print("Channel C3 Parameters : ", scope.get_parameter(scope.C3, "ALL"))
    print("Channel C4 Parameters : ", scope.get_parameter(scope.C4, "ALL"))

    # Test panel functions
    panel_a = scope.get_panel()
    scope.set_panel(panel_a)
    input("Press a key to continue...")
    scope.show_grid(scope.SINGLE)
    print("ALL Waveform OFF...")
    for trace in scope.TRACE_CHANNELS:
        scope.show_trace(trace, scope.OFF)
    input("Set calibration signal to C1 and Press a key to continue...")
    # Visualize C1
    scope.show_trace(scope.C1, scope.ON)
    scope.show_trace(scope.Z1, scope.ON)
    input("Select Z1 area and Press a key to continue...")
    # save Z1 to M1
    scope.save_memory(scope.Z1, scope.M1)
    # scope.get_wave_to_file("./test_full.bin", scope.BYTE, scope.C1, 2000000)
    # scope.display_wave("./test_full.bin")
    # scope.get_wave_to_file("./test_partial.bin", scope.BYTE, scope.C1, 2000000, 1000000)
    # scope.get_wave_to_file("./test_full_z1.bin", scope.BYTE, scope.Z1, 1000000, 500000)
    # scope.display_wave("./test_full_z1.bin")
    # intelhex.bin2hex("./test_full.bin", "./test_full.hex", 0)
    # scope.close()


if __name__ == '__main__':
    sys.exit(main())
