import random

def Game(comp, you):
    if (comp==you):
     return None
    elif (comp=="s"):
        if (you== "p"):
            return True
        elif (you =="sc"):
            return False
    elif (comp=="p"):
        if (you== "sc"):
            return True
        elif (you =="s"):
            return False
    
    elif (comp=="sc"):
        if (you== "s"):
            return True
        elif (you =="p"):
            return False

print("Computer Choose from Stone (s), Paper (p), Scissor (sc):\n")
randomNo = random.randint(1, 3)
if(randomNo==1):
    comp = "s"
elif(randomNo==2):
    comp = "p"
else:
    comp = "sc"

you= input("Choose one: Stone (s), Paper (p), Scissor (sc):\n")

a = Game(comp, you)

print(f"Computer Choose {comp}")
print(f"Player Choose {you}")

if a==None:
    print("Match Tie")
elif a==True:
    print("Player Won!")
else:
    print("Player Lose.")