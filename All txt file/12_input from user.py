

#name = input("Emter your name \n")
#print(f"Hello {name} how are you.")
#print()

#q1 = input("Enter the text which you want to put in a txt file: \n")

#with open('public.txt','w') as f:
#    pub = f.write(q1)

#print()    
#with open('public.txt') as f:
#    ans = f.read()
#print(ans)

print("If you want to name a file on your name")
print()
q2 = input("What will be your file name: \n")
q3 = input("What you want to enter in the txt file: \n")

with open(f"{q2}",'w') as y:
    filen = y.write(q3)
    
with open(f"{q2}",'r') as y:
    filex = y.read()
    
print()
print(filex)   