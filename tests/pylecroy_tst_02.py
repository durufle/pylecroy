from pylecroy import PyLecroy
import time


SCOPE_LASER = "10.67.16.25"
SCOPE_SCA = "10.67.16.22"
SCOPE_EMFI = ""
ADDRESS = SCOPE_LASER

if __name__ == '__main__':

    scope = PyLecroy(ADDRESS)

    # Test identify
    scope.identify()
    print("scope identifier   : " + scope.identifier)

    # print all C1 parameters
    print("Channel C1 Parameters : ", scope.get_parameter(scope.C1, "ALL"))

    # grid state
    for state in scope.GRID_STATE:
        print("Grid state : " + state)
        scope.show_grid(state)
        input("Press a key to continue...")
    # single grid
    scope.show_grid(scope.SINGLE)

    # Set  C1 to C4 to off
    print("Channels  OFF...")
    for channel in scope.WAVEFORM_CHANNELS:
        scope.show_trace(channel, "OFF")
    print("Memory  OFF...")
    for channel in scope.INTERNAL_MEMORY:
        scope.show_trace(channel, "OFF")

    input("Press a key to continue...")
    print("Channel C1 ON...")
    scope.show_trace(scope.C1, "ON")

    input("Get a signal on C1 and press a key to continue...")
    # save C1 to M1
    print("Channel C1 save in M1...")
    scope.save_memory(scope.C1, scope.M1)
    print("Channel C1 OFF...")
    scope.show_trace(scope.C1, "OFF")
    print("Show M1...")
    scope.show_trace(scope.M1, "ON")

    scope.close()
