#Nested Function

#program1
def fun(x,y):
    print(x)
    print(y)
    return x+y
retval = fun(10,20)
print(retval)

#program2
def fun(x,y):
    print(x)
    print(y)
    return x+y
fun(10,20)

#program3
def fun(x,y):
    print(x)
    print(y)
    return x+y
print(fun(10,20))

#program4
def add(x,y):
    return x+y
print(add(10,20))

def add(x,y):
    return x+y
ret = lambda x,y:x+y
add(10,20)
ret(30,40)

#program5
def add(x,y):
    return x+y
print(add(10,20))

def add(x,y):
    return x+y
ret = lambda x,y:x+y
print(add(10,20))
data = ret(30,40)
print(data)

#program6
mult = lambda a,b:a*b
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
print(mult(x,y))

#program7
def mult(a,b):
    return a*b
xyz = mult
xyz(5,3)

#program8
mult = lambda a,b :print("In mult")
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
mult(x,y)
#print(mult(x,y))

#program9
def mult(a,b):
    return a*b
xyz = mult
xyz(5,3)

#program8
mult = lambda a,b :print("In mult"),#print("go to hell")
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
mult(x,y)
#print(mult(x,y))

#program9
def add(a,b):
    return a+b
add = lambda x,y:x+y
print(add(10,20))

#program10
def add(a,b):
    print("In add")
    return a+b
add = lambda x,y:x+y
print(add(10,20))

#call by value

#program1
def fun(x):
    print("In fun before: ",x)
    x = 30
    print("In fun after: ",x)
x = 10
print("global before:",x)
fun(x)
print("global after:",x)

#program2
def fun(a):
    print("In fun before: ",a)
    a = 30
    print("In fun after: ",a)
x = 10
print("global before:",x)
fun(x)
print("global after:",x)

#program3
def fun(x,y):
    print("fun data",x,y)
    x = 50
    y = 100
    print("fun data after update:",x,y)
x = 10
y = 20
print("main data:",x,y)
fun(x,y)
print("main data after fun call:",x,y)

#call by reference
#program1
def fun(listobj):
    print("In fun:",listobj)
listobj = [10,20,30,40,50]
print("In main:",listobj)
fun(listobj)

#program2
def fun(listobj):
    print("In fun:",listobj)
    listobj[2] =  70
    print("In fun after update:",listobj)
listobj = [10,20,30,40,50]
print("In main:",listobj)
fun(listobj)
print("In main after fun call:",listobj)




