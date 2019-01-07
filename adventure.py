import sys
import os
from school import School, clear
from gym import Gym
from restaurant import Restaurant

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
    |                                                                                                                         |
    |   Type on the console to continue ...                                                                                   |
    |_________________________________________________________________________________________________________________________|
    """)
    cons = raw_input()
    if cons.lower() != None:
        user_name = raw_input("Name: ")
        while alive:
            # print("Name: ")
            clear()
            print("Hello, " + user_name + ".")
            print("Where would you like to go today?")
            print("School / Gym / Restaurant")
            choice = raw_input("Go To: ")
        
            # User Choice
            if choice.lower() == "school":
                 print("You are in school.")
                 School(user_name)
                #  alive = False
            if choice.lower() == "gym":
                print("Welcome to the Gym. Let's get hyped.")
                Gym(user_name)
                # alive = False
            elif choice.lower() == "restaurant":
                print("You are feeling hungry. Time to eat!")
                Restaurant(user_name)
                # alive = False

if __name__ == "__main__":
    main()