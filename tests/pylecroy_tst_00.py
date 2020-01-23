from pylecroy import PyLecroy
import matplotlib
import intelhex

SCOPE_LASER = "169.254.178.97"
SCOPE_SCA = "192.168.168.2"
SCOPE_GLITCH = ""
SCOPE_EMFI = "169.254.52.26"
SCOPE = SCOPE_LASER

if __name__ == '__main__':

    scope = PyLecroy(SCOPE)

    # Test identify
    scope.identify()
    print("scope identifier   : " + scope.identifier)

    # Test trigger mode
    # scope.set_trigger_mode(scope.NORM)
    # scope.get_trigger_mode()
    # print("scope trigger mode : " + scope.trigger_mode)
    # scope.set_hardcopy(BMP, "D:\\folder", "test.bmp")
    # print(scope.get_hardcopy())
    # scope.print_screen()

    # waveform is a byte array
    # waveform = (scope.get_wave(scope.NATIVE, scope.C1, 10000, 0))

    # print all C1 parameters
    # print("Channel C1 Parameters : ", scope.get_parameter(scope.C1, "ALL"))
    # reboot scope
    # scope.reboot()

    # Test panel functions
    # panel_a = scope.get_panel()
    # scope.set_panel(panel_a)
    # input("Press a key to continue...")
    # scope.show_grid(SINGLE)
    # for trace in scope.TRACE_CHANNELS:
    #     scope.show_trace(trace, OFF)
    # input("Press a key to continue...")
    # Visualize C1

    # scope.show_trace(scope.C1, scope.ON)
    # scope.show_trace(scope.Z1, scope.OFF)
    # save Z1 to M1
    # scope.save_memory(scope.Z1, scope.M1)
    # scope.get_wave_to_file("./test_full.bin", scope.BYTE, scope.C1, 2000000)
    # scope.display_wave("./test_full.bin")
    # scope.get_wave_to_file("./test_partial.bin", scope.BYTE, scope.C1, 2000000, 1000000)
    # scope.get_wave_to_file("./test_full_z1.bin", scope.BYTE, scope.Z1, 1000000, 500000)
    # scope.display_wave("./test_full_z1.bin")
    intelhex.bin2hex("./test_full.bin", "./test_full.hex", 0)
    scope.close()
