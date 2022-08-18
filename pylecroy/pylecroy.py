#!/usr/bin/python3

import sys
import logging
import win32com.client


class CustomException(Exception):
    """Exception raised when very uncommon things happen"""
    pass


class MetaConst(type):
    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        raise TypeError


class Const(object, metaclass=MetaConst):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError


class RemoteModes(Const):
    LOCAL = 0
    REMOTE = 1
    MODES = (LOCAL, REMOTE)


class TriggerModes(Const):
    AUTO = 'AUTO'
    NORMAL = 'NORM'
    SINGLE = "SINGLE"
    STOP = "STOP"
    MODES = (AUTO, NORMAL, SINGLE, STOP)


class GridStates(Const):
    AUTO = 'AUTO'
    SINGLE = 'SINGLE'
    DUAL = 'DUAL'
    QUAD = 'QUAD'
    OCTAL = 'OCTAL'
    XY = 'XY'
    XYSINGLE = 'XYSINGLE'
    XYDUAL = 'XYDUAL'
    TANDEM = 'TANDEM'
    QUATTRO = 'QUATTRO'
    TWELVE = 'TWELVE'
    STATES = (AUTO, SINGLE, DUAL, QUAD, OCTAL, XY, XYSINGLE, XYDUAL, TANDEM, QUATTRO, TWELVE)


class Channels(Const):
    C1 = 'C1'
    C2 = 'C2'
    C3 = 'C3'
    C4 = 'C4'
    Z1 = "Z1"
    Z2 = "Z2"
    Z3 = "Z3"
    Z4 = "Z4"
    Z5 = "Z5"
    Z6 = "Z6"
    Z7 = "Z7"
    Z8 = "Z8"
    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F5 = "F5"
    F6 = "F6"
    F7 = "F7"
    F8 = "F8"
    NAMES = (C1, C2, C3, C4, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, F1, F2, F3, F4, F5, F6, F7, F8)


class Parameters(Const):
    # Parameters related constants
    ALL = 'ALL'
    AMPL = 'AMPL'
    DELAY = 'DLY'

    RISE = 'RISE'
    FALL = 'FALL'
    MEAN = 'MEAN'
    PKPK = 'PKPK'
    NAMES = (ALL, AMPL, DELAY, RISE, FALL, MEAN, PKPK)


class Memories(Const):
    M1 = 'M1'
    M2 = 'M2'
    M3 = 'M3'
    M4 = 'M4'
    NAMES = (M1, M2, M3, M4)


class Display(Const):
    ON = "ON"
    OFF = "OFF"
    STATES = (ON, OFF)


class Setups(Const):
    S1 = 0
    S2 = 1
    S3 = 2
    S4 = 3
    S5 = 4
    S6 = 5
    SLOTS = (S1, S2, S3, S4, S5, S6)


class WaveForms(Const):
    BYTE = 0
    INTEGER = 1
    SCALED = 2
    NATIVE = 3
    MODES = (BYTE, INTEGER, SCALED, NATIVE)


class Hardcopy(Const):
    # Devices constant
    BMP = 'BMP'
    JPEG = 'JPEG'
    PNG = 'PNG'
    TIFF = 'TIFF'
    DEVICE = (BMP, JPEG, PNG, TIFF)
    # Index
    IDX_FOLDER = 9
    IDX_FILE = 11


class Calibration(Const):
    ON = 'ON'
    OFF = 'OFF'
    STATES = (ON, OFF)


class Sequence(Const):
    ON = 'ON'
    OFF = 'OFF'
    MODES = (ON, OFF)


class Lecroy:
    """
    Class to drive a Lecroy oscilloscope using ActiveDSO active X
    """
    def __init__(self, address=None):
        self._is_open = False
        self._instance = None
        self._mode = None
        self._timeout = None
        self._logger = logging.getLogger(__name__)
        self.open(address)

    def __del__(self):
        if self._is_open:
            self.close()

    # ----------------------------------------------------------------------- #
    def open(self, address):
        """
        Create a connection with the device and setup in remote mode

        :param address: IP Address
        :return:
        """
        self._instance = win32com.client.Dispatch("LeCroy.ActiveDSOCtrl.1")
        """ Create Connection with device """

        if self._instance.MakeConnection(address):
            self._is_open = True
            self.timeout = 1
            self.mode = RemoteModes.REMOTE
            self.beep()
        else:
            sys.exit("Connection with scope failed...")

    def close(self):
        """
        Close communication with the device. Switch the device in local
        mode before closing.

        """
        self.mode = RemoteModes.LOCAL
        if self._instance.Disconnect():
            self._is_open = False

    # ----------------------------------------------------------------------- #
    @property
    def mode(self):
        """
        Get the current scope mode.

        :return: device mode.
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Set the scope mode (remote or local)

        :param mode:
        :return:
        """
        if mode not in RemoteModes.MODES:
            raise ValueError("Not a valid mode...")

        if self._is_open:
            if self._instance.SetRemoteLocal(mode):
                self._mode = mode

    # ----------------------------------------------------------------------- #
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        """
        This method sets the time that the control will wait for a response from the instrument.
        The methods to which this applies are:
            ReadString, ReadBinary, WaitForOPC, GetByteWaveform, GetIntegerWaveform GetNativeWaveform,
            GetScaledWaveform, GetScaledWaveformWithTimes

        :param value: Single, Time-out time in seconds
        """
        if self._instance.SetTimeout(value):
            self._timeout = value

    # ----------------------------------------------------------------------- #
    # HARDCOPY - Printing the Display/Screen Capture
    # ----------------------------------------------------------------------- #
    @property
    def hardcopy(self) -> dict:
        """
        Hardcopy setup

        :return: return the complete of hardware setup as a dict.
        """
        if self._instance.WriteString("HCSU?", True):
            result = self._instance.ReadString(5000).split(',')
            return dict(zip(result[::2], result[1::2]))

    @hardcopy.setter
    def hardcopy(self, config: dict):
        # convert dictionary into list
        new_list = zip(config.keys(), config.values())
        new_list = list(new_list)

        fields = []
        for i in new_list:
            item, value = i
            fields.append("{0},{1},".format(item, value))

        params = ''.join(fields)
        cmd = 'HCSU ' + params[:-1]
        self._instance.WriteString(cmd, True)
        while not self._instance.WaitForOPC():
            pass

    # ----------------------------------------------------------------------- #
    def store_hardcopy(self, name, form='BMP'):
        """
        Store an hardcopy file from scope to PC.

        :param name: file name
        :param form: Hardcopy format
        :return: None
        """
        self._instance.StoreHardcopyToFile(form, "", name)

    # ----------------------------------------------------------------------- #

    def screen_dump(self):
        """
        Perform a screen dump. See set_hardcopy method

        :return:
        """
        self._instance.WriteString("SCDP", True)

    # ----------------------------------------------------------------------- #
    # ACQUISITION - Controlling Waveform Captures
    # ----------------------------------------------------------------------- #

    def set_waveform_transfer(self, first_point=0, segment=0):
        """
        configures parameters controlling the waveform transfer

        :param  first_point: Integer, The index of the first point to transfer (0 = first point).
        :param  segment: Integer, Segment number to transfer (0 = all segments).

        :notes:
            This method affects how the various GetWaveform functions transfer a waveform. For the majority of cases the
            default settings will be sufficient. These are Start Transfer at first point, Transfer all data points Transfer all segments.
        """
        self._instance.SetupWaveformTransfer(first_point, 0, segment)

    # ----------------------------------------------------------------------- #
    @property
    def waveform_transfer(self):
        """
        Get Waveform setup information

        :return: A dictionary
        :rtype: dict

        """
        if self._instance.WriteString("WFSU?", True):
            value = self._instance.ReadString(50)
            self._logger.debug(value)
            setup = {}
            (setup["Sparsing"]) = self._instance.GetCommaDelimitedString(value, 1)
            (setup["Number"]) = self._instance.GetCommaDelimitedString(value, 3)
            (setup["First"]) = self._instance.GetCommaDelimitedString(value, 5)
            (setup["Segment"]) = self._instance.GetCommaDelimitedString(value, 7)
            return setup
    # ----------------------------------------------------------------------- #

    def get_wave(self, mode, name, max_bytes):
        """
        Get a wave from scope, and return it

        :param mode: mode (BYTE, INTEGER, SCALED, NATIVE)
        :param name: channel name
        :param max_bytes: maximum byte
        :return: list of waveform values

        :notes: For NATIVE WaveForm, 12-bit oscilloscopes must use the 16-bit word format. Set maxBytes value as <number of bytes to read> x 2.

        """
        wave = None
        if mode not in WaveForms.MODES:
            raise ValueError("Not a valid get waveform mode...")
        if name not in Channels.NAMES:
            raise ValueError("Not a valid channel...")
        if mode not in WaveForms.MODES:
            raise ValueError("Not a valid transfer mode...")

        if mode == WaveForms.BYTE:
            wave = list(self._instance.GetByteWaveform(name, max_bytes, 0))
        elif mode == WaveForms.INTEGER:
            wave = self._instance.GetIntegerWaveform(name, max_bytes, 0)
        elif mode == WaveForms.SCALED:
            wave = self._instance.GetScaledWaveform(name, max_bytes, 0)
        elif mode == WaveForms.NATIVE:
            wave = self._instance.GetNativeWaveform(name, max_bytes, False, 'ALL')
        return wave

    # ----------------------------------------------------------------------- #

    @property
    def trigger_mode(self):
        """
        Return current trigger mode

        :return: trigger mode
        """
        if self._instance.WriteString("TRMD?", True):
            return self._instance.ReadString(80)

    @trigger_mode.setter
    def trigger_mode(self, mode):
        """
        Set trigger mode

        :param mode: trigger mode
        """
        if mode not in TriggerModes.MODES:
            raise ValueError("Not a Valid mode...")
        self._instance.WriteString("TRMD " + mode, True)
        while not self._instance.WaitForOPC():
            pass

    def trigger_arm(self):
        """
        Arm the scope for single mode
        """
        self.trigger_mode = TriggerModes.SINGLE

    def wait(self, timeout=1):
        self._instance.WriteString("WAIT {0}".format(timeout), True)
        while not self._instance.WaitForOPC():
            pass

    @property
    def sequence(self):
        """
        Return Conditions for the sequence acquisition

        :return: Return sequence activation flag, number sequences and memory length
        :rtype: String
        """
        if self._instance.WriteString("SEQUENCE?", True):
            value = self._instance.ReadString(10)
            setup = {}
            (setup["Mode"]) = self._instance.GetCommaDelimitedString(value, 0)
            (setup["Segments"]) = self._instance.GetCommaDelimitedString(value, 1)
            (setup["Size"]) = self._instance.GetCommaDelimitedString(value, 2)
            return setup

    def set_sequence(self, mode, segment, size):
        """
        Set conditions for the sequence acquisition.

        :param mode: ON or OFF
        :param segment: number segment
        :param size: memory length

        :note:

        The size value can be expressed either as numeric fixed point, exponential, or using standard suffixes
        """
        if mode not in Sequence.MODES:
            raise ValueError("Not a valid mode...")
        return self._instance.WriteString("SEQUENCE {0},{1},{2}".format(mode, segment, size), True)

    # ----------------------------------------------------------------------- #
    # CURSOR - Performing Measurements
    # ----------------------------------------------------------------------- #

    def get_parameter(self, name, parameter):
        """
        Return a channel parameters(s)

        :param name: Channel Name in Channels constant class
        :param parameter: Channel Parameter in Parameters class
        :return: Parameter value
        """
        if name not in Channels.NAMES:
            raise ValueError("Not a valid channel...")
        if parameter not in Parameters.NAMES:
            raise ValueError("Not a valid parameter...")
        cmd = "{0}:PAVA? {1}".format(name, parameter)
        if self._instance.WriteString(cmd, True):
            return self._instance.ReadString(1000)

    # ----------------------------------------------------------------------- #
    # SAVE/RECALL SETUP - Perserving and Restoring Panel Settings
    # ----------------------------------------------------------------------- #

    @property
    def panel(self):
        """
        The Panel property reads the instrument's control state into a String,
        allowing a future call to SetPanel to reproduce the state.
        """
        return self._instance.GetPanel()

    # ----------------------------------------------------------------------- #
    @panel.setter
    def panel(self, panel: str):
        """
        The Panel setter sets the instrument's control state using a panel
        string captured using the panel property.

        :param panel: panel string used

        """
        self._instance.SetPanel(panel)

    # ----------------------------------------------------------------------- #
    # WAVEFORM TRANSFER - Preserving and Restoring Waveforms
    # ----------------------------------------------------------------------- #
    def save_memory(self, channel, memory):
        """
        Save a trace in an internal memory slot

        :param channel: trace channel number
        :param memory: memory slot n umber
        :return: Write command status

        :exception: ValueError: Trace selected not supported...
        :exception: ValueError: Memory selected not supported...
        """
        if channel not in Channels.NAMES:
            raise ValueError("Trace selected not supported...")
        if memory not in Memories.NAMES:
            raise ValueError("Memory selected not supported...")
        cmd = "STO {0},{1}".format(channel, memory)
        return self._instance.WriteString(cmd, True)

    # ----------------------------------------------------------------------- #
    # SAVE/RECALL SETUP - Perserving and Restoring Panel Settings
    # ----------------------------------------------------------------------- #
    def recall_setup(self, setup):
        """
        Recall a setup stored in an internal setup slot

        :param: setup slot number
        :return: Write command status

        :exception: ValueError: Setup slot selected not supported..
        """
        if setup not in Setups.SLOTS:
            raise ValueError("Setup slot selected not supported...")
        cmd = "*RCL {0}".format(setup)
        return self._instance.WriteString(cmd, True)

    def save_setup(self, setup):
        """
        Save a setup stored in an internal setup slot

        :param: setup slot number
        :return: Write command status

        :exception: ValueError: Setup slot selected not supported..
        """
        if setup not in Setups.SLOTS:
            raise ValueError("Setup slot selected not supported...")
        cmd = "*SAV {0}".format(setup)
        return self._instance.WriteString(cmd, True)

    # ----------------------------------------------------------------------- #
    # Display Commands and Queries
    # ----------------------------------------------------------------------- #

    @property
    def display(self):
        """
        Get display mode
        :return: ON or OFF
        """
        if self._instance.WriteString("DISP?", True):
            return self._instance.ReadString(10)

    @display.setter
    def display(self, state):
        """
        Set display mode

        :param state: ON or OFF
        :exception: ValueError: display state value not supported

        :notes:
        When you set the display to OFF, the screen does not actually go blank. Instead, the real-time
        clock and the message field are continuously updated. but waveforms and associated text are frozen.
        """
        if state not in Display.STATES:
            raise ValueError("Display state not supported...")
        cmd = "DISP {0}".format(state)
        self._instance.WriteString(cmd, True)

    @property
    def grid(self):
        """
        return the style of grid used
        """
        if self._instance.WriteString("GRID?", True):
            return self._instance.ReadString(10)

    @grid.setter
    def grid(self, grid):
        """
        Change scope grid format

        :param grid: grid format
        :exception ValueError: Grid mode not supported
        """
        if grid not in GridStates.STATES:
            raise ValueError("Grid mode not supported...")
        cmd = "GRID {0}".format(grid)
        self._instance.WriteString(cmd, True)
        while not self._instance.WaitForOPC():
            pass

    def display_channel(self, name, state):
        """
        Display/ Doesn't display a channel to the scope screen.

        :param name: trace channel number
        :param state: ON / OFF
        :return: Write command status
        """
        if (name not in Channels.NAMES) and (name not in Memories.NAMES):
            raise ValueError("Channel name selected not supported...")
        if state not in Display.STATES:
            raise ValueError("state selected not supported...")
        cmd = "{0}:TRA {1}".format(name, state)
        self._instance.WriteString(cmd, True)
        while not self._instance.WaitForOPC():
            pass

    # ----------------------------------------------------------------------- #
    def clear(self, reboot):
        """
        Clear device with reboot option
        """
        if isinstance(reboot, bool):
            self._instance.DeviceClear(reboot)

    def beep(self):
        """
        Execute a beep
        :return: Write command status
        """
        return self._instance.WriteString("BUZZ BEEP", 1)

    def calibrate(self):
        """
        Execute a calibration.
        """
        if self._instance.WriteString("*CAL?", True):
            # Waiting scope available...
            while not self._instance.WaitForOPC():
                pass

    @property
    def auto_calibration(self):
        """
        Get the auto calibration flag

        :return: ON or OFF
        """
        cmd = "ACAL?"
        if self._instance.WriteString(cmd, True):
            return self._instance.ReadString(3)

    @auto_calibration.setter
    def auto_calibration(self, state):
        """
        Enable / Disable Auto calibration

        :param state: ON or OFF
        :exception: ValueError: Auto calibration state value not supported
        """
        if state not in Calibration.STATES:
            raise ValueError("Auto calibration state not supported...")
        cmd = "ACAL {0}".format(state)
        self._instance.WriteString(cmd, True)

    @property
    def identifier(self):
        """
        Get scope identifier field.

        :return: Identifier information string
        """
        if self._instance.WriteString("*IDN?", True):
            return self._instance.ReadString(80)
    # ----------------------------------------------------------------------- #
    # ----------------------------------------------------------------------- #
