rows = int(input("Enter how many rows you want to print: "))

# Upper half of the pyramid
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end=" ")
    for j in range(1, 2 * i):
        print("*", end=" ")
    print()

# Lower half of the pyramid
for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end=" ")
    for j in range(1, 2 * i):
        print("*", end=" ")
    print()
