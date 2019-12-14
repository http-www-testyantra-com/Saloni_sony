# method with same name will override the previous method that was present with same name

def add(a,b):
    return a+b  #30-output
print(add(10,20))
def add(a,b,c):
    return a+b+c
print(add(10,20))   #add() missing 1 required positional argument: 'c'