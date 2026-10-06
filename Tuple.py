#program1
tplobj = (10,20,30,40)
print(tplobj)
print(type(tplobj))

#parenthesis
#program2
tplobj1 = ()
print(tplobj1)
print(type(tplobj1))

#Packing
#program3
x = 10,20,30,40
print(x)
print(type(x))

#Single element tuple
#program4
tplobj2 = (10)
#tplobj2 = (10,)
print(tplobj)
print(type(tplobj2))

#Empty tuple
#program5
tplobj3 = tuple()
print(tplobj3)
print(type(tplobj3))

#Using constructor
#program6
tplobj4 = tuple(10,20,30,40)
#tuple([10,20,30])
print(tplobj4)
print(type(tplobj4))

#program7
tplobj4 = tuple("shashi")
#tuple([10,20,30])
print(tplobj4)
print(type(tplobj4))

#Tuple Packing
#program8
tplobj1 = 10,20,30
print(tplobj1)
print(type(tplobj1))

#Tuple Unpacking
#program9
tplobj1 = (10,20,30)
a,b = tplobj1
print(tplobj1)
print(type(tplobj1))
#unpacking
print(a)
print(b)

#program10
tplobj1 = (10,[20,30])
a,b = tplobj1
print(a)
print(b)

#Swapping
#program11
tplobj1 = 10,20,30
print(tplobj1)
print(type(tplobj1))
a,b,c,d = tplobj1
print("original value of a:",a)
print("original value of b:",b)
print(c)
print(d)
print("**post swapping**")
a,b = c,d
print("swapped value of a:",a)
print("swapped value of b:",b)
print(c)
print(d)

#Extended Unpacking
#program12
tplobj1 = 10,20,30
print(tplobj1)
print(type(tplobj1))
a,b,c,d = tplobj1
print("original value of a:",a)
print("original value of b:",b)
print(c)
print(d)
print("**post swapping**")
a,b = c,d
print("swapped value of a:",a)
print("swapped value of b:",b)
print(c)
print(d)
print("**extended unpacking**")
x,*y = tplobj1
print(x)
print(y)
print(type(tplobj1))
print(type(tplobj1))

#program13
def fun(*args):
    print(args)
    print(type(args))
    fun(10,20,30,40)

#Indexing
#program14
tplobj = (10,20,30,40)
print(tplobj[2])

#program15
tplobj = (10,20,30,40)
print(tplobj[2])
print(tplobj[:2:2])
print(tplobj[::-2])

#Nested tuple
#program16
tplobj = ((10,20,30,40),50)
print(tplobj[1])
print(tplobj[2])
print(tplobj[3])

#Immutability
#program17
tplobj = (10,"kanha",20.5,True,10)
print(tplobj)
tplobj[1] = "badhe"
print(tplobj[1])

#program18
tplobj1 = (10,"kanha",20.5,True,10)
print(tplobj1)
tplobj1[1] = "badhe"
print(tplobj1[1])
try:
    tplobj1[1] = "badhe"
except TypeError as e:
    print(e)
print(tplobj1)

#Mutable object inside tuple
#program19
tplobj2 = (10,20,30,[40,50],60)
print(tplobj2)
print(tplobj2[1])
print(tplobj2[3])
print(tplobj2[3][1])
tplobj2[3[1]] = 55
print(tplobj2[2])

#program20
tplobj2 = (10,20,30,[40,50],60)
print(tplobj2)
print(tplobj2[1])
print(tplobj2[3])
print(tplobj2[3][1])
tplobj2[3[1]] = 55
print(tplobj2[2])
tplobj2[3] = (45,55,65)
print(tplobj2)
print(tplobj2)

#Tuple with function
#program21
def fun(*args):
    print(args)
    print(id(args))

#program22
def fun(*args):
    print(args*2)
    print(type(args))
    fun(10,20,30,40)

#Tuple Method
#program23
tplobj = (10,20,30,40,10)
print(tplobj)
tplobj.append(50)

#Count and Index
#program24
tplobj = (10,20,30,40,10)
print(tplobj.count(10))
print(tplobj.index(30))
print(tplobj.index(10))
print(tplobj.index(10,1))

#Bulit-In Methods:Len(),Min(),Max(),Sum()

#program25
tplobj5 = (10,20,30,40,50)
tplobj(len(tplobj5))
tplobj(min(tplobj5))
tplobj(max(tplobj5))
tplobj(sum(tplobj5))

#Named tuple
#program26
from collections import namedtuple

tplobj5 = (10,20,30,40,50)
emp = namedtuple("emoplyee",["empid","empsal"])

#emp = namedtuple("empolyee",["empid","empsal","empname"])
obj = emp(10,20.5)
#obj = emp(10,"kanha",20.5)
print(obj.empid)
#print(obj.empname)
print(obj.empsal)
print(type(emp))
print(type(obj))

