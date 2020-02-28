from pylecroy import PyLecroy

SCOPE_LASER = "10.67.16.26"
SCOPE_SCA = "10.67.16.22"
SCOPE_EMFI = "10.67.16.24"
ADDRESS = SCOPE_LASER

if __name__ == '__main__':

    device = PyLecroy(ADDRESS)

    # Get scope identifier identify
    device.identify()
    print("scope identifier : {} ".format(device.identifier))
    # get current Hardcopy file name
    print("Get Current Hardcopy file name : {} ".format(device.get_hardcopy(device.FILE)))

    device.close()
