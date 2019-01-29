# I need a clear function so that the output looks clean
import os
import time

class School:
    def __init__(self, user):
        class_prompt = input("Enter School (Y/N)\n> ")
        prompt = True
        if class_prompt.lower() == "y":
            in_school(user)
        elif class_prompt.lower() == "n":
            out_school(prompt)

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
    "1: AP Learning to Save People by Kiritsugu Emiya and guest staring Shirou Emiya",
    "2: AP Reading Farenheit 451 with Enji Todoroki",
    "3: How to create over 9000 memes and mistakes by Akira Toriyama",
    "4: How to inject memes in original stories to write original stories by Linkuriboh"
]

social_studies_lis = [
    "1: AP History of All Might with All Might",
    "2: AP History of Heroes with All might",
    "3: AP Law with Phoenix Right",
    "4: History of Egypt with the Joseph Joestar"
]

science_lis = [
    "1: AP Biology",
    "2: AP Chemistry",
    "3: AP Physics"
]

def math_choice():
    print("First up, Math. Pick your math class.")
    mat = class_pick(math_lis)
    return mat

def english_choice():
    print("\nNext up, English. Pick your English class.")
    eng = class_pick(english_lis)
    return eng

def social_studies_choice():
    print("\nNext up, Social Studies. Pick your Social Studies class.")
    ss = class_pick(social_studies_lis)
    return ss

def science_choice():
    print("\nNext up, Science. Pick your Science class.")
    sci = class_pick(science_lis)
    return sci

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def in_school(user):
    print("You are in school.")
    launch_school_exe()

def launch_school_exe():
    clear()
    print("You are a new student at your school. Your guidance counselor asks you to pick your classes.\n")
    math = math_choice()
    english = english_choice()
    social_studies = social_studies_choice()
    science = science_choice()
    clear()
    print("""
    Your classes are:

    English: {}
    Math: {}
    Social Studies: {}
    Science: {}
    """.format(english, math, social_studies, science))
    time.sleep(2)

def class_pick(lis):
    subject_bool = True
    choice = 1
    index = 0
    bool_2 = True
    while subject_bool:
        print("\n".join(sorted(lis)))
        prompt = input("Choice: ")
        if int(prompt) >= 1 and int(prompt) <= len(lis):
            while bool_2:
                if int(prompt) == int(choice):
                    print("Console: Added {}".format(lis[index][3:len(lis[index])]))
                    subject = lis[index][3:len(lis[index])]
                    subject_bool = False
                    bool_2 = False
                choice = choice + 1
                index = index + 1
            if "AP" in subject:
                print("Good Pick!")
        else:
            clear()
            print("Bad input. Type in the corresponding number.\n")
    # clear()
    return subject

def out_school(prompt):
    if prompt == True:
        print("school.exe: Access Denied.\n\nExiting...")
        exit()
    else:
        print("Exiting school.exe")
        time.sleep(1)