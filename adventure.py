import sys
import os
from school import School, clear
from gym import Gym
from hackers import Hacker
import time

def main():
    game()

def game():
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
    |                                          ____ _  _ ____ ____    ____ __     __  _  _                                    | 
    |                                         (_  _( \/ (  _ ( ___)  (  _ (  )   /__\( \/ )                                   |
    |                                           )(  \  / )___/)__)    )___/)(__ /(__)\)  /                                    |
    |                                          (__) (__)(__) (____)  (__) (____(__)(__(__)                                    |
     -------------------------------------------------------------------------------------------------------------------------
""")                                                                                                                     
    raw_input()
    clear()
    alive = True
    print("""
     _________________________________________________________________________________________________________________________
    |   Welcome to New York, the city filled with hopes and dreams for every hacker, student, and investor.                   |
    |   You are living in Manhattan where every opportunity makes you $$$. It is your duty to live your life                  |
    |   fully, and make the best decisions.                                                                                   |
    |                                                                                                                         |
    |   WARNING: YOU WILL BE HELD RELIABLE FOR ALL YOUR CHOICES. IF YOU ARE NOT A GOOD BOY, PREPARE TO FACE THE CONSEQUENCES. |
    |                                                                                                                         |
    |_________________________________________________________________________________________________________________________|
    """)
    time.sleep(4)
    user_name = input("Name: ")
    class_choice = input()
    print("Hello, " + user_name + ".")
    while alive:
        # print("Name: ")
        clear()
        print("Where would you like to go today?")
        choice = raw_input("Go To: ")
        # User Choice
        if choice.lower() == "school":
             print("launching school.exe")
             time.sleep(3)
             School(user_name)
            #  exit()
             continue
        if choice.lower() == "gym":
            print("launching gym.exe")
            time.sleep(3)
            Gym(user_name)
            continue
        elif choice.lower() == "hacker_space":
            print("launching hack.exe")
            time.sleep(3)
            Hacker(user_name)
            continue

if __name__ == "__main__":
    main()