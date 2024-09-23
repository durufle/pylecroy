"""
parameters example module
"""
import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
from pylecroy.pylecroy import Lecroy, Trigger, Sequence, Calibration, WaveForm, Display


def main():
    """
    Main entry
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', help='device visa name or address.')
    args = parser.parse_args()

    scope = Lecroy(args.name)

    print(f"scope identifier : {scope.identifier}")
    print("Set trigger STOP...")
    scope.trigger_mode = Trigger.Modes.STOP

    print("Enable sequence Mode...")
    scope.set_sequence(Sequence.Modes.ON, 10, 5000000)
    print("Get sequence setup...")
    seq_setup = scope.sequence
    print(seq_setup)

    print("Channels  OFF...")
    for channel in Display.Channels:
        scope.display_channel(channel, "OFF")

    input("Set calibration signal to C1 and Press a key to continue...")

    print("Show Channel C1...")
    scope.display_channel("C1", "ON")

    number = 1
    print(f"Defined Waveform transfer mode... segment = {number}")
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
    scope.wait()

    for acquit in range(0, 1):
        trace = scope.get_wave(WaveForm.Modes.INTEGER, "C1", 5000000)
        array.insert(acquit, np.array(trace, dtype=np.int32))
        plt.plot(array[acquit])
        plt.title(f'Acquisition {acquit}')
        plt.show()

    input("press a key to exit...")
    print("Disable sequence Mode...")
    scope.set_sequence(Sequence.Modes.OFF, 10, 5000000)

    scope.close()


if __name__ == '__main__':
    sys.exit(main())
