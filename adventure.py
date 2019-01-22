import os
from school import School, clear
# from gym import Gym
from hackers import Hacker
import time

roles = ["Hacker", "Student", "Investor"]
play_again = ["yes", "no", "n", "y"]

def display_user(user_name, role):
    print("""
User: {}
Role: {}
        """.format(user_name, role))

def game():
    clear()
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
    clear()
    alive = True
    print("""
     _________________________________________________________________________________________________________________________
    |   Welcome to New York, the city filled with hopes and dreams for every hacker, student, and investor.                   |
    |   You are living in Manhattan where every opportunity makes you $$$. It is your duty to live your life                  |
    |   fully, and make the best decisions.                                                                                   |
    |                                                                                                                         |
    |   WARNING: YOU WILL BE HELD RELIABLE FOR ALL YOUR CHOICES. IF YOU ARE NOT A GOOD BOY, PREPARE TO FACE THE CONSEQUENCES. |
    |_________________________________________________________________________________________________________________________|
    """)
    time.sleep(3)
    user_name = input("Username: ")
    # class_choice = input()
    password = input("Password: ")
    role = input("Choose Your Role: ")
    if role in roles:
        display_user(user_name, role)
    else:
        print("Invalid Role. Default role of 'student' selected.")
        role = "Student"
        display_user(user_name, role)
    time.sleep(1)
    print("\nLogged in.")
    time.sleep(2)
    clear()
    print("\nHello, " + user_name + ".")
    print("\nWhere would you like to go today?")
    choice = input("> ")
    while True:
        if choice.lower() == "school":
             print("launching school.exe")
             time.sleep(3)
             School(user_name)
             continue
        # if choice.lower() == "gym":
        #     print("launching gym.exe")
        #     time.sleep(3)
        #     Gym(user_name)
        #     continue
        elif choice.lower() == "hacker_space" or choice.lower() == "hacker space":
            print("launching hack.exe")
            time.sleep(3)
            Hacker(user_name, role)
            continue
        elif choice.lower() == "quit":
            print("Play Again?")
            inp = input("> ")
            if inp.lower() == "yes" or inp.lower() == "y":
                game()
            else:
                print("Disconnecting...")
                time.sleep(2)
                exit(1)
        print("\nGo somewhere else?")


if __name__ == "__main__":
    game()
