from pylecroy import PyLecroy
import matplotlib
import intelhex

SCOPE_LASER = "10.67.16.25"
SCOPE_SCA = "10.67.16.22"
SCOPE_EMFI = ""
ADDRESS = SCOPE_LASER

FOLDER = "D:\\HARDCOPY\\TEST_LECROY"
FILE = "test_screen"

if __name__ == '__main__':

    scope = PyLecroy(ADDRESS)

    # Get identify
    scope.identify()
    print("scope identifier   : " + scope.identifier)

    # Get current hardcopy setup
    print(scope.get_hardcopy_full_setup())
    # get current hardcopy directory
    print("Hardcopy directory : " + scope.get_hardcopy())

    # Set new hardcopy environment (dir, file)
    scope.set_hardcopy(scope.BMP, FOLDER, FILE)
    print("Hardcopy directory : " + scope.get_hardcopy())

    input("Display signal on channel C1 and press a key to continue...")
    # Perform a print screen
    scope.print_screen()
    input("Check print screen file in scope and press a key to continue...")

    scope.close()
