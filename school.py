import os
from random import randint

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
    # choice = round(randint(1, 2))
    # # print choice
    # if choice == 1:
    #     launch_bully_exe(user)
    # else:
    launch_school_exe(user)
        
# def launch_bully_exe(user):
#     print("Execute bully.exe")
    
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
    "1: (AP) Learning to Save People by Kiritsugu Emiya",
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
    # print("Execute school.exe")
    clear()
    print("You are a new student at your school. Your guidance counselor asks you to pick your classes.\n")
    math = math_choice()
    english = english_choice()
    social_studies = social_studies_choice()
    science = science_choice()
    

def math_choice():
    print("First up, Math. Pick your math class:")
    math_bool = True
    while math_bool:
        print("\n".join(sorted(math_lis)))
        prompt = raw_input("Choice: ")
        if int(prompt) >= 1 and int(prompt) <= len(math_lis):
            if int(prompt) == 1:
                print("Added Algebra I")
                math = "Algebra I"
                math_bool = False
            elif int(prompt) == 2:
                print("Added Geometry")
                math = "Geometry"
                math_bool = False
            elif int(prompt) == 3:
                print("Added Algebra II/Trigonometry")
                math = "Algebra II/Trigonometry"
                math_bool = False
            elif int(prompt) == 4:
                print("Added AP Calculus AB")
                math = "AP Calculus AB"
                math_bool = False
            elif int(prompt) == 5:
                print("Added AP Calculus BC")
                math = "AP Calculus BC"
                math_bool = False
            elif int(prompt) == 6:
                print("Added AP Hero Academia")
                math = "AP Hero Academia"
                math_bool = False
        else:
            print("Type in the corresponding number.")
    return math
            
def english_choice():
    print("Next up, English. Pick your English class:")
    english_bool = True
    while english_bool:
        print("\n".join(sorted(english_lis)))
        prompt = raw_input("Choice: ")
        if int(prompt) >= 1 and int(prompt) <= len(english_lis):
            if int(prompt) == 1:
                print("Added (Regents) English")
                english = "(Regents) English"
                english_bool = False
            elif int(prompt) == 2:
                print("Added (AP) English")
                english = "(AP) English"
                english_bool = False
            elif int(prompt) == 3:
                print("Added (AP) Learning to Save People")
                english = "(AP) Learning to Save People"
                english_bool = False
        else:
            print("Type in the corresponding number.")
    return english
    
def social_studies_choice():
    print()
    return social_studies
    
def science_choice():
    
    print()
    return science
            
def out_school(user):
    print("You left school.")