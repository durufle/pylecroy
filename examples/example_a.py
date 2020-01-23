from pylecroy import PyLecroy
import matplotlib
import intelhex

SCOPE_LASER = "10.67.16.25"
SCOPE_SCA = "10.67.16.22"
SCOPE_EMFI = "10.67.16.24"
ADDRESS = SCOPE_EMFI

if __name__ == '__main__':

    device = PyLecroy(ADDRESS)

    # Get scope identifier identify
    device.identify()
    print("scope identifier : {} ".format(device.identifier))
    # get current Hardcopy file name
    print("Get Current Hardcopy file name : {} ".format(device.get_hardcopy(device.FILE)))

    # set new hardcopy setup and read back
    # device.set_hardcopy("BMP", "D:\\Hardcopy\\TEST_SCOPE", "example_a.bmp")
    # print("New Hardcopy directory     : {} ".format(device.get_hardcopy_full_setup()))
    device.close()
