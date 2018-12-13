import sys
import os
import school.py, gym.py, restaurant.py

def main():
    user_name = input("Pick a Name: ")
    print("Hello, " + user_name + ".")
    print("Where would you like to go today?" + ": " )
    print("Your choices are: School, Gym, and Restaurant")
    choice = input()

    # User Choice
    if choice.lower() == "school":
        print("You are in school.")
        school()
    elif choice.lower() == "gym":
        print("Welcome to the Gym. Let's get hyped.")
        gym()
    elif choice.lower() == "restaurant":
        print("You are feeling hungry. Time to eat!")
        restaurant()


if __name__ == "__main__":
    main()
