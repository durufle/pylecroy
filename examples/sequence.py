#!/usr/bin/env python3

from pylecroy.pylecroy import *
import numpy as np
import matplotlib.pyplot as plt
import sys

VERSION = '0.1.0'

USAGE = '''sequence: sequence acquisition mode example
Usage:
    python sequence.py -a "IP:10.67.16.22"

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

    # Get scope identifier property
    print("scope identifier : {} ".format(scope.identifier))
    print("Set trigger STOP...")
    scope.trigger_mode = Trigger.Modes.STOP

    print("Enable sequence Mode...")
    scope.set_sequence(Sequence.Modes.ON, 10, 500000)
    print("Get sequence setup...")
    seq_setup = scope.sequence
    print(seq_setup)

    print("Channels  OFF...")
    for channel in WaveForm.Channels:
        scope.display_channel(channel.value, "OFF")

    for memory in WaveForm.Memories:
        scope.display_channel(memory.value, "OFF")

    input("Set calibration signal to C1 and Press a key to continue...")

    print("ShowChannels C1...")
    scope.display_channel("C1", "ON")

    number = 1
    print("Defined Waveform transfer mode... segment = {0}".format(number))
    scope.set_waveform_transfer(first_point=0, segment=number)
    print("Get Waveform setup...")
    wave_setup = scope.waveform_transfer
    print(wave_setup)

    print("Disable auto calibration...")
    scope.auto_calibration = Calibration.States.OFF

    array = [[]]

    print("Set trigger SINGLE...")
    scope.trigger_mode = Trigger.Modes.SINGLE
    print("Wait for acquisition...")
    scope.wait(timeout=10)

    for acquit in range(0, 1):
        trace = scope.get_wave(WaveForm.Modes.INTEGER, "C1", 500000)
        array.insert(acquit, np.array(trace, dtype=np.int32))
        plt.plot(array[acquit])
        plt.title('Acquisition {0}'.format(acquit))
        plt.show()

    input("press a key to exit...")
    print("Disable sequence Mode...")
    scope.set_sequence(Sequence.Modes.OFF, 10, 500000)

    scope.close()


if __name__ == '__main__':
    sys.exit(main())

