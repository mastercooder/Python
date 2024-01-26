print()
print("----------------------------------------------------------------")
print()
a1 = input("Enter your name: \n")
print()
print("Hellow " + a1)
print('''
I am the developer of this side.
Thanks for comming to this side.
This is a trusted webside.
It is also verifird with government.
''')

print("If you want a lauty ticket", a1)
print()
l1 = input("yes or no:\n")
print()

if l1=="yes":
    print('''You selected yes.
    Your Password is 701155
     ''')
else:
    print("Thanks for comming")

l2 = int(input("Enter the password: \n"))

if l2== 701155:
    lou = "Correct Password."
else:
    lou = "Incorrect Password."
    
print("You Enterd " + lou)
print()
print("----------------------------------------------------------------")
myDict = {
    "BHTYN509K": "BEAST OF LUCK NEXT TIME",
    "PTYRT890L": "BEAST OF LUCK NEXT TIME",
    "VHYFD648J": "CONGRACHULATIONS YOU WON THE FIRST PRIZE",
    "JYTEH903M": "BEAST OF LUCK NEXT TIME",
    "JGRTE001Z": "BEAST OF LUCK NEXT TIME",
    "JFUYI900P": "CONGRACHULATIONS YOU WON THE SECOND PRIZE",
    "JHRUO530X": "BEAST OF LUCK NEXT TIME",
    "KOYRP764C": "CONGRACHULATIONS YOU WON THE THIRD PRIZE",
    "TORFT589N": "BEAST OF LUCK NEXT TIME",
    "GJDYR843N": "BEAST OF LUCK NEXT TIME",
}
print("----------------------------------------------------------------")
print()
print("Now you are going to see the ticket.")
print()
print("WARNING")
print('''
1) If you will select more then one ticket you will be discolified.
2) If you will select enter any spelling Earror then you will discolidied.
3) Enter the name of the ticket exactly the same in capial.
''')
print()
print("----------------------------------------------------------------")
print(list(myDict.keys()))
print()
print("Fill the detailes carefully")
print()

m1 = input("Enter your name: \n")
#m2 = input("Enter your name: \n")
#m3 = input("Enter your name: \n")
#m4 = input("Enter your name: \n")
#m5 = input("Enter your name: \n")
#m6 = input("Enter your name: \n")
#m7 = input("Enter your name: \n")
#m8 = input("Enter your name: \n")
#m9 = input("Enter your name: \n")
#m10 = input("Enter your name: \n")

l3 = input("select any ticket and enter it: \n")
d1 = print("", myDict.get(l3))
