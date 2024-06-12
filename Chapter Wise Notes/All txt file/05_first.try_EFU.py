a = int(input("Enter your highest score: "))

def game():
    b = 1000
    return b
    
score = game()

with open('hiscore.txt') as f:
    z = f.read()

if z == '':
    with open('hiscore.txt','w') as f:
     f.write(int(a))
elif int(z)<score:
     with open('hiscore.txt','w') as f:
         f.write(int(a))

with open('hiscore.txt') as ans:
     c = ans.read()

if int(c)>score:
     print(f'''            CONGRACHULATIONS! You Have made a new high recod.
     Old Recod = {b}
     Your Record = {c}
     ''')
elif c==score:
     print(f'''            CONGRACHULATIONS! You Have made a same high recod.
     Highest Recod = {score}
     Your Record = {a}
     ''')
else:
     print(f'''
ALL THE BEAST NEXT TIME
Highest Recod = {score} 
Your Record = {a} 
     
     ''')
     