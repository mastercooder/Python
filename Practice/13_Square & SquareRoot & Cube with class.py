class Calculator:
    def __init__(self, number):
        self.number = number
        
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")
    def squareRoot(self):
        print(f"The value of {self.number} squareRoot {self.number **0.5}")
    def cube(self):
        print(f"The value of {self.number} cube {self.number **3}")

print()
b = int
+(input("Enter your number\n"))                
a = Calculator(b)
a.square()
a.squareRoot()
a.cube()
        
        