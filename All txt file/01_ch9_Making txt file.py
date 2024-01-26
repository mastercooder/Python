
print("This program is to read a txt or bineary file")
print()
f = open('sample.txt',)
data = f.read()
print(data)
f.close()
print()
# ---------------------------------------
print("This program is to write a txt or bineary file ")
print()
f = open('sample2.txt', 'w')
f.write("Does it worked")
f.close()
