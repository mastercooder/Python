print("This is anuther way to read a txt file.")
print()
with open('awsample.txt', 'r') as z:
    a = z.read()
print(a)
print()
# -------------------------
print("This is another way to write a txt file")
print()
with open('awSample2.txt','w') as z:
    a = z.write("It is also working like fist sample2.txt file")
print(a)
print()
    