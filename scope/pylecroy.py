#!/usr/bin/python3
#
# Lecroy scope class
#
import sys
import win32com.client
import logging
import logging.config
import numpy as np
import matplotlib.pyplot as plt


class PyLecroy:
    """
    Class to drive a Lecroy oscilloscope using ActiveDSO active X

    """
    version = "0.1.1"
    __version__ = version

    # scope mode
    LOCAL, REMOTE = (0, 1)
    # trigger , grid mode
    AUTO, NORM, SINGLE, STOP = \
        ('AUTO', 'NORM', 'SINGLE', 'STOP')
    DUAL, QUAD, OCTAL, XY, XYSINGLE, XYDUAL, TANDEM, QUATTRO, TWELVE, SIXTEEN, TRIPLE, HEX = \
        ('DUAL', 'QUAD', 'OCTAL', 'XY', 'XYSINGLE', 'XYDUAL', 'TANDEM', 'QUATTRO', 'TWELVE', 'SIXTEEN', 'TRIPLE', 'HEX')
    # hardcopy
    BMP, JPEG, PNG, TIFF = ('BMP', 'JPEG', 'PNG', 'TIFF')
    FOLDER, FILE = (9, 11)
    # Waveform mode
    BYTE, INTEGER, SCALED, NATIVE = (0, 1, 2, 3)
    C1, C2, C3, C4, M1, M2, M3, M4, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, F1, F2, F3, F4, F5, F6, F7, F8 = \
        ("C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4",
         "Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8",
         "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8")
    ON, OFF = ("ON", 'OFF')

    # Setup slot
    S1, S2, S3, S4, S5, S6 = (0, 1, 2, 3, 4, 5)

    # List
    SCOPE_MODES = (LOCAL, REMOTE)
    TRIG_MODES = (AUTO, NORM, SINGLE, STOP)
    HARDCOPY_DEVICES = (BMP, JPEG, PNG, TIFF)
    WAVEFORM_MODES = (BYTE, INTEGER, SCALED, NATIVE)
    WAVEFORM_CHANNELS = (C1, C2, C3, C4, Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, F1, F2, F3, F4, F5, F6, F7, F8)
    INTERNAL_MEMORY = (M1, M2, M3, M4)
    DISPLAY_STATE = (ON, OFF)
    TRACE_STATE = DISPLAY_STATE
    TRACE_CHANNELS = WAVEFORM_CHANNELS
    GRID_STATE = (AUTO, SINGLE, DUAL, QUAD, OCTAL, XY, XYSINGLE, XYDUAL, TANDEM, QUATTRO, TWELVE, SIXTEEN, TRIPLE, HEX)
    SETUP_SLOT = (S1, S2, S3, S4, S5, S6)

    def __init__(self, address):
        self._address = None
        self._is0pen = False
        self._instance = None
        self._identifier = None
        self._mode = None
        self._timeout = 1
        self._trigger_mode = None
        self._calibration = None

        self._logger = logging.getLogger(__name__)

        if not address:
            # empty address
            self._logger.warning("An empty address has been  provided...")
            sys.exit()
        else:
            self._address = address
            self.open()

    # ----------------------------------------------------------------------- #
    def open(self):
        """
        Create a connection with the device and setup in remote mode

        :return:
        """
        self._instance = win32com.client.Dispatch("LeCroy.ActiveDSOCtrl.1")
        """ Create Connection with device """
        if self._instance.MakeConnection("IP:" + self._address):
            self._logger.info("Connexion established...")
            self._is0pen = True
            self.set_timeout(self._timeout)
            self.set_mode(self.REMOTE)
            self.beep()
        else:
            self._logger.warning("Connection with scope failed...")
            sys.exit(-1)
    # ----------------------------------------------------------------------- #

    def close(self):
        """
        Close communication with the device. Switch the device in local
        mode before closing.

        """
        self.set_mode(self.LOCAL)
        if self._instance.Disconnect():
            self._is0pen = False
        else:
            self._logger.warning("Dis-connection with scope failed...")

    # ----------------------------------------------------------------------- #

    @property
    def address(self):
        """
        Return the device address. This method return the private variable.

        :return:  address value
        """
        return self._address
    # ----------------------------------------------------------------------- #

    def set_address(self, address):
        """
        Set IP address. This method close previous session if opened, and
        perform a new opening session using the new address.

        :param address:
        :return:
        """
        """ set ip address """
        if address is None:
            raise ValueError("Address value must be provided...")
        if self._is0pen:
            self.close()
        self._address = address
        self.open()

    # ----------------------------------------------------------------------- #

    @property
    def mode(self):
        """
        Get the current scope mode. This method return the private variable.

        :return: device mode.
        """
        return self._mode

    # ----------------------------------------------------------------------- #

    def set_mode(self, mode):
        """
        Set the scope mode (remote or local
        :param mode:
        :return:
        """
        if mode not in self.SCOPE_MODES:
            raise ValueError("Not a valid mode...")

        if self._is0pen:
            if self._instance.SetRemoteLocal(mode):
                self._mode = mode
            else:
                self._logger.warning("set mode failed...")

    # ----------------------------------------------------------------------- #

    def set_timeout(self, value):
        """

        :param value:
        :return:
        """
        if self._instance.SetTimeout(value):
            self._timeout = value
        else:
            self._logger.warning("Set timeout failed...")

    # ----------------------------------------------------------------------- #
    def get_hardcopy_full_setup(self):
        """
        Get all hard-copy setup

        :return: return the complete of hardware setup as a list.
        """
        if self._instance.WriteString("HCSU?", True):
            return self._instance.ReadString(5000).split(",")

    def get_hardcopy(self, index):
        """
        Get and print hardcopy directory

        :return: hardcopy directory from hardware setup
        """
        setup = self.get_hardcopy_full_setup()
        self._logger.info("Hardcopy directory : " + setup[index])
        return setup[index]

    def set_hardcopy(self, device, directory, name):
        """
        Partial hard-copy setup.

        :param device: print screen file format
        :param directory: print screen directory
        :param name: file name
        :exception: ValueError:
        """
        if device not in self.HARDCOPY_DEVICES:
            raise ValueError("Not a valid device value...")

        # Create MAUI command
        cmd = "HCSU DEV,{0},DIR,\"{1}\",FILE,\"{2}\" ".format(device, directory, name)
        if not self._instance.WriteString(cmd, True):
            self._logger.warning("Print screen command failed...")

    # ----------------------------------------------------------------------- #
    def store_hardcopy(self, name):
        """
        Store an hardcopy file form scope to PC.

        :param name: file name
        :return:
        """
        if not self._instance.StoreHardcopyToFile("BMP", "", name):
            self._logger.warning("hardcopy failed...")

    # ----------------------------------------------------------------------- #

    def print_screen(self):
        """
        Perform a print screen. See set_hardcopy method

        :return:
        """
        if not self._instance.WriteString("SCDP", True):
            self._logger.warning("Print screen command failed...")

    # ----------------------------------------------------------------------- #

    def delete_hardcopy(self, name):
        """ delete an hardcopy file in scope"""

    # ----------------------------------------------------------------------- #
    def set_waveform_transfer(self, first_point):
        """ configures parameters controlling the waveform transfer """
        if not self._instance.SetupWaveformTransfer(first_point, 0, 0):
            self._logger.warning("set waveform command failed...")

    # ----------------------------------------------------------------------- #

    def get_wave(self, mode, name, max_bytes, first_byte):
        """
        Get a wave from scope, and return it

        :param mode:
        :param name:
        :param max_bytes:
        :param first_byte:
        :return:
        """
        if mode not in self.WAVEFORM_MODES:
            raise ValueError("Not a valid get waveform mode...")
        if name not in self.WAVEFORM_CHANNELS:
            raise ValueError("Not a valid channel...")
        if mode == self.BYTE:
            wave = self._instance.GetByteWaveform(name, max_bytes, 0)
        else:
            raise ValueError("Not a supported get waveform mode...")
        return wave[first_byte:]

    # ----------------------------------------------------------------------- #

    def get_wave_to_file(self, filename, mode, name, max_bytes, first_byte=0):
        """
        get a waveform and sva into a file. If file already exist then is
        overwritten.

        :param filename:
        :param mode:
        :param name:
        :param max_bytes:
        :param first_byte:
        :return:
        """
        filemode = "wb"
        # get data trace from scope.
        data = self.get_wave(mode, name, max_bytes, first_byte)

        f = open(filename, filemode)
        f.write(data)
        f.close()

    @staticmethod
    def display_wave(filename=""):
        """
        Display to screen a trace from file. be careful to type

        :param filename: trace file
        """
        with open(filename, 'rb') as f:
            array = np.frombuffer(f.read(), dtype=np.uint8)
        plt.plot(array)
        plt.show()
    # ----------------------------------------------------------------------- #

    @property
    def trigger_mode(self):
        """
        Return the internal trigger mode

        :return: trigger mode
        """
        return self._trigger_mode

    def set_trigger_mode(self, mode):
        """
        Set trigger mode

        :param mode: trigger mode part of TRIG_MODES
        """
        if self._is0pen:
            if mode not in self.TRIG_MODES:
                raise ValueError("Not a Valid mode...")

            if not self._instance.WriteString("TRMD " + mode, True):
                self._logger.warning("set trigger mode command failed...")
            # Waiting scope available...
            while self._instance.WaitForOPC() != 1:
                pass

    def get_trigger_mode(self):
        """
        Return current trigger mode

        :return: trigger mode
        """
        if self._is0pen:
            if self._instance.WriteString("TRMD?", True):
                self._trigger_mode = self._instance.ReadString(80)

    def arm(self):
        """
        Arm the scope for single mode

        """
        self.set_trigger_mode(self.SINGLE)

    # ----------------------------------------------------------------------- #

    def get_parameter(self, name, parameter):
        """


        :param name:
        :param parameter:
        :return:
        """
        if name not in self.WAVEFORM_CHANNELS:
            raise ValueError("Not a valid channel...")
        cmd = "{0}:PAVA? {1}".format(name, parameter)
        if self._instance.WriteString(cmd, 1):
            return self._instance.ReadString(1000)

    # ----------------------------------------------------------------------- #
    def set_panel(self, panel):
        self._instance.SetPanel(panel)

    def get_panel(self):
        """

        """
        return self._instance.GetPanel()

    # ----------------------------------------------------------------------- #
    # Display Commands and Queries

    def display(self, state):
        """

        :param state:
        :exception: ValueError: display state value not supported
        """
        if state not in self.DISPLAY_STATE:
            raise ValueError("Display state not supported...")
        cmd = "DISP {0}".format(state)
        self._instance.WriteString(cmd, True)

    def show_grid(self, grid):
        """
        Change scope grid format

        :param grid: grd format
        :exception ValueError: grid value not supported
        """
        if grid not in self.GRID_STATE:
            raise ValueError("Grid mode not supported...")
        cmd = "GRID {0}".format(grid)
        self._instance.WriteString(cmd, True)

    def show_message(self, msg):
        """
        Show a custom message to the screen

        :param msg: message
        """
        cmd = "MSG {0}".format(msg)
        self._instance.WriteString(cmd, True)

    def show_trace(self, trace, state):
        """
        Display/ Doesn't display a channel to the scope screen.

        :param trace: trace channel number
        :param state: ON / OFF
        """
        if (trace not in self.WAVEFORM_CHANNELS) and (trace not in self.INTERNAL_MEMORY):
            raise ValueError("Trace selected not supported...")
        if state not in self.TRACE_STATE:
            raise ValueError("state selected not supported...")
        cmd = "{0}:TRA {1}".format(trace, state)
        self._instance.WriteString(cmd, True)

    def save_memory(self, trace, memory):
        """
        Save a trace in an internal memory slot

        :param trace: trace channel number
        :param memory: memory slot n umber
        """
        if trace not in self.WAVEFORM_CHANNELS:
            raise ValueError("Trace selected not supported...")
        if memory not in self.INTERNAL_MEMORY:
            raise ValueError("Memory selected not supported...")
        cmd = "STO {0},{1}".format(trace, memory)
        self._instance.WriteString(cmd, True)

    def recall_setup(self, setup):
        """
        Recall a setup stored in an internal setup slot

        :param: setup slot number
        """
        if setup not in self.SETUP_SLOT:
            raise ValueError("Setup slot selected not supported...")
        cmd = "*RCL {0}".format(setup)
        self._instance.WriteString(cmd, True)

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

        """
        self._instance.WriteString("BUZZ BEEP", 1)

    @property
    def calibration(self):
        """
        Return calibration result.

        :return: calibration result
        """
        return self._calibration

    def calibrate(self):
        """
        Execute a calibration. The result is saved.

        :return:
        """
        if self._instance.WriteString("*CAL?", True):
            self._calibration = self._instance.ReadString(10)
        else:
            self._logger.warning("Calibration command failed...")

    @property
    def identifier(self):
        """
        Return the identifier field. A call to identify method shall be previously
        executed.

        :return:
        """
        return self._identifier

    def identify(self):
        """
        Get scope identifier field.

        """
        if self._instance.WriteString("*IDN?", True):
            self._identifier = self._instance.ReadString(80)
    # ----------------------------------------------------------------------- #
    # ----------------------------------------------------------------------- #
