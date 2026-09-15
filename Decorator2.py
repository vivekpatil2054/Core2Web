#program1
def fun():
    print("In fun")
fun()

#program2
def decorfun(funref):
    def innerfun():
        print("start deocration")
        funref()
        print("end decoration")
    return innerfun
def fun():
    print("In fun")
fun()

#program3
def decorfun(funref):
    def innerfun():
        print("start deocration")
        funref()
        print("end decoration")
    return innerfun
@decorfun
def fun():
    print("In fun")
fun()

#program4
def decorfun(funref):
    def innerfun():
        print("start deocration")
        funref()
        print("end decoration")
    return innerfun
#@decorfun
def fun():
    print("In fun")
fun()

#program5
def subscriptionapp(subappref):
    def quizattempt():
        print("attempting quiz for subscription")
        subappref()
        print("win competition and get netflix subscription")
        return quizattempt
@subscriptionapp
def subscription():
    print("netflix")
subscription()

#program6
def decorfun(funref):
    def innerfun():
        print("start decoration")
        funref()
        print("end decoration")
    return innerfun
#@decorfun
def fun():
    print("In fun")
fun = decorfun(fun)
fun()

#program7
def decorfun(funref):
    def innerfun():
        print("start decoration")
        funref()
        print("end decoration")
    return innerfun
#@decorfun
def fun():
    print("In fun")
fun = decorfun(fun)
print(fun)

#program8
def decorfun(funref):
    def innerfun():
        print("start decoration")
        funref()
        print("end decoration")
    return innerfun
#@decorfun
def fun():
    print("In fun")
fun = (fun.__closure__)
print(fun)

#program9
def decorfun(funref):
    def innerfun():
        print("start decoration")
        #funref()
        print("end decoration")
    return innerfun
#@decorfun
def fun():
    print("In fun")
fun = decorfun(fun)
print(fun)

#program10
def add(x,y):
    print("add:",x+y)
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
add(num1,num2)

#program11
def add(x,y):
    print(x)
    print(y)
    print("add:",x+y)
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
add(num1,num2)

#program12
def add(x,y):
    print("x:",x)
    print("y:",y)
    print("add:",x+y)
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
add(num1,num2)

#program13
def add(x,y):
    print("x:",x)
    print("y:",y)
    print("add:",x+y)
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
add(y = num1,x = num2)

#program14
def decorfun(funref):
    def innerfun(*args,**kwargs):
        print("start decoration")
        funref(*args,**kwargs)
        print("end deocration")
    return innerfun
@decorfun
def add(x,y):
    print("y:",y)
    print("add:",x+y)
add(10,20)

#program15
tplobj = (10,20,30)
print(tplobj)
print(type(tplobj))

#program16
tplobj = (10,20)
print(tplobj)
print(type(tplobj))
x,y = tplobj
print(x)
print(y)

#program17
def decorfun(funref):
    def innerfun(*args,**kwargs):
        print("start decoration")
        funref(*args,**kwargs)
        print("end deocration")
    return innerfun
#@decorfun
def add(x,y):
    print("y:",y)
    print("add:",x+y)
add = decorfun(add)
add(10,20)

#program18
def decorfun(funref):
    def innerfun(*args,**kwargs):
        print("start decoration")
        funref(*args,**kwargs)
        print("end deocration")
    return innerfun
@decorfun
def add(x,y):
    print("y:",y)
    print("add:",x+y)
add = decorfun(add)
add(y=50,x=20)

#program18
def decorfun(funref):
    def innerfun(*args,**kwargs):
        print("start decoration")
        funref(*args,**kwargs)
        print("end deocration")
    return innerfun
@decorfun
def add(x,y):
    print("y:",y)
    print("add:",x+y)
add = decorfun(add)
add(5,7,y=50,x=20)

#Multiple Deocorator

#program1
def decorfun1(funref1):
    def innerfun1():
        print("start decoration")
        funref1()
        print("end decoration")
    return innerfun1
def decorfun2(funref2):
    def innerfun2():
        print("start decoration")
        funref2()
        print("end decoration")
    return innerfun2
@decorfun1
@decorfun2
def fun():
    print("In fun")
fun()

#program2
def decorfun1(funref1):
    def innerfun1():
        print("start decoration")
        funref1()
        print("end decoration")
    return innerfun1
def decorfun2(funref2):
    def innerfun2():
        print("start decoration")
        funref2()
        print("end decoration")
    return innerfun2
# @decorfun1
# @decorfun2
def fun():
    print("In fun")
fun = decorfun1(decorfun2(fun))
fun()

#program3
def decorfun1(funref1):
    def innerfun1():
        print("start decoration")
        funref1()
        print("end decoration")
    return innerfun1
def decorfun2(funref2):
    def innerfun2():
        print("start decoration")
        funref2()
        print("end decoration")
    return innerfun2
# @decorfun1
# @decorfun2
def fun():
    print("In fun")
#fun = decorfun1(decorfun2(fun))
fun()

#program4
def decorfun1(funref1):
    def innerfun1():
        print("start decoration")
        funref1()
        print("end decoration")
    return innerfun1
def decorfun2(funref2):
    def innerfun2():
        print("start decoration")
        funref2()
        print("end decoration")
    return innerfun2
# @decorfun1
# @decorfun2
retinner2 = decorfun2(fun)
print(retinner2.__closure__)
retinner1 = decorfun1(retinner2)
print(retinner1.__closure__)
retinner1()

#program5
def add(x,y):
    print("In add")
    return x+y
retval = add(10,50)
print(retval)

#program6
def decorfun(funref):
    def innerfun(*args):
        print("start decor1")
        retval = funref(*args)
        print("end decor2")
        return retval 
    return innerfun
@decorfun
def add(x,y):
    print("In add")
    return x+y
retval = add(10,50)
print(retval)












