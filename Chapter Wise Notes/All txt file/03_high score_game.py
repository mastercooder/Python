def game():
    return 1000

score = game()
with open('hiscore.txt') as f:
    a = f.read()
if a == '':
    with open('hiscore.txt','w') as f:
        f.write(f" {score} ")

elif int(a)<score :
    with open('hiscore.txt','w') as f:
        f.write(str(score))