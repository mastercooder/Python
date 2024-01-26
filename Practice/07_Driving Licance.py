print("-------------------------------------------------------------------")
print()
print("Driving Eligibility")
print("--------------------")
print()
print("If is shows None then you are eligible for driving but you need to have your Driving Licence.")
print()
myDuct = {
    1: "You are under age for driving , You cannot drive",
    2: "You are under age for driving , You cannot drive",
    3:"You are under age for driving , You cannot drive",
    4:"You are under age for driving , You cannot drive",
    5: "You are under age for driving , You cannot drive",
    6:"You are under age for driving , You cannot drive",
    7:"You are under age for driving , You cannot drive",
    8:"You are under age for driving , You cannot drive",
    9:"You are under age for driving , You cannot drive",
    10:"You are under age for driving , You cannot drive",
    11: "You are under age for driving , You cannot drive",
    12:"You are under age for driving , You cannot drive",
    13: "You are under age for driving , You cannot drive",
    14:"You are under age for driving , You cannot drive",
    15: "You are under age for driving , You cannot drive",
    16: "You are under age for driving , You cannot drive",
    17:"You are under age for driving , You cannot drive",
    18:"You can drive if you have your (Driving Licence)",
}

# --------------------------

print()
a = input("Enter your age\n")
a = int(a)
print()
b = print("", myDuct.get(a))
print(a)
print()
print("-------------------------------------------------------------------")
print()

print("If you want to see a sample of Driving Licence")
print("Fill The bellow requarments")
print()
print("-------------------------------------------------------------------")
dl = '''
                       
                      
                      THE UNION OF INDIA
              CHHATTISGARH STATE MOTOR DRIVING LICENCE         
           


     DL NO:<|DLNO|>                                         DOL:<|DOL|>   
     
   Valid Till:<|VL|>
   
          
                                                    DLR:<|DLR|> 
                                                   
               AUTHORISATION TO DRIVE FOLLOWING
               CLASS OF VEHICLES THROUGHOUT INDIA    
              
               
                      COV         DOI
                      LMV:       <|LMV|>                                                       MCWG:       <|MCWG|>                     
                      
                      DOB:      <|DOB|>        BG:<|BG|> 
                      
                                                                       Name: <|NAME|>
    S/D/W of: <|SDW|>
    Add:<|ADD|>
    
          
    PIN:<|PIN|>
    Signature & ID of                              Signature/Thumb 
    Issuing Authority:<|IA|>                        Impression of Holder     
'''
# --------------------------
dlno = input("ENTER YOUR DL NO HERE\n" )
dol = input("Enter your DOL here\n")
vl = input("Entet Valid Till date in DD-MM-YYYY\n")
dlr = input("Enter your DLR in DD-MM-YYYY\n")
lmv = input("Enter your LMV in DD-MM-YYYY\n")
mcwg = input("Enter your MCWG in DD-MM-YYYY\n")
dob = input("Enter your DOB in DD-MM-YYYY\n")
bg = input("Enter your BG here\n")
name = input("Enter your name with surname\n")
sdw = input("Enter your SDW of name surname\n")
add = input("Enter your addres\n")
pin = input("Enter your PIN number\n")
ia = input("Enter your IA in numbers\n")
#---------------------------
dl = dl.replace("<|DLNO|>", dlno)
dl = dl.replace("<|DOL|>", dol)
dl = dl.replace("<|VL|>", vl)
dl = dl.replace("<|DLR|>",dlr)
dl = dl.replace("<|LMV|>", lmv)
dl = dl.replace("<|MCWG|>", mcwg)
dl = dl.replace("<|DOB|>", dob)
dl = dl.replace("<|BG|>",bg)
dl = dl.replace("<|NAME|>",name)
dl = dl.replace("<|SDW|>",sdw)
dl = dl.replace("<|ADD|>",add)
dl = dl.replace("<|PIN|>",pin)
dl = dl.replace("<|IA|>",ia)
print(dl)
print()
print("-------------------------------------------------------------------")
print()