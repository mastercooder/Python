name = input("Enter your name\n")
print()
print(f"Hello {name} How are you")
print()
print("---------------------------------------------------------------------")
print()
if 'jayesh' in name.lower():
    print(f"Hay {name} you are noob with 6GB ram mobile")
elif 'tejesh' in name.lower():
    print(f"Hay {name} is very pro player")
else:
    print(f"The name {name} is not registerd in the list")
print()
print("---------------------------------------------------------------------")
print()
print("If you want to make a TXT file then I can help you with that.")
print()
q1 = input("Enetr name of the file: ")
print()
q2 = inout("Enter what you want to type in the {q1}.txt file: ")
print()

with open(f'{q1}.txt','r') as f:
    file1 = f.read()
print(file1)

with open(f'{q1}','w') as w:
    file2 = w.write(f'{q2}')

print()
print(f'''
Now If you want to see the what is written in {q1}.txt fiel then press Enter.
''')
print()
print()
input("")
print()
with open(f'{q1}') as r:
    open = r.read()
print(open)