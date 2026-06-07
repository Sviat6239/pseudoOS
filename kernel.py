user_input = ""

print("Kernel loaded succesfull")

while True:
    user_input = input(">>>")

    if user_input == "help" or "h" or "-h":
        print("List of comannds: ")

    if user_input == "about" or "-about":
        print("this is a simple terminal operationg system that written in Python Programming language.")    