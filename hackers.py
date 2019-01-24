from school import clear
import time

class Hacker:
    def __init__(self, user, role):
        if role.lower() == "investor":
            print("""
Your Skills as an Investor:
    1. Smooth Talker
    2. Profit Maker
    3. Bitcoin Billionaire
                """)
            time.sleep(2)
        elif role.lower() == "hacker":
            print("""
Your Skills as a Hacker:
    1. Blackhat
    2. Exploiter
    3. Code Zer0
                """)
        else:
            print("""
Your Skills as a Student:
    1. Hard Worker
    2. Honest
    3. Honors Student
                """)
        class_prompt = input("Enter HackerSpace? ")
        if class_prompt.lower() == "y":
            time.sleep(1)
            hacker_space(user, role)
        elif class_prompt.lower() == "n":
            leave()

def hacker_space(user, role):
    clear()
    print("Welcome to the HackerSpace. What would you like to do today?")
    time.sleep(1)
    if role.lower() == "hacker":
        clear()
        print("This is Team Cr3st. We are a hacker group in search of recruits for our annual cityHack.")
        time.sleep(1)
        inp = input("\nHello, {}. You have been selected to take part into our cityHack assignment. If you wish to continue, install 'salt'.\n".format(user))

        if inp.lower() == "python install salt":
            time.sleep(3)
            print("\nSalt imported")
            time.sleep(2)
            print(".bin imported")
            time.sleep(1)
            print("Welcome to the Game!")
            launch_hack()
    else:
        print("Welcome to the HackerSpace.")


def launch_hack():
    print("Dependencies Installed")
    ent = input("> ")
    if ent in "launch ddos.exe ddos hack3d":
        print("DDOSed. Thank your participating. We will contact you soon of your results.")
        print("- Team Cr3st.")
    else:
        leave()

def leave():
    print("Left HackerSpace.")
