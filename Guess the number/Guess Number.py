import random
randNum= random.randint(1, 100)
player = None
guess= 0
while(player!=randNum):
    guess+=1
    player = int(input("Please choose a number between 1 to 100:\n"))
    if (player==randNum):
        print("You Won!")
    elif (player<=randNum):
        print("Please choose greater number.")
    else:
        print("Please choose smaller number.")
print(f"You guess total {guess} times.")