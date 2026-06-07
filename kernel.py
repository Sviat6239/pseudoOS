from coreUtils import *

core_version = "0.0.1"

print("Kernel loaded successfully")

while True:
    user_input = input(">>>").strip().lower()

    if user_input in ("help", "h"):
        Help()
    elif user_input in ("about",):
        About()
    elif user_input in ("version", "ver", "v"):
        print(core_version)
    else:
        print("Unknown command, try help.")