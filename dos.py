print("Starting a DOS...")
import time
time.sleep(5)
is_on = 1
while is_on == 1 :
    response = input("C:")
    if response.lower().strip() == "ver" :
        print("This is a DOS.")
        print("This has been created in 2024")
    elif response.lower().strip() == "exit" :
        print("exiting...")
        time.sleep(5)
        is_on = 0
    elif response.lower().strip() == "help" :
        print("VER   : Gives information about the system.")
        print("EXIT  : Exits the DOS interface.")
    else :
        print("This command does not exist.")
