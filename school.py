from random import randint

class School:
    def __init__(self, user):
        class_prompt = raw_input("Enter School (Y/N): ")
        if class_prompt.lower() == "y":
            in_school(user) 
        elif class_prompt.lower() == "n":
            out_school(user)

def in_school(user):
    print("You are in school.")
    choice = round(randint(1, 2))
    # print choice
    if choice == 1:
        launch_bully_exe(user)
    else:
        launch_school_exe(user)
        
def launch_bully_exe(user):
    print("Execute bully.exe")
    
def launch_school_exe(user):
    print("Execute school.exe")
    
def out_school(user):
    print("You left school.")