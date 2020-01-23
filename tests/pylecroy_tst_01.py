from pylecroy import PyLecroy
import matplotlib
import intelhex

SCOPE_LASER = "10.67.16.25"
SCOPE_SCA = "10.67.16.22"
SCOPE_EMFI = ""
ADDRESS = SCOPE_LASER

if __name__ == '__main__':

    scope = PyLecroy(ADDRESS)
    # Get identify
    scope.identify()
    print("scope identifier   : " + scope.identifier)

    # Test trigger mode
    scope.set_trigger_mode(scope.AUTO)
    scope.get_trigger_mode()
    print("scope trigger mode : " + scope.trigger_mode)
    scope.set_trigger_mode(scope.NORM)
    scope.get_trigger_mode()
    print("scope trigger mode : " + scope.trigger_mode)
    scope.set_trigger_mode(scope.SINGLE)
    scope.get_trigger_mode()
    print("scope trigger mode : " + scope.trigger_mode)
    scope.set_trigger_mode(scope.STOP)
    scope.get_trigger_mode()
    print("scope trigger mode : " + scope.trigger_mode)

    try:
        scope.set_trigger_mode("NONE")
    except ValueError as msg:
        print(msg)

    scope.close()
