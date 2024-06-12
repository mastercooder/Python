class Science: 
    def __init__(self, name, admno, rollno, section):
        self.name = name
        self.admno = admno
        self.rollno = rollno
        self.section = section
        
    def studentInfo(self):
        print("---------------------------------------")
        print(f"Name of the student {self.name}")
        print(f"Student Adm No. {self.admno}")
        print(f"Student Roll No {self.rollno}")
        print(f"Student Section {self.section}")
        print("---------------------------------------")
    def studentMarks(self):
        print(f"English Subject number {m1}")
        print(f"Math Subject number {m2}")
        print(f"Physics Subject number {m3}")
        print(f"Chemistry Subject number {m4}")
        print(f"IP Subject number {m5}")
        print("----------------------------------")
        print("")
        print(f"Total {a1}")
        print("")
        print("----------------------------------")
        
jayesh = Science("Jayesh", "JS07574", 26, "G")
    
def average(a, b, c, d, e):
    a = (a + b + c + d + e)/5
    return a
print()
print("Science Candidwte")
print("_____________________")
print()
m1 = int(input("Enter Your English Subject Marks\n"))
m2 = int(input("Enter Your Math Subject Marks\n"))
m3 = int(input("Enter Your Physics Subject Marks\n"))
m4 = int(input("Enter Your Chemistry Subject Marks\n"))
m5 = int(input("Enter Your Hindi Subject Marks\n"))
print()
a1 = average(m1, m2, m3, m4, m5)
print()
jayesh.studentInfo()
print()
jayesh.studentMarks()
print()
print("------------------------------------------------------")
print()

class Commerse: 
    def __init__(self, name, admno, rollno, section):
        self.name = name
        self.admno = admno
        self.rollno = rollno
        self.section = section
        
    def studentInfo(self):
        print("---------------------------------------")
        print(f"Name of the student {self.name}")
        print(f"Student Adm No. {self.admno}")
        print(f"Student Roll No {self.rollno}")
        print(f"Student Section {self.section}")
        print("---------------------------------------")
        
    def studentMarks(self):
        print(f"English Subject number {m1}")
        print(f"Bussines Stides Subject number {m2}")
        print(f"Economic Subject number {m3}")
        print(f"Accounts Subject number {m4}")
        print(f"IT Subject number {m5}")
        print("----------------------------------")
        print("")
        print(f"Total {a2}")
        print("")
        print("----------------------------------")
        
tejesh = Commerse("Tejesh", "JS05095", 38, "H")
    
def average(a, b, c, d, e):
    a = (a + b + c + d + e)/5
    return a

print()
print("Commerse Student Chanse")
print("_________________________")
print()
m1 = int(input("Enter Your English Subject Marks\n"))
m2 = int(input("Enter Your Business Stides Subject Marks\n"))
m3 = int(input("Enter Your Economic Subject Marks\n"))
m4 = int(input("Enter Your Accounts Subject Marks\n"))
m5 = int(input("Enter Your IT Subject Marks\n"))
print()
a2 = average(m1, m2, m3, m4, m5)
print()
tejesh.studentInfo()
print()
tejesh.studentMarks()
print()
print("_____________________________________________________")
print()
print()


class School:
    def __init__(self, name, location, country):
        self.name = name
        self.location = location
        self.country = country
        
    def schoolLocation(self):
        print("------------------------------------------------------------")
        print(f"The name of the school is {self.name}")
        print(f"The locatin of the school is {self.location}")
        print(f"The School is located in {self.country} Country")
        print("-----------------------------------------------------------")
        
    def classCompraison(self):
        print(f"The class which we will compare are ITOV & Commerse")
        print("----------------------------------------------------------")
        print("")
        print(f"Science student average {a1}")
        print(f"Commerse student average {a2}")
        print("")
        print("-----------------------------------") 
    
    def classCompraisonn(self):
        if(a1>a2):
            print(f"Science student has more {sub1} Persentage")
        elif(a1<a2):
            print(f"Commerse student has more {sub2} Persentage")
        else:
            print(f"Both the student has same persentage")      

jindal = School("Jindal", "Raigarh", "India")
print()
print("COMPRASION TIME!")
print("__________________")
print()
jindal.schoolLocation()
print()
jindal.classCompraison()
print()
sub1 = (a1 - a2)
sub2 = (a2 - a1)
jindal.classCompraisonn()                                                                                   