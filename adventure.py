import sys
import os
# from school.py import School
from gym import Gym
# from restaurant.py import Restaurant

def main():
    print("Pick a Name: ", end="")
    user_name = input()
    print("Hello, " + user_name + ".")
    print("Where would you like to go today?" + ": " )
    print("Your choices are: School, Gym, and Restaurant")
    choice = input()

    # User Choice
    # if choice.lower() == "school":
    #     print("You are in school.")
    #     school()
    if choice.lower() == "gym":
        print("Welcome to the Gym. Let's get hyped.")
        Gym()
    # elif choice.lower() == "restaurant":
    #     print("You are feeling hungry. Time to eat!")
    #     restaurant()


if __name__ == "__main__":
    main()
