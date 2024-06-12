print("-------------------------------------------------------------------")
print()
letter = '''
<|NAME|>
<|ADDRESS|>
To <|RECIPIENT|>
<|INSTITUTE|>
<|AOEI|>
<|DATE|>

Dear <|NWYWTS|>

With due respect, I want to inform you that my child (name of the child) is a student of class (state which class), of your school. Due to some health issues, my child is hospitalized and is advised to be in a doctor's surveillance for three days. All my family members are right now taking care of him/her in the hospital and we are not in a condition to send him/her to school

Therefore, I request you to please understand our situation and grant him/her leave for (mention number of days) from (start date) to (end date). I am enclosing a medical certificate from the doctor for your reference, I assure you that he/she will attend classes regularly going forward.

Thanking you.
Your Sincerely
<|SINCERELY|>

'''

name = input("Name of the sender\n")
print()
address = input("Enter your address\n")
print()
recipient = input("Enter the name Who you want to send\n")
print()
institute = input("Enter the name of the Educational Institute\n")
print()
aoei = input("Enter the Address of Educational Institute\n")
print()
date = input("Enter today's date\n")
print()
nwywts = input("Enter the Name Who you want to send\n")
print()
sincerely = input("Enter your name\n")
print()
print("-------------------------------------------------------------------")
print()
letter = letter.replace("<|NAME|>" , name)

letter = letter.replace("<|ADDRESS|>" , address)

letter = letter.replace("<|INSTITUTE|>" , institute)

letter = letter.replace("<|RECIPIENT|>" , recipient)

letter = letter.replace("<|AOEI|>" , aoei)

letter = letter.replace("<|DATE|>" , date)

letter = letter.replace("<|NWYWTS|>" , nwywts)

letter = letter.replace("<|SINCERELY|>" , sincerely)

print(letter)
print()
print("----------------------------------------------------------------")