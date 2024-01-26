a = input("Enetr the word you want to spam. \n")
b = int(input("Eneter Hoe much rous ypu want. \n"))
c = int(input('''Entet the numbet of word you want to add in each row. (SUGGESTED 100 WORDS) \n'''))
print()
print("-------------------------------------------------------------------")
print('''                               WARNING

1) If you will enter big numbers in the place in upper asked questions your system can crash.

2) If you have typed a big number like then you have a option to back the program 

3) MOBILE = 3000  
   PC = 10,000
   
If you enter more then theis then your system can cresh. 
''')
print()
print("-------------------------------------------------------------------")
print()
d = 5000
if b >= d or c >= d:
    print("If you are using Mobile. Device Can be Crash.")
else:
    print("If you You are Good to go")

print()
    
d2 = 10000
if b >= d or c >= d:
    print("Your Device Can be Crash.")
else:
    print("You are Good to go")
    print()
e = input("Press Enter to print:")
print()
print("Here is your spam")
print()
print("-------------------------------------------------------------------")
print()

for i in range(b):
    for z in range(c):
        print(f"{a} ", end="")
    z+=1
    print()
print("-------------------------------------------------------------------")
print()