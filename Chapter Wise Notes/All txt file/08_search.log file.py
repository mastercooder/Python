with open('log.txt') as f:
    content = f.read()
    
if 'python' in content.lower():
    print("Python is presant")
else:
    print("Python is not presant")
    