class School:
    def __init__(self, user):
        class_prompt = raw_input("Enter School (Y/N): ")
        if class_prompt.lower() == "y":
            in_school(user)
        elif class_prompt.lower() == "n":
            out_school(user)

def in_school(user):
    print("You are in school")
    
def out_school(user):
    print("You left school.")