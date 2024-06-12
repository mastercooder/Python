class Student:
    name = "Tejesh"
    rollno = 41
    classt = "XI"
    section = "H"
    contactno = 9109325767
    
    def genralInfo(self):
        print("-----------------------------------------------------------------------")
        print("")
        print(f"Student Name:    {self.name}")
        print(f"Class:           {self.classt}")
        print(f"Section:         {self.section}")        
        print(f"Roll NO:         {self.rollno}")
        print(f"Contact NO:      {self.contactno}")
        print("-----------------------------------------------------------------------")
        print("")
       
    @classmethod     
    def changeName(cls, nam):
        cls.name = nam      
        
    def changeRollno(cls, rol):
        cls.rollno = rol
        
    def changeClasst(cls, cla):
        cls.classt = cla
        
    def changeSection(cls, sec):
        cls.section = sec
        
    def changeContactno(cls, con):
        cls.contactno = con
        
s = Student()
s.genralInfo()
print()
print("If you want to change any information enter Y bellow")
c1 = input("Y/N:  ")
c1 = c1.capitalize()
print()
if c1=="Y":
    print('''
         Example
        ---------
1: First enter catagre
Eg- For changeing the name enter: name

2: Then enter replacing word
Eg- For replacing the name from Tejesh enter: Jayesh

3: If you want to edit multiple please enter m bellow
       
    ''')
    print()
    c2 = input("Enter the categress:  ")
    c2 = c2.lower()
    print()
    c3 = input("Enter the replacing word: ")
    c3 = c3.upper()
    print()
else:
    None
    
if c2=="name":
    s.changeName(c3)
    s.genralInfo()
elif c2=="roll no":
    s.changeRollno(c3)
    s.genralInfo()
elif c2=="class":
    s.changeClasst(c3)
    s.genralInfo()
elif c2=="section":
    s.changeSection(c3)
    s.genralInfo()
elif c2=="contact no":
    s.changeContactno(c3)
    s.genralInfo()    
else:
    print("Please enter a valid name") 

   