class Gym():
    def __init__(self, choice):
        choice()
    
    def choice(self):
        doneG = True
        if doneG:
            doneG = False
            class_prompt = input("Do you want to run on the treadmill? (Y/N) :")
        
        if class_prompt.lower() == "n":
            class_prompt = input("Would you like to leave the gym? (Y/N) :")
            
        if class_prompt.lower() == "y":
            print("You left gym.")