from school import clear
import time

# Not an object but behaves like an independent code
class Hacker:
    def __init__(self, user, role):
        # Dead-End
        if role.lower() == "athlete":
            print("""
Your Skills as an Athlete:
    1. Proficient Talker
    2. Excellent Stamina
    3. Extraordinary Endurance
                """)
        # BINGO!
        elif role.lower() == "hacker":
            print("""
Your Skills as a Hacker:
    1. Ghost Blackhat
    2. Master Exploiter
    3. Founder of Code Zer0
                """)
        # Dead-End
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
    # Key to winning the game
    if role.lower() == "hacker":
        clear()
        # aesthetic
        print("This is Team Cr3st. We are a hacker group in search of recruits for our annual cityHack.")
        time.sleep(1)
        # Python code, so install as python
        inp = input("\nHello, {}. You have been selected to take part into our cityHack assignment. If you wish to continue, install 'salt'.\n".format(user))
        # User is about to win
        if inp.lower() == "python install salt":
            time.sleep(1)
            print("\nSalt imported")
            print(".bin imported")
            print("Welcome to the Game!")
            launch_hack()
        # User fails to see it as a python shell
        else:
            print("I'm Sorry. You did not make the cut. Please try again next time.")
            leave()
    # Dead-End
    else:
        print("Welcome to the HackerSpace. (You have failed to win).")
        game()

# User Wins
def launch_hack():
    # aesthetics
    print("Dependencies Installed")
    ent = input("> ")
    # cityHack = Anonymous Blackout / DDOSed Web Servers
    if ent in "launch ddos.exe ddos hack3d":
        print("DDOSed. Thank your participating. We will contact you soon of your results.")
        print("- Team Cr3st")
        print("\n\n You have won the game! :)")
        time.sleep(1)
        exit()
    # User fails to see cityHack
    else:
        leave()

def leave():
    print("Left HackerSpace.")