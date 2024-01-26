import random

def gameWin(comp, you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="p":
            return True
        elif you=="si":
            return False
    elif comp=="p":
        if you=="s":
            return False
        elif you=="si":
            return True
    elif comp=="si":
        if you=="s":
            return True
        elif you=="p":
            return False
            
print()
print("---------------------------------------------------------------------------------------------")
print()
print("STONE PAPER SIGER")
print("___________________")
print()
print('''
------------------
Stone = s             
Paper = g           
Scisser = si         
------------------
''')
print()
print()
input("Press Enter to Start")
print()
print("-------------------------------------------------------")
print()
print("Computer Chance: Done")
randNo = random.randint(1, 3)
if randNo==1:
    comp = 's'
elif randNo==2:
    comp = 'p'
elif randNo==3:
    comp = 'si'
else:
    None 
    
you = input("Enter your choice: ")
a = gameWin(comp, you)
print("-------------------------------------------------------")
print()
print("----------------------")
print(f"Computer Chose: {comp}")
print(f"Your Chose: {you}")
print("----------------------")
print()
print()
print("----------------------------------")
print("----------------------------------")
if a==None:
    print("Game is Tie")
elif a:
    print("You Win!")
else:
    print("You Lose!")
print("----------------------------------")
print("----------------------------------")