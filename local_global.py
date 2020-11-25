x = 2
y = 0

def g():
    global x,y

def adder():
    g()
    x = 3
    y = 1
    x = x + y
    
print(x)        
adder()
print(x)