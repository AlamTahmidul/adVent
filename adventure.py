import os
from school import School, clear
from gym import Gym
from hackers import Hacker
import time

# Display name of the game
print("""
     -------------------------------------------------------------------------------------------------------------------------
    |                                          _____ _            _____                                                       |
    |                                         |_   _| |          |  __ \                                                      |
    |                                           | | | |__   ___  | |  \/ __ _ _ __ ___   ___                                  |
    |                                           | | | '_ \ / _ \ | | __ / _` | '_ ` _ \ / _ \                                 |
    |                                           | | | | | |  __/ | |_\ | (_| | | | | | |  __/                                 |
    |                                           \_/ |_| |_|\___|  \____/\__,_|_| |_| |_|\___|                                 |
    |                                                                                                                         |
     -------------------------------------------------------------------------------------------------------------------------

""")
time.sleep(1)

# Roles and standard inputs
roles = ["Hacker", "Student", "Athlete"]
play_again = ["yes", "no", "n", "y"]

# aesthetics
def display_user(user_name, role):
    print("""
User: {}
Role: {}
        """.format(user_name, role))

def game():
    clear()
    alive = True
    # Context/Background
    print("""
     _________________________________________________________________________________________________________________________
    |   Welcome to New York, the city filled with hopes and dreams for every hacker, student, and athlete.                    |
    |   You are a student living in Manhattan where every opportunity makes you $$$. It is your duty to                       |
    |   live your life fully, and make the best decisions.                                                                    |
    |                                                                                                                         |
    |   WARNING: YOU WILL BE HELD RELIABLE FOR ALL YOUR CHOICES. IF YOU ARE NOT A GOOD BOY, PREPARE TO FACE THE CONSEQUENCES. |
    |_________________________________________________________________________________________________________________________|
    """)
    time.sleep(1)
    # User Inputs name (aesthetic)
    user_name = input("Username: ")
    # User Inputs Password (aesthetic)
    password = input("Password: ")
    # User Inputs Role (Important!)
    role = input("Choose Your Role: ")
    # 3 Given roles given the context
    if role in roles:
        display_user(user_name, role)
    else:
        # Default is Student
        print("Invalid Role. Default role of 'student' selected.")
        role = "Student"
        display_user(user_name, role)
    # aesthetic
    print("\nLogged in.")
    time.sleep(1)
    clear()
    # Display (aesthetic)
    print("\nHello, " + user_name + ".")
    print("\nWhere would you like to go today?")
    # Important for Winning the Game
    choice = input("> ")
    while True:
        # Dead-End
        if choice.lower() == "school":
            print("launching school.exe")
            time.sleep(1)
            School(user_name)
        # BINGO
        elif choice.lower() == "hacker_space" or choice.lower() == "hacker space":
            print("launching hack.exe")
            time.sleep(1)
            Hacker(user_name, role)
        # Dead-End
        elif choice.lower() == "gym":
            print("launching gym.exe")
            time.sleep(1)
            Gym(user_name)
        # Rage Quit
        elif choice.lower() == "quit":
            # Maybe try again?
            print("Play Again?")
            inp = input("> ")
            # Good. Continue.
            if inp.lower() == "yes" or inp.lower() == "y":
                game()
            # Hard Rage Quit ?!?!
            else:
                print("Disconnected.")
                exit(1)
        # Went into Dead End
        print("\nGo somewhere else?")
        choice = input("> ")


if __name__ == "__main__":
    game()