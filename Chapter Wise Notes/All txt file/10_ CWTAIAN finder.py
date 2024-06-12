file1 = "CWTAIAN.txt"
file2 = "CWTAIAN2.txt"

with open("CWTAIAN.txt") as f:
    f1 = f.read()
    
with open("CWTAIAN2.txt") as f:
    f2 = f.read()
    
if f1==f2:
    print("They are same")
else:
    print("They are not same")