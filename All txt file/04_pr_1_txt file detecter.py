with open('twinkal twinkal.txt','r') as f:
    t = f.read()
if 'twinkal' in t:
    print("Twinkal is present in twinkal twinkal txt file")
else:
    print("Twinkal is not  present in twinkal twinkal txt file")