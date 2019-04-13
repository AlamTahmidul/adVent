import time
from school import clear

class Gym:
    def __init__(self, user):
        class_prompt = input("Enter Gym (Y/N): ")
        if class_prompt.lower() == "y":
            in_gym(user)
        elif class_prompt.lower() == "n":
            out_gym(user)

def in_gym(user):
    clear()
    choice = input("Do you want to run on the treadmill? (Y/N) :")
    if choice.lower() == "n":
        choice = input("Would you like to leave the gym? (Y/N) :")
        if choice.lower() == "y":
            out_gym(user)
    elif choice.lower() == "y":
        print("You are on a treadmill. How long do you want to run? (in minutes) : ")
        tread_inp = input()
        treadmill(tread_inp, user)

def treadmill(tread_inp, user):
    print("{} was on the treadmill for {} minutes".format(user, tread_inp))
    time.sleep(1)

def out_gym(user):
    print("Left Gym. {} gets robbed. Type in y to continue.".format(user))
    class_choice = input()
    if class_choice.lower() == "y":
        print("You have encountered a robber running away with your wallet. What do you do? (Type help for options)")
        class_prompt = input()

    while class_prompt.lower() == "help":
        print("1: Run after him with your cane.")
        print("2: Call your parents and cry.")
        print("3: 'Tactically' *cough* advance and attempt to retrieve your wallet.")
        class_prompt = input()

    if class_prompt.lower() == "1":
        print("You ran after him but could not quite catch up to him. Instead, he was hit by a car.")
        time.sleep(1)
    elif class_prompt.lower() == "2":
        print("Your parents call you pathetic and tell you to man up and solve your own problems. As you are talking a helicopter rams into you.")
        time.sleep(1)
    elif class_prompt.lower() == "3":
        print("You got distracted by 'FREE RAM' and was hit by a car.")
        time.sleep(1)