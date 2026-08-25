#Local Varaible
#program1
def fun():
    x = 10
    print("In fun")
    print("fun: x",x)
fun()

#program2
x = 20
def fun():
    x = 10
    print("In fun:")
    print("In fun:,x",x)
fun()
print(x)

#program3
x = 20
y = 30
def fun():
    x = 10
    print("In fun:")
    print("In fun:,x",x)
fun()
print(x)
print(y)

#program4
x = 20
def fun():
    x = 10
    print("In fun:")
    print("In fun:,x",x)
    def gun():
        z = 30
        print("In gun, x",x)
        print("In gun z",z)
fun()
print(x)

#program5
x = 30
def fun():
    global x
    x = x + 1
    print("In fun:",x)
print(x)
fun()
print(x)

#program6
x = 10
def fun():
    global x 
    x = 20
    print("In fun")
    print("fun:",x)
print(x)
fun()
print(x)

#program7
x = 10
def fun():
    x = 20
    print("In fun")
    print("local:",x)
print(x)
fun()
print(x)

#global function

#program1
x = 30
def fun():
    print("In fun")
print(globals())

#program2
x = 10
def fun():
    x = 20
    print("In fun")
    print("local:",x)
    print("global:",globals()['x'])
print(x)
fun()
print(x)

#program3
x = 10
def fun():
    x = 20
    print("fun x:",x)
    def gun():
        global x
        x = x + 1
        print("gun x:",x)
    return gun
print(x)
retval  = fun()
retval = fun()
retval()
print(x)

#Nonlocal Keyword

#program1
x = 10
def fun():
    x = 20
    print("fun x:",x)

    def gun():
        nonlocal x
        x = x + 1
        print("gun x:",x)
    return gun
print(x)
retval = fun()
retval()
print(x)