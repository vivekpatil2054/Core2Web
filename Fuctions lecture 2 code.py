#1
def fun():
    print("In fun")
print("start code")
fun()
fun()
print("End code")    

#2
def fun(x,y):
    ans = x + y
    return ans
retval = fun(10,20)
print(retval)

# #3
def add(x,y):
    ans = x + y
    return ans
data1 = int(input("Enter the value: "))
data2 = int(input("Enter the value: "))
retval = add(data1,data2)
print(retval)

# #4
def fun():
    print("In fun")
    return 10
x = fun()
print(x)

# #5
def fun():
    print("In fun")
retval = fun()
print(retval)

#6
def fun():
    print("In fun")
    return 10
    print("End code")
retval = fun()
print(retval)

#7
def addmul(x,y):
    add = x + y
    mul = x * y
    return add,mul
retval = addmul(10,20)
print(retval)

#8
def addmul(x,y):
    add = x + y
    mul = x * y
    return add,mul
retval1,retval2 = addmul(10,20)
print(retval1)
print(retval2)

#9
def fun(x):
    print("In fun")
fun(10)

#10
def fun(x):
    print("In fun")
x = 50
print(type(x))
y = "kahna"
print(type(y))
fun(10)

#11
def fun(x):
    print("In fun")
x = 50
print(type(x))
y = "kahna"
print(type(y))
z = 50
print(type(z))
fun(10)

#12
def fun(x):
    print("In fun")
x = 50
print(type(x))
y = "kahna"
print(type(y))
z = 50
print(type(z))
fun(10)
print(id(x))
print(id(y))
print(id(z))

#13
def fun(x):
    print("In fun")
x = 257
print(type(x))
y = "kahna"
print(type(y))
z = 257
print(type(z))
fun(10)
print(id(x))
print(id(y))
print(id(z))

#Function as on object

#1
def fun():
    print("In fun")
print(type(fun))

#2
def fun():
    print("In fun")
print(type(fun))
fun()
fun.___call__()
fun.___call__()

#3
def fun():
    print("In fun")
def gun():
    print("In gun")
def run():
    print("In run")
fun()
gun()
run()

#4
def fun1():
    print("In fun1")
def fun2():
    print("In fun2")
def fun3():
    print("In fun3")
fun1()
fun2()
fun3()






