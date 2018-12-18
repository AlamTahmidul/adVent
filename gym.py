class Gym:
    def __init__(self, user):
        class_prompt = raw_input("Enter Gym (Y/N) :")
        if class_prompt.lower() == "y":
            in_gym(user)
        elif class_prompt.lower() == "n":
            out_gym(user)

def in_gym(user):
    choice = raw_input("Do you want to run on the treadmill? (Y/N) :")
    if choice.lower() == "n":
        choice = raw_input("Would you like to leave the gym? (Y/N) :")
        if choice.lower() == "y":
            out_gym(user)
    elif choice.lower() == "y":
        print("You are on a treadmill. How long do you want to run? (in minutes) : ")
        tread_inp = raw_input()
        treadmill(tread_inp, user)
    
def treadmill(tread_inp, user):
    print("{} was on the treadmill for {} hours".format(user, tread_inp))

def out_gym(user):
    class_choice = raw_input()
    if class_choice.lower() == "y":
        print("{} left gym. {} lost their wallet on the way home.".format(user, user))
        print("You have encountered a robber running away with your wallet. What do you do? (Type help for options)")
        class_prompt = raw_input()
        
    while class_choice.lower() == "help":
        print("1: Run after him with your cane.")
        print("2: Call your parents and cry.")
        print("3: Tactically advance and attempt to retrieve your wallet.")
        class_prompt = raw_input()
    
    if class_prompt.lower() == "1":
        print("You ran after him but could not quite catch up to him. Instead, he was hit by a car.")
    elif class_prompt.lower() == "2":
        print("Your parents call you pathetic and tell you to man up and solve your own problems.")
    elif class_prompt.lower() == "3":
        print("FREE RAM")