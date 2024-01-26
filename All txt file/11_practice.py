import random

name = input("Emter your name \n")
print(f"Hello {name} how are you.")
print()

q1 = input("Enter the text which you want to put in a txt file: \n")

with open('public.txt','w') as f:
    pub = f.write(q1)
    


    