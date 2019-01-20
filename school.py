# I need a clear function so that the output looks 
import os
# I am using the random library to get a random integer generator
from random import randint
import time

classes = []

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

class School:
    def __init__(self, user):
        class_prompt = raw_input("Enter School (Y/N): ")
        if class_prompt.lower() == "y":
            in_school(user) 
        elif class_prompt.lower() == "n":
            out_school(user)

def in_school(user):
    print("You are in school.")
    launch_school_exe(user)
        
    
math_lis = [
    "1: Algebra I", 
    "2: Geometry", 
    "3: Algebra II/Trig", 
    "4: AP Calculus AB", 
    "5: AP Calculus BC", 
    "6: AP Hero Academia by All Might",
    "7: Computer Science",
    "8: AP Computer Science Principles",
    "9: AP Dueling by Professor Crowler"
]
    
english_lis = [
    "1: (AP) Learning to Save People by Kiritsugu Emiya and guest staring Shirou Emiya",
    "2: (AP) Reading Farenheit 451 with Enji Todoroki",
    "3: How to create over 9000 memes and mistakes by Akira Toriyama",
    "4: How to inject memes in original stories to write original stories by Linkuriboh"
]

social_studies_lis = [
    "1: (AP) History of All Might with All Might",
    "2: (AP) History of Heroes with All might",
    "3: (AP) Law with Phoenix Right",
    "4: History of Egypt with the Joseph Joestar"
]

science_lis = [
    "1: How to effectively destroy a person's confidence in their own intelligence by Mr. Park and Mr. Grima"
]

def launch_school_exe(user):
    clear()
    print("You are a new student at your school. Your guidance counselor asks you to pick your classes.\n")
    math = math_choice()
    # print math
    english = english_choice()
    # print english
    social_studies = social_studies_choice()
    # print social_studies
    science = science_choice()
    # print science
    # classes.append(math + english + social_studies + science)
    clear()
    print math + english + social_studies + science
    time.sleep(4)

def class_pick(lis):
    subject_bool = True
    choice = 1
    index = 0
    bool_2 = True
    while subject_bool:
        print("\n".join(sorted(lis)))
        prompt = raw_input("Choice: ")
        if int(prompt) >= 1 and int(prompt) <= len(lis):
            while bool_2:
                if int(prompt) == int(choice):
                    print("Added {}".format(lis[index][3:len(lis[index])]))
                    subject = lis[index][3:len(lis[index])]
                    subject_bool = False
                    bool_2 = False
                choice = choice + 1
                index = index + 1
        else:
            clear()
            print("Bad input. Type in the corresponding number.")
    # clear()
    return subject

def math_choice():
    print("First up, Math. Pick your math class.")
    math = class_pick(math_lis)
    if math[0][0] == "(" and math[0][1] == "A" and math[0][2] == "P" and math[0][3] == ")":
        print("NICE!")
    return math
            
def english_choice():
    clear()
    print("Next up, English. Pick your English class.")
    english = class_pick(english_lis)
    return english

def social_studies_choice():
    clear()
    print("Next up, Social Studies. Pick your Social Studies class.")
    ss = class_pick(social_studies_lis)
    return ss

def science_choice():
    clear()
    print("Next up, Science. Pick your Science class.")
    science = class_pick(science_lis)
    return science
            
def out_school(user):
    print("You left school.")