print("----------------------------------------------------------------")
print()
print("You Have to enter your all 5 subject marks and then you will get your result pass or fail")
print()
# --------------------------
num1 = int(input("Enter your First Subject marks here:\n"))
num2 = int(input("Enter your Second Subject marks here:\n"))
num3 = int(input("Enter your Theard Subject marks here:\n"))
num4 = int(input("Enter your Fourth Subject marks here:\n"))
num5 = int(input("Enter your Fifth Subject marks here:\n"))
print()
# --------------------------
if(num1<33 or num2<33 or num3<33 or num4<33 or num5<33):
    print("You are fail due to less then 33% in an individual subject.")
elif(num1+num2+num3+num4+num5)/5 < 40:
    print("You are fail due to less then 40% overall")
else:
    print("PASS")
    
print("----------------------------------------------------------------")
print()
print("If You want to know your grade then enter your ovear all persentage down")

m1 = int(input("Enter your persentage here: \n"))

if m1>=90:
    grade = "A++"
elif m1>=80:
    grade = "A"
elif m1>=70:
    grade = "B"
elif m1>=60:
    grade = "C"
elif m1>=50:
    grade = "D"
elif m1>=40:
    grade = "E"
else:
    grade: "F"

print("Your Grade is " + grade)
print()
print("----------------------------------------------------------------")