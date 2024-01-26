while True:
    try:
        query = input("Enter the query number: ")
    except Exception as e:
        print("Something went wrong!")

    if "exit" in query.lower():
        print("Exiting The loop")
        break;


# Code For * Pattern
    if(query=='1') or 'pattern' in query.lower():
        print()
        print(" Code for Star pattern")
        print("-----------------------")
        print()
        rows = int(input("Enter the number of Rows you want    ||   0 to Exit: "))
        print(" ")

        if(rows==0):
            print("Exiting The Loop! ")
            continue;

        for i in range(rows):
            for j in range(rows-i):
                print(" ", end="")
            for j in range(2*i-1):
                print("*", end="")
            print()
            


    elif(query=='2'):
        print("Trying Range")
        print() 

        n = int(input("Enter the Starting Number: "))
        m = int(input("Enter the ending number: "))
        for i in range(n, m+1):
            print(i)

    elif(query=='3'):
        print()
        print("     Table    ")
        print("    --------  ")
        print()

        user = int(input("Enter the number: "))
        print()
        print("----------------------")
        for i in range(1, 11):
            print(f"{user} X {i} = {user*i}")
        print("----------------------")
        print()

    elif(query=='4'):
        print()
        column = int(input("Enter how many column you want: "))
        rows = int(input("Enter how many rows you want: "))
        print()
        word = input("Enter the word you want to summon: ")

        for i in range(1, column):
            for j in range(1, rows):
                print(f" {word} ", end="")
            print()


    else:
        print("Enter the Correct Number")

