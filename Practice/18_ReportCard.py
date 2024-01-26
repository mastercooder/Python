class Tresult:
    def __init__(self,school):
        self.school = school
        
    def studentInfo(self):                                                                                             
        print("")                                                                             
        print("-------------------------------------------------------------------------------------------------------------------------")
        print("")
        print(f"Student's name    -  {sname}                           Class / Section -  {classs}/{section}")
        print("")
        print(f"Father's name     -  {fname}                           Admission No    -  JS0{admno}")
        print("")
        print(f"Mother's name     -  {mname}                           Date Of Birth   -  {day}/{mon}/{yer}")
        print("")
        print(f"Class Techer name -  {cname}                           House           -  {house}")
        print("")
        print("-------------------------------------------------------------------------------------------------------------------------")

tejesh = Tresult("O.P. Jindal School",)
print()
sname = input("Enter Student name: ")
fname = input("Enter Father name: ")
mname = input("Enter Mother name : ")
cname = input("Enter Class Teacher name: ")
print()
classs = input("Enter Student Class:  ")
section = input("Enter Student Section:  ")
admno = input("Enter Student Admission NO:  JS0")
day = input("DOB Day:  ")
mon = input("DOB Month:  ")
yer = input("DOB Year:  ")
house = ("Enter Student House:  ")

tejesh.studentInfo()
