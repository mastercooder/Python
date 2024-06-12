class Movie:
    def __init__(self, tname, name, time, state, location):
        self.tname = tname
        self.name = name
        self.time = time
        self.state = state
        self.location = location
         
    def movieInfo(self):
        print("")
        print("----------------------------------------------")
        print("")
        print(f"The name of the Movie Theater is: {self.tname}")
        print(f"The name of the Movie is: {self.name}")
        print(f"The Time of the movie is: {self.time} Minutes")
        print("")
        print("----------------------------------------------")
        
    def movieLocation(self):
        print("")
        print(f"The stare is: {self.state}")
        print(f"Movie lacation: {self.location}")
        print("")
        print("----------------------------------------------")
        
    def movieTicket(self):
        print("")
        print(f"The name of the Ticket holdet is {name}")
        print(f"The number of the seat is {q4}")
        print("")
        print("----------------------------------------------")
        
    def totalCost(self):
        print("")
        print("")
        print("----------------------------------------------")
        print("")
        print(f"The total cost is {myDict.get(q4)}")    
        print("")
        print("----------------------------------------------")
          
myDict = {
1 : "Rs 500",
2 : "Rs 400",
3 : "Rs 300",
4 : "Rs 200",
5 : "Rs 200",
6 : "Rs 200",
7 : "Rs 200",
8 : "Rs 200",
9 : "Rs 200",
10 : "Rs 200",
}


moviee = Movie("Galaxy", "SPYDER MAN no way home", 200, "Chhattisgath", "Raigarh")
print()
print("TODAYS FILM")
print("_______________")
print()
moviee.movieInfo()           
moviee.movieLocation()            
print("")
print("------------------------------------------------------")
print("")
print(f"Do you want to Book a Movie ticket")
print()
q1 = input("Y/N: ")
q1 = q1.capitalize()
if q1=="Y":
    print("Press Enter")
elif q1=="N":
    print("Thanks For Comming")
else:
    print("Please Enter Y for Yes or N for No")
    
print()
q2 = input("   ")
print()
print("------------------------------------------------------")
print()
name = input("Enter your name: ")
print()
print("-------------------------------------")
print(list(myDict.keys()))
print("-------------------------------------")
print()
print("------------------------------------------------------")
print()
q4 = int(input("Which site do you want to Book: "))
print()
print(f"Here is your cost {myDict.get(q4)}")
print()
print("------------------------------------------------------")
print()
print("HERE IS YOUR TICKET")
print("---------------------")
print()
moviee.movieInfo()

moviee.movieTicket()

moviee.totalCost()



          