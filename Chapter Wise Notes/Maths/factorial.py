print("__________________________________________________________________________________________________")
print()
def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)

print()
c = int(input("Enter the number witch factorial you want\n"))
print()
d = fact(int(c))
print("~~~~~~~~~~~~~~~~~~~")
print(d)        
print("__________________________________________________________________________________________________")