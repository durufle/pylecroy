"""
single example module
"""
import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
from pylecroy.pylecroy import Lecroy, Sequence, Trigger, Display, WaveForm


def main():
    """
    Main entry
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', help='device visa name or address.')
    args = parser.parse_args()

    array = [[]]
    scope = Lecroy(args.name)

    # Get scope identifier property
    print(f"scope identifier : {scope.identifier}")
    input("Set calibration signal to C1 and Press a key to continue...")

    print("Disable sequence Mode...")
    scope.set_sequence(Sequence.Modes.OFF, 10, 500000)

    print("Set trigger STOP...")
    scope.trigger_mode = Trigger.Modes.STOP

    print("Channels  OFF...")
    for channel in Display.Channels:
        scope.display_channel(channel, "OFF")

    print("Display Channel C1...")
    scope.display_channel("C1", "ON")

    print("Defined Waveform transfer mode...")
    scope.set_waveform_transfer(first_point=0, segment=0)
    print("Set trigger SINGLE...")
    scope.trigger_mode = Trigger.Modes.SINGLE
    print("Wait for acquisition...(timeout = 1s) ")
    scope.wait()

    trace = scope.get_wave(WaveForm.Modes.INTEGER, "C1", 5000000)
    if trace:
        array.insert(0, np.array(trace, dtype=np.int32))
        plt.plot(array[0])
        plt.title(f'Acquit {0}')
        plt.show()
    input("press a key to exit...")

    scope.close()


if __name__ == '__main__':
    sys.exit(main())
