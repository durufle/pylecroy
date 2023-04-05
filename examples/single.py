#!/usr/bin/env python3

from pylecroy.pylecroy import Lecroy, Sequence, Trigger, WaveForm
import numpy as np
import matplotlib.pyplot as plt

import sys

USAGE = '''single: no sequence acquisition mode example
Usage:
    python single.py -a "IP:10.67.16.22"
    python single.py -a VXI11:10.67.0.211
    
Options:
    -h, --help              this help message.
    -a, --address           device IP address
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
        print("scope IP address must be provide...")
        print(USAGE)
        return 2

    array = [[]]

    scope = Lecroy(address)

    # Get scope identifier property
    print("scope identifier : {} ".format(scope.identifier))
    input("Set calibration signal to C1 and Press a key to continue...")

    print("Disable sequence Mode...")
    scope.set_sequence(Sequence.Modes.OFF, 10, 500000)

    print("Set trigger STOP...")
    scope.trigger_mode = Trigger.Modes.STOP

    print("Channels  OFF...")
    for channel in WaveForm.Channels:
        scope.display_channel(channel.value, "OFF")

    for memory in WaveForm.Memories:
        scope.display_channel(memory.value, "OFF")

    print("ShowChannels C1...")
    scope.display_channel("C1", "ON")

    print("Defined Waveform transfer mode...")
    scope.set_waveform_transfer(first_point=0, segment=0)
    print("Set trigger SINGLE...")
    scope.trigger_mode = Trigger.Modes.SINGLE
    print("Wait for acquisition...")
    scope.wait()

    trace = scope.get_wave(WaveForm.Modes.INTEGER, "C1", 5000000)
    if trace:
        array.insert(0, np.array(trace, dtype=np.int32))
        plt.plot(array[0])
        plt.title('Acquit {0}'.format(0))
        plt.show()
    input("press a key to exit...")

    scope.close()


if __name__ == '__main__':
    sys.exit(main())

