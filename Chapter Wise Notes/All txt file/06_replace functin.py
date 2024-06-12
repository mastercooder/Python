with open('replace.txt') as f:
    a = f.read()
    
a = a.replace("donkey", "************")
a = a.replace("losser", "*********")
a = a.replace("never", "*********")

with open('replace.txt','w') as f:
    f.write(a)
    