rows = 5

for i in range(rows):
    for j in range(rows-i):
        print(" ", end=" ")
    
    for j in range(2*i-1):
        print("*", end=" ")
    print()