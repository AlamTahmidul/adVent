class Restaurant:
    def __init__(self, user):
        class_prompt = raw_input("Enter Restaurant (Y/N): ")
        if class_prompt.lower() == "y":
            in_res(user)
        elif class_prompt.lower() == "n":
            out_res(user)

def in_res(user):
    print("You are inside the restaurant. However two suspicious indivduals come before they pull out their weapons, shouting 'This is a robbery'")

def out_res(user):
    print("You exited the restaurant.")