class Train:
    def __init__(self, name, traino, seats, cost):
        self.name = name
        self.traino = traino
        self.seats = seats
        self.cost = cost
        
    def getStatus(self):
        print(f"-------------------------------------------------------------------------")
        print(f"The name of the Train is {self.name}")
        print(f"The number of the Train is {self.traino}")
        print(f"The seats Avelable are is {self.seats}")
        print("--------------------------------------------------------------------------")
    def yourDestination(self):
        print("--------------------------------------------------------------------------")
        print(f"Your Train is {c} to {d}")
        print("--------------------------------------------------------------------------")
                        
    def getCost(self):
         print("--------------------------------------------------------------------------")
         print(f"The cost of one Ticket is Rs{self.cost}")
         print("--------------------------------------------------------------------------")
         
    def bookTicket(self):
         if(self.seats>0):
             print(f"Your ticket has been bocked! Your seats number is {self.seats}")
         else:
             print("Sorry, The Train is full Please try Tatkal")     
                          
    def cansalTicket(self):
        if(ct=="Y"):
             print(f"Your Ticket has been cansaled and your Ticket number is {tn}")
             self.seats = self.seats + 1
        else:
             print(f"Engoy your Trip")


jaansatabdi = Train("Jaansatabdi", 2635700, 10, 300)

a = input("Enter your name\n")
print(f"Hello {a}")
print()
print("Do you want to book a Train Ticket")
b = input("Y/N: ")
b = b.capitalize()

if b=="Y":
    print("Press Enter")
else:
    print("Thanks For Comming")

print()
print()
input("   ")
print()

print("Enter the Derailes Below")
print()
c = input("Enter Your location\n")
d = input("Enter the Destination\n")
print()
print("---------------------------------------------------------------------------------------------------------------------------------------")
print()

jaansatabdi.bookTicket()
print()
print("HERE ARE YOUR DETAILES")
print()
jaansatabdi.getStatus()
print()
jaansatabdi.yourDestination()
print()
jaansatabdi.getCost()
print()
print("---------------------------------------------------------------------------------------------------------------------------------------")
print()
print("Do you want to cansal a Ticket: ")
ct = input("Y/N: ")
ct = ct.capitalize()
tn = input("Enter your Ticket number: ")
jaansatabdi.cansalTicket()
print()
# --------------------------------------------------------------

myDict = {
"STEHD7703L": "Beast of luck next time",
"DTYAJ8729K": "Beast of luck next time",
"TWWTE5643O": "First Prize",
"YETSJ4683Z": "Beast of luck next time",
"YRIOT9860L": "Second Prize",
"HSXEJ1038M": "Beast of luck next time",
"UFKHD9986J": "Theard Prize",
"HSKDV7378P": "Beast of luck next time",
"HSFKDU775A": "Beast of luck next time",
}
            
print("Do you want to take part in a lauttry")
print()
lau = input("Y/N: ")
lau = lau.capitalize()
if lau=="Y":
 print("Press Enter")
else:
 print("Thanks For Comming")
print()
print()
input("   ")
print()
print("Here are your ticket")
print()
print("-----------------------------------------------------------------")
print(list(myDict.keys()))
print("-----------------------------------------------------------------")
print()
print("Chose any one")
print()
print("Enter your Ans")
lau2 = input("",)
lau3 = myDict.get(lau2)
print()
print("------------------------------")
print(lau3)        