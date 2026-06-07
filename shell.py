from coreUtils import *

kernel_version = "0.0.2"
shell_version = "0.0.1"

def Shell():

    print("Kernel loaded successfully")
    print("Shell loaded successfully")

    user_input = input(">>>").strip().lower()

    if user_input in ("help", "h"):
        Help()
    elif user_input in ("about",):
        About()
    elif user_input in ("version", "ver", "v"):
        print("Kernel version:" + kernel_version)
        print("Shell version" + shell_version)
    elif user_input in ("poweroff", "off"):
        Poweroff()
    else:
        print("Unknown command, try help.")