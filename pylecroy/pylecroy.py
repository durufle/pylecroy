"""
pylecroy module
"""

import sys
import logging
import enum
import warnings
from typing import Union
import win32com.client


class CustomException(Exception):
    """Exception raised when very uncommon things happen"""
    pass


class MetaConst(type):
    """
    MetaConst class
    """
    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        raise TypeError


class Const(object, metaclass=MetaConst):
    """
    Constant class
    """
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError


class MyEnumMeta(enum.EnumMeta):
    """
    MyMetaClass class
    """
    def __contains__(cls, item):
        if not isinstance(item, enum.Enum):
            if isinstance(item, str) or isinstance(item, int):
                return item in [v.value for v in cls.__members__.values()]

            warnings.warn(
                "in 3.12 __contains__ will no longer raise TypeError, but will return True if\n"
                "obj is a member or a member's value",
                DeprecationWarning,
                stacklevel=2,
            )
            raise TypeError(
                "unsupported operand type(s) for 'in': '%s' and '%s'" % (
                    type(item).__qualname__, cls.__class__.__qualname__))
        return isinstance(item, cls) and item._name_ in cls._member_map_


class Remote(Const):
    """
    Remote const class
    """
    class Modes(enum.Enum, metaclass=MyEnumMeta):
        LOCAL = 0
        REMOTE = 1


class Trigger(Const):
    """
    Trigger const class
    """
    class Modes(enum.Enum, metaclass=MyEnumMeta):
        AUTO = 'AUTO'
        NORMAL = 'NORM'
        SINGLE = "SINGLE"
        STOP = "STOP"


class Grid(Const):
    """
    Grid const class
    """
    class States(enum.Enum, metaclass=MyEnumMeta):
        AUTO = 'AUTO'
        SINGLE = 'SINGLE'
        DUAL = 'DUAL'
        QUAD = 'QUAD'
        OCTAL = 'OCTAL'
        XYONLY = 'XYONLY'
        XYSINGLE = 'XYSINGLE'
        XYDUAL = 'XYDUAL'
        TANDEM = 'TANDEM'
        QUATTRO = 'QUATTRO'
        TWELVE = 'TWELVE'


class WaveForm(Const):
    """
    Waveform const class
    """
    class Channels(enum.Enum, metaclass=MyEnumMeta):
        C1, C2, C3, C4 = ('C1', 'C2', 'C3', 'C4')
        Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8 = ('Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8')
        F1, F2, F3, F4, F5, F6, F7, F8 = ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8')
        M1, M2, M3, M4 = ('M1', 'M2', 'M3', 'M4')

    class Modes(enum.Enum, metaclass=MyEnumMeta):
        BYTE, INTEGER, SCALED, NATIVE = ('BYTE', 'INTEGER', 'SCALED', 'NATIVE')

    class Blocks(enum.Enum, metaclass=MyEnumMeta):
        DESC, TEXT, TIME, DAT1, DAT2, ALL = ("DESC", 'TEXT', 'TIME', 'DAT1', 'DAT2', 'ALL')

    class StoreModes(enum.Enum, metaclass=MyEnumMeta):
        OFF, FILL, WRAP = ("OFF", "FILL", "WRAP")

    class Formats(enum.Enum, metaclass=MyEnumMeta):
        ASCII, BINARY, EXCEL, MATHCAD, MATLAB = ("ASCII", "BINARY", "EXCEL", "MATHCAD", "MATLAB")


class Parameters(Const):
    """
    Parameters const class
    """
    class Channels(enum.Enum, metaclass=MyEnumMeta):
        C1 = "C1"
        C2 = "C2"
        C3 = "C3"
        C4 = "C4"
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
        M1 = "M1"
        M2 = "M2"
        M3 = "M3"
        M4 = "M4"

    class Param(enum.Enum, metaclass=MyEnumMeta):
        # Parameters related constants
        ALL = 'ALL'
        AMPL = 'AMPL'
        DELAY = 'DLY'

        RISE = 'RISE'
        FALL = 'FALL'
        MEAN = 'MEAN'
        PKPK = 'PKPK'


class Display(Const):
    """
    Display const class
    """
    class States(enum.Enum, metaclass=MyEnumMeta):
        OFF = "OFF"
        ON = "ON"

    class Channels(enum.Enum, metaclass=MyEnumMeta):
        C1 = "C1"
        C2 = "C2"
        C3 = "C3"
        C4 = "C4"
        F1 = "F1"
        F2 = "F2"
        F3 = "F3"
        F4 = "F4"
        F5 = "F5"
        F6 = "F6"
        F7 = "F7"
        F8 = "F8"
        M1 = "M1"
        M2 = "M2"
        M3 = "M3"
        M4 = "M4"


class Setup(Const):
    """
    Setup const class
    """
    class Slots(enum.Enum, metaclass=MyEnumMeta):
        S1, S2, S3, S4, S5, S6 = (0, 1, 2, 3, 4, 5)


class HardCopy(Const):
    """
    Hardcopy const class
    """
    class Formats(enum.Enum, metaclass=MyEnumMeta):
        BMP = 'BMP'
        JPEG = 'JPEG'
        PNG = 'PNG'
        TIFF = 'TIFF'


class Calibration(Const):
    """
    Calibration const class
    """
    class States(enum.Enum, metaclass=MyEnumMeta):
        OFF = 'OFF'
        ON = 'ON'


class Sequence(Const):
    """
    Sequence const class
    """
    class Modes(enum.Enum, metaclass=MyEnumMeta):
        ON = 'ON'
        OFF = 'OFF'


class Command(Const):
    """
    Command const class
    """
    class Header(Const):
        class Modes(enum.Enum, metaclass=MyEnumMeta):
            ON = 'ON'
            OFF = 'OFF'

    class Help(Const):
        class Levels(enum.Enum, metaclass=MyEnumMeta):
            OFF = 'OFF'
            EO = 'EO'
            FD = 'FD'

        class Reset(enum.Enum, metaclass=MyEnumMeta):
            YES = 'YES'
            NO = 'NO'


class Disk(Const):
    """
    Disk const class
    """
    class Devices(enum.Enum, metaclass=MyEnumMeta):
        HDD = 'HDD'
        USB = 'USB'
        MICRO = 'MICRO'


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

    @staticmethod
    def __get_from_type(param: Union[str, enum.Enum]):
        if type(param) is str:
            return param
        else:
            return param.value

    # ----------------------------------------------------------------------- #
    def open(self, address):
        """
        Create a connection with the device and setup in remote mode

        :param address: Device connection
        """
        self._instance = win32com.client.Dispatch("LeCroy.ActiveDSOCtrl.1")

        if self._instance.MakeConnection(address):
            self._is_open = True
            self.timeout = 1
            self.mode = Remote.Modes.REMOTE
            self.beep()
        else:
            sys.exit("Connection with scope failed...")

    def close(self):
        """
        Close communication with the device. Switch the device in local
        mode before closing.
        """
        self.mode = Remote.Modes.LOCAL
        if self._instance.Disconnect():
            self._is_open = False

    # ----------------------------------------------------------------------- #
    @property
    def mode(self) -> Remote.Modes:
        """
        Get the current scope mode.

        :return: Remote mode.
        """
        return Remote.Modes(self._mode)

    @mode.setter
    def mode(self, mode: Union[str, Remote.Modes]):
        """
        Set the scope mode (remote or local)

        :param mode: Remote mode
        """
        if mode not in Remote.Modes:
            raise ValueError("Not a valid mode...")

        if self._is_open and self._instance.SetRemoteLocal(self.__get_from_type(mode)):
            self._mode = mode

    # ----------------------------------------------------------------------- #
    @property
    def timeout(self):
        """
        timeout property
        """
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
        Get hardcopy configuration

        :return: return the complete of hardware setup as a dict.
        """
        if self._instance.WriteString("HCSU?", True):
            result = self._instance.ReadString(5000).split(',')
            return dict(zip(result[::2], result[1::2]))

    @hardcopy.setter
    def hardcopy(self, config: dict):
        """
        set hardcopy configuration using a dictionary
        """
        # convert dictionary into list
        new_list = zip(config.keys(), config.values())
        new_list = list(new_list)

        fields = []
        for i in new_list:
            item, value = i
            fields.append(f"{item},{value},")

        params = ''.join(fields)
        cmd = 'HCSU ' + params
        self._instance.WriteString(cmd, True)
        while not self._instance.WaitForOPC():
            pass

    # ----------------------------------------------------------------------- #
    def store_hardcopy(self, name, form='BMP'):
        """
        Store a hardcopy file from scope to PC.

        :param name: file name
        :param form: Hardcopy format
        """
        self._instance.StoreHardcopyToFile(form, "", name)

    # ----------------------------------------------------------------------- #

    def screen_dump(self):
        """
        Perform a screen dump. See set_hardcopy method
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

        :notes: This method affects how the various GetWaveform functions transfer a waveform. For the majority of cases the default settings will be sufficient. These are Start Transfer at first point, Transfer all data points Transfer all segments.
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

    def get_wave(self, mode: Union[str, WaveForm.Modes], channel: Union[str, WaveForm.Channels], max_bytes):
        """
        Get a wave from scope, and return it

        :param mode: mode (BYTE, INTEGER, SCALED, NATIVE)
        :param channel: channel name
        :param max_bytes: maximum byte
        :return: list of waveform values

        :notes: For NATIVE WaveForm, 12-bit oscilloscopes must use the 16-bit word format. Set maxBytes value as <number of bytes to read> x 2.
        """
        wave = None
        if mode not in WaveForm.Modes:
            raise ValueError("Not a valid get waveform mode...")
        if channel not in WaveForm.Channels:
            raise ValueError("Not a valid channel...")

        mode = self.__get_from_type(mode)
        channel = self.__get_from_type(channel)

        if mode == 'BYTE':
            wave = self._instance.GetByteWaveform(channel, max_bytes, 0)
        elif mode == 'INTEGER':
            wave = self._instance.GetIntegerWaveform(channel, max_bytes, 0)
        elif mode == 'SCALED':
            wave = self._instance.GetScaledWaveform(channel, max_bytes, 0)
        elif mode == 'NATIVE':
            wave = self._instance.GetNativeWaveform(channel, max_bytes, False, 'ALL')
        return wave

    # ----------------------------------------------------------------------- #

    @property
    def trigger_mode(self) -> Trigger.Modes:
        """
        Return current trigger mode

        :return: trigger mode
        """
        if self._instance.WriteString("TRMD?", True):
            return Trigger.Modes(self._instance.ReadString(80))

    @trigger_mode.setter
    def trigger_mode(self, mode: Union[str, Trigger.Modes]):
        """
        Set trigger mode

        :param mode: trigger mode in Trigger.Mode or in ['AUTO', 'NORM', 'SINGLE','STOP']
        """
        if mode not in Trigger.Modes:
            raise ValueError(f'Param is not a Trigger Modes : {mode}')
        self._instance.WriteString(f"TRMD {self.__get_from_type(mode)}", True)
        while not self._instance.WaitForOPC():
            """
            Wait OPC
            """
            pass

    def trigger_arm(self):
        """
        Arm the scope for single mode
        """
        self.trigger_mode = Trigger.Modes.SINGLE

    def wait(self, timeout=1):
        self._instance.WriteString(f"WAIT {timeout}", True)
        while not self._instance.WaitForOPC():
            """ Wait OPC """
            pass

    @property
    def trigger(self) -> str:
        """
        Get the trigger mode

        :return: trigger mode in ['AUTO', 'NORM', 'SINGLE', 'STOP']
        """
        if self._instance.WriteString("TRMD?", True):
            return self._instance.ReadString(80)

    @trigger.setter
    def trigger(self, mode: str):
        """
        Set trigger mode

        :param mode: trigger mode in ['AUTO', 'NORM', 'SINGLE', 'STOP']
        """
        if mode not in ['AUTO', 'NORM', 'SINGLE', 'STOP']:
            raise ValueError(f'Param is not a Trigger Modes : {mode}')
        self._instance.WriteString(f"TRMD {mode}", True)
        while not self._instance.WaitForOPC():
            pass

    @property
    def sequence(self) -> dict:
        """
        Return Conditions for the sequence acquisition

        :return: Return sequence Mode, number sequences and memory length
        """
        if self._instance.WriteString("SEQUENCE?", True):
            value = self._instance.ReadString(10)
            setup = {}
            (setup["Mode"]) = self._instance.GetCommaDelimitedString(value, 0)
            (setup["Segments"]) = self._instance.GetCommaDelimitedString(value, 1)
            (setup["Size"]) = self._instance.GetCommaDelimitedString(value, 2)
            return setup

    def set_sequence(self, mode: Union[str, Sequence.Modes], segment, size):
        """
        Set conditions for the sequence acquisition.

        :param mode: ON or OFF
        :param segment: number segment
        :param size: memory length

        :note: The size value can be expressed either as numeric fixed point, exponential, or using standard suffixes
        """
        if mode not in Sequence.Modes:
            raise ValueError("Not a valid mode...")
        return self._instance.WriteString(f"SEQUENCE {self.__get_from_type(mode)},{segment},{size}", True)

    # ----------------------------------------------------------------------- #
    # CURSOR - Performing Measurements
    # ----------------------------------------------------------------------- #

    def get_parameter(self, channel: Union[str, Parameters.Channels], parameter: Union[str, Parameters.Param]):
        """
        Return a channel parameters(s)

        :param channel: Channel Name in Channels constant class
        :param parameter: Channel Parameter in Parameters class
        :return: Parameter value
        """
        if channel not in Parameters.Channels:
            raise ValueError("Not a valid channel...")
        if parameter not in Parameters.Param:
            raise ValueError("Not a valid parameter...")

        if self._instance.WriteString(f"{self.__get_from_type(channel)}:PAVA? {self.__get_from_type(parameter)}", True):
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
        if channel not in WaveForm.All:
            raise ValueError("Trace selected not supported...")
        if memory not in WaveForm.Memories:
            raise ValueError("Memory selected not supported...")
        cmd = f"STO {channel},{memory}"
        return self._instance.WriteString(cmd, True)

    # ----------------------------------------------------------------------- #
    # SAVE/RECALL SETUP - Preserving and Restoring Panel Settings
    # ----------------------------------------------------------------------- #
    def recall_setup(self, setup):
        """
        Recall a setup stored in an internal setup slot

        :param: setup slot number
        :return: Write command status

        :exception: ValueError: Setup slot selected not supported..
        """
        if setup not in Setup.Slots:
            raise ValueError("Setup slot selected not supported...")
        cmd = "*RCL {0}".format(setup)
        self._instance.WriteString(cmd, True)

    def save_setup(self, setup):
        """
        Save a setup stored in an internal setup slot

        :param: setup slot number
        :return: Write command status

        :exception: ValueError: Setup slot selected not supported..
        """
        if setup not in Setup.Slots:
            raise ValueError("Setup slot selected not supported...")
        cmd = f"*SAV {setup}"
        return self._instance.WriteString(cmd, True)

    # ----------------------------------------------------------------------- #
    # Display Commands and Queries
    # ----------------------------------------------------------------------- #

    @property
    def display(self) -> Display.States:
        """
        Get display mode
        :return: Display.States.ON or Display.States.OFF
        """
        if self._instance.WriteString("DISP?", True):
            return Display.States(self._instance.ReadString(10))

    @display.setter
    def display(self, state: Union[str, Display.States]):
        """
        Set display mode

        :param state: 'ON' or 'OFF' or Display.States.ON or Display.States.OFF
        :exception: ValueError: display state value not supported

        :notes:
        When you set the display to OFF, the screen does not actually go blank. Instead, the real-time
        clock and the message field are continuously updated. but waveforms and associated text are frozen.
        """
        if state not in Display.States:
            raise ValueError("Display state not supported...")
        self._instance.WriteString(f"DISP {self.__get_from_type(state)}", True)

    @property
    def grid(self) -> Grid.States:
        """
        return the style of grid used
        """
        if self._instance.WriteString("GRID?", True):
            return Grid.States(self._instance.ReadString(10))

    @grid.setter
    def grid(self, grid: Union[str, Grid.States]):
        """
        Change scope grid format

        :param grid: grid format
        :exception ValueError: Grid mode not supported
        """
        if grid not in Grid.States:
            raise ValueError("Grid mode not supported...")
        self._instance.WriteString(f"GRID {self.__get_from_type(grid)}", True)
        while not self._instance.WaitForOPC():
            """ Wait OPC """
            pass

    def display_channel(self, name: Union[str, Display.Channels], state: Union[str, Display.States]):
        """
        Display/ Doesn't display a channel to the scope screen.

        :param name: Channel name
        :param state: ON / OFF
        :return: Write command status
        """
        if name not in Display.Channels:
            raise ValueError(f"Channel {name} selected not supported...")

        if state not in Display.States:
            raise ValueError("state selected not supported...")

        cmd = f"{self.__get_from_type(name)}:TRA {self.__get_from_type(state)}"
        self._instance.WriteString(cmd, True)
        while not self._instance.WaitForOPC():
            """ Wait OPC """
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
            while not self._instance.WaitForOPC():
                pass

    @property
    def auto_calibration(self) -> Calibration.States:
        """
        Get the auto calibration flag

        :return: ON or OFF
        """
        cmd = "ACAL?"
        if self._instance.WriteString(cmd, True):
            return Calibration.States(self._instance.ReadString(3))

    @auto_calibration.setter
    def auto_calibration(self, state: Union[str, Calibration.States]):
        """
        Enable / Disable Auto calibration

        :param state: ON or OFF or Calibration.States.ON or Calibration.States.OFF
        :exception: ValueError: Auto calibration state value not supported
        """
        if state not in Calibration.States:
            raise ValueError(f'Param is not a Calibration states : {state}')
        self._instance.WriteString(f"ACAL {self.__get_from_type(state)}", True)

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
