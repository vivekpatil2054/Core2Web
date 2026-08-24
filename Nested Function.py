#Function Interals and Inner Interals

#Program1:
'''
def fun():
    print("In fun")
print(type(fun))
'''
x = 10
print(x)    
y  =  x
print(y)
print(id(x))
print((y))

#program2
def fun():
    print("In fun")
print(fun)

print(type(fun))
x =  10
print(x)
print(type(x))

#program3
def fun():
    print("In fun")

print(id(fun))
print(fun)
print(type(fun))

#program4
def fun():
    print("In fun")
print(hex(id(fun)))
print(fun)
print(type(fun))

#Nested Function

#program1
def outerfun():
    print("In outer function")
    def innerfun():
        print("In inner function")
outerfun()

#program2
def outerfun():
    print("In outer function")
    def innerfun():
        print("Inner function")
    innerfun()    

outerfun()

#program3
def outerfun():
    print("In outer function")
    def innerfun():
        print("Inner function")
    innerfun() 
    print("End User")   

outerfun()

#program4
def outerfun():
    print("In outer function")
    def innerfun1():
        print("In Inner1 function")
    def innerfun2():
        print("In Inner2 function")
    innerfun1()
    innerfun2()
    print("End user")
outerfun()

#program5
def outerfun():
    print("In outer function")
print(outerfun)

#program6
def outerfun():
    print("In outer function")
    def innerfun():
        print("In Inner function")
    print(innerfun)
print(outerfun)

#program7
def outerfun():
    print("In outer function")
    def innerfun():
        print("In Inner function")
    print(innerfun)
print(outerfun)
outerfun()

#program8
def outerfun():
    print("In outer function")
    def innerfun():
        print("In Inner function")
    print(innerfun)
    print(innerfun)
print(outerfun)
outerfun()

#program9
def outerfun():
    print("In outer function")
    x = 20
    def innerfun():
        print("In inner function")
    innerfun()
    return outerfun()

#program10
def outerfun():
    print("In outer function")
    x = 20
    def innerfun():
        print("In inner function")
    innerfun()
    return outerfun()
retval = outerfun
print(retval)

#program11
def outerfun():
    print("In outer function")
    x = 20
    def innerfun():
        print("In inner function")
    innerfun()
    return outerfun()
retval = outerfun()
retval()

#program12
def outerfun():
    print("In outer function")
    x = 20
    def innerfun():
        print("In inner function")
    innerfun()
    return outerfun()
retval = outerfun()
print(type(outerfun))

#program13
def outerfun():
    print("In outer function")
    x = 20
    def innerfun():
        print("In inner function")
    innerfun()
    return outerfun()
retval = outerfun()
print(retval)

#program14
def outerfun():
    print("In outer function")
    def innerfun1():
        print("In inner1 function")
    def innerfun2():
        print("In inner2 function")
    return innerfun1,innerfun2
retval = outerfun()
print(retval)

#program15
def outerfun():
    print("In outer function")
    def innerfun1():
        print("In inner1 function")
    def innerfun2():
        print("In inner2 function")
    return innerfun1,innerfun2
retval = outerfun()
print(type(retval))

#program16
def outerfun():
    print("In outer function")
    def innerfun1():
        print("In inner1 function")
    def innerfun2():
        print("In inner2 function")
    return innerfun1,innerfun2
retval = outerfun()
for data in retval:
    data()

#program17
def outerfun():
    print("In outer function")
    def innerfun1():
        print("In inner1 function")
    def innerfun2():
        print("In inner2 function")
    return innerfun1,innerfun2
retval1,retval2 = outerfun()
retval1()
retval2()








