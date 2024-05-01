import random

def check(comp, user):
        if (comp == user):
            return 0
        elif (comp == 1 and user == 0):
            return -1
        elif (comp == 2 and user == 1):
            return -1
        elif (comp == 0 and user == 2):
            return -1 
        
        return 1
    

user = int(input("0 for Rock, 1 for Paper, 2 for Scissor: "))
comp = random.randint(0,2)
print(f"Computer: {comp}")


score = check(comp, user)

if (score == 0):
    print("Draw")
elif (score == -1):
    print("You Loose")
else:
    print("You Won")
    

        
