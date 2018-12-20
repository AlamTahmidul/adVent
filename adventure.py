import sys
import os
from school import School
from gym import Gym
from restaurant import Restaurant

def main():
    game()

def game():
    alive = True
    while alive:
        # print("Name: ")
        user_name = raw_input("Name: ")
        print("Hello, " + user_name + ".")
        print("Where would you like to go today?" + ": ")
        print("Your choices are: School, Gym, and Restaurant")
        choice = raw_input("Go To: ")
    
        # User Choice
        if choice.lower() == "school":
             print("You are in school.")
             School(user_name)
        if choice.lower() == "gym":
            print("Welcome to the Gym. Let's get hyped.")
            Gym(user_name)
            #alive = False
        elif choice.lower() == "restaurant":
            print("You are feeling hungry. Time to eat!")
            Restaurant(user_name)

if __name__ == "__main__":
    main()