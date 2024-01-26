'''
This Code is wirten by Master Coder

Note:-

You can make changes and make it as your wish.
This code is a formate of NOTICE.

'''
#----------------------------------------------------------------------------------------X X X-------------------------------------------------------------------------------#

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