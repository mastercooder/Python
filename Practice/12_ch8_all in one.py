import random

a = input("Enter your name \n")
 

def nam():
    b = " How are you"
    return b

def mult(num1 ,num2):
    c = (num1 * num2)
    return c
  
      
print()   
print(f"Hello {a} {nam()} ")


print()    
print(sum)
print()

print("-------------------------------------------------------------------")
print()
print("You got a goldon Chance to win some products do you are intrested")
q3 = input("Y/N: ")
print()


if q3 == "Y" or q3 == "y":
    print("Congratulations! You are amongst the selected few to be eligible for a pre-approved personal Care offer. You won a Louttry ticket You can win Car, Mobile, Gold and lot more.")
else:
    print("You are missing a good chance")
print()


print("You want to participate in a lauttry.")
q4 = input("Y/N: ")


UserName = random.randint(1,999)
Password = random.randint(1,999999)


if q4 == "Y" or q4 == "y":
    print(f'''wealcome
Username - {a}{UserName}
Password - {Password}
    ''')
else:
    print(f"Thanks for comming {a} ")

# q5 = input("Eneter Username: \n")
q6 = int(input("Eneter the password: \n"))
print()

print(UserName)
if Password == q6:
    print("Correct password press Enter to continu")
else:
    print("Correct passwors press Back and fill the form continue.")
print()
input("")
print()
print("-------------------------------------------------------------------")
print()
louttry = ['Gold','Car', 'Iphone 13 pro max', 'Laptop',  'Cup', 'Bathroom Fittings',  'Bathroom Mats',  'Bathroom Mirrors', 'Linen Closet & Towel Rails', 'Bath Tubs',  'Wash Basins',
'Soap Dispensers & Sets Brushes', 'Brooms & Mops']

win = random.choice(louttry)

print(f"You win {win} ")
print()
print("-------------------------------------------------------------------")
import random 
print()
print("If you have win a grand prize then CONGACHULATION! and if you have not win then you have a chance to win")
print()
print("If you want to win BitCoin then you can try now.")
q7 = input("Do you want Y/N: ")

if q7 == "Y" or q7 == "y":
    print(f'''
WEALCOME 
UserName - {a}{UserName}
Password - {Password}   
PRESS ENTER TO CONTINUE.
''')
else:
    print("Thanks for comming.")
    
input(" ")


print()

myDict = {
    1: "2000mhs",
    2: "2500mhs",
    3: "3000mhs",
}
print()
print(list(myDict.keys()))
print()
print("Chose any one.")
q8 = int(input())
print()
print(f"You have chosen {q8} and you got") 
print(myDict.get(q8))
print()

print("Do you want to mine BitCoin?")
q9 = input("Y/N: ")
print()

if q9 == "Y" or q9 == "y":
    print("Press Enter")
else:
    print("Thanks for comming.")

print()
print()
input(" ")
print()
print("____________________________________________________________________________________________________________________________________________") 
print()
print("Witch cripto do you want to mine")  
print()

myDict2 = {
    "BITCOIN": "Here is your link - https://b.tc/conference/registration?gclid=CjwKCAiAl-6PBhBCEiwAc2GOVIKbRL55wpkgmMzqIeP_ns_RNpVAqCEC5QPcrmXkZ9uhAz-fALnNHhoCROIQAvD_BwE",
    "EITHAREUM": "Here is your link - https://b.tc/conference/registration?gclid=CjwKCAiAl-6PBhBCEiwAc2GOVIiyrCCNjv9T-hdWjcVha7dTsqASP_m2eG-tJPj8TQ0YYqyHJapWsxoCYCYQAvD_BwE",
    "DOGECOIN": "Here is your link - https://dogecoin.com/",
    "TETHER": "Here is your link -  https://b.tc/conference/registration?gclid=CjwKCAiAl-6PBhBCEiwAc2GOVL-nB7FdPh-yfBfjgSInsLF31sL9y6pHFByEEAH50jUvPitgi6kPehoCIu0QAvD_BwE",
}
print()
print("We have four BitCoies only.")
print()
print("``````````````````````````````````````````````")
print(list(myDict2.keys()))
print("``````````````````````````````````````````````")
print()    
q10 = input("Enter the name: ")  
print()
print(myDict2.get(q10))        
print()
print("-------------------------------------------------------------------")
print()
