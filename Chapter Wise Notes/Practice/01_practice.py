print()
print("------------------------------------------------------------")
print()
notice = '''
                               <|COMPANY|>
                                  NOTICE
<|DATE|>                         
                               <|HEADING|>

<|BODY|>

<|AUTHO|>
<|NAME|>


'''
company = input("Entet the name if the company/school\n")
print()
date = input("Enter date here\n")
print()
heading = input("Enter the heading of Notice\n")
print()
body = input("Enter the body of the Notice\n")
print()
autho = input("Enter the name of the Authorized signatory\n")
print()
name = input("Enter your name if not given the the Question\n")
print()


notice = notice.replace("<|COMPANY|>" , company)

notice = notice.replace("<|DATE|>" , date)

notice = notice.replace("<|HEADING|>" , heading)

notice = notice.replace("<|BODY|>" , body)

notice = notice.replace("<|AUTHO|>" , autho)

notice = notice.replace("<|NAME|>" , name)

print(notice)
print()
print("------------------------------------------------------------")
print()
chapter = '''ailing Planet: the Green Movement's Role' by Nani Palkhiwala is an enlightening treatise on environmental degradation, the causes behind, and the solutions needed to be implemented to save our ailing planet. The line from the chapter 'Forests precede mankind deserts follow' has been written to bring people's attention to the fact how crucial trees are for mankind. This line means before God put man on earth, he put trees on it to create wholesome and hospitable conditions for him and his posterities; however, man in his recklessness destroys trees and makes lands barren like deserts; in such conditions mankind also disappears.

To sum up, the line means trees are indispensable for mankind to survive; in their absence, mankind will dwindle away
'''
print(len(chapter))
print()
print("-----------------")
print()
print(chapter.replace("a", "aa"))
print()
print("-----------------")
print()
print(chapter.endswith(""))
print()
print("-----------------")
print()
print(chapter.count(" "))
print()
print("-----------------")
print()
print(chapter.capitalize())
print()
print("-----------------")
print()
print(chapter.find("in"))
print()
print("-------------------------------------------------------------------")

print("DISTANCE:- KM TO M")
print()
a = input("Enter KM here\n")
b = 1000

a = int(a)
b = int(b)

dis = (a * b)
print("Here is your Meater\n" , dis)
print()
print("-------------------------------------------------------------------")
print()
print("DISTANCE:- M TO KM")
print()
a = input("Enter M here\n")
b = 1000

a = int(a)
b = int(b)

dis = (a / b)
print("Here is your KM\n" , dis)
print()
print("-------------------------------------------------------------------")
print()