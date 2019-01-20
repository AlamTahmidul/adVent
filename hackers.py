from school import clear
import time

class Hacker:
    def __init__(self, user):
        class_prompt = raw_input("Enter HackerSpace? ")
        if class_prompt.lower() == "y":
            hacker_space(user)
        elif class_prompt.lower() == "n":
            leave()

def hacker_space(user):
    clear()
    print("Welcome to the HackerSpace. What would you like to do today?")
    inp = raw_input()
    if inp.lower() == "python install salt":
        time.sleep(3)
        print("Salt imported")
        time.sleep(2)
        print(".bin imported")
        time.sleep(1)
        print("Welcome to the Game!")
        launch_hack()

def launch_hack():
    print("Okay")

def leave():
    print("Left HackerSpace.")