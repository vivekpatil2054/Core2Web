#python internal ans nbsp
#program1
class demo:
    def __init__(self):
        print("constructor")
demo()

#object related magic methods:
#__call__(),__init()__,__new()__

#program2
class demo:
    def __init__(self):
        print("constructor")
    def __new__(cls):
        print("memroy allocation")
        return super().__new__(cls)
    '''
    def  __call__(self):
          print("callable object")
    '''
obj = demo()
obj()

#program3
class demo:
    def __init__(self):
        print("constructor")
    def __new__(cls):
        print("memroy allocation")
        return super().__new__(cls)
    
    def  __call__(self):
          print("callable object")

#obj = type(demo).__call__(demo)
obj = demo()
obj()

#program4
class demo:
    def __init__(self):
        print("constructor")
    def __new__(cls):
        print("memroy allocation")
        return super().__new__(cls)
    
    def  __call__(self):
          print("callable object")

obj = type(demo).__call__(demo)
#obj = demo()
obj()

#object related magic methods:
#__del__(),__str()__,__repr__()

#program5
class demo:
    def __init__(self):
        print("constructor")
    def ___del__(self):
        print("deleting object..")
    def fun(self):
        print("In fun")
obj = demo()
obj.fun()

#program6
class demo:
    def __init__(self):
        print("constructor")
    def ___del__(self):
        print("deleting object..")
    def fun(self):
        print("In fun")
obj = demo()
obj.fun()
obj.__del__

#program7
class demo:
    def __init__(self):
        print("constructor")
    def ___del__(self):
        print("deleting object..")
    def fun(self):
        print("In fun")
obj = demo()
obj.fun()
obj.__del__
del obj

#porgram8
class demo:
    def __init__(self):
        print("constructor")
    def ___del__(self):
        print("deleting object..")
    def fun(self):
        print("In fun")
obj = demo()
obj.fun()
obj.__del__
del obj
obj.fun()

#program9
class demo:
    def __init__(self):
        print("constructor")
    def ___del__(self):
        print("deleting object..")
    def fun(self):
        print("In fun")
obj1 = demo()
obj2 = demo()
obj1.fun()
del obj1
obj2.fun()

#program10
class demo:
    def __init__(self):
        print("constructor")
    def ___del__(self):
        print("deleting object..")
    def fun(self):
        print("In fun")
obj1 = demo()
obj2 = demo()
obj1.fun()
del obj1
obj2.fun()

#program11
class demo:
    def __init__(self):
        print("constructor")
obj1 = demo()
print(obj1)

#program12
class demo:
    def __init__(self):
        print("constructor")
    def __str__(self):
        print("In str")
        return super().__str__()
    
obj1 = demo()
print(obj1)

#program13
class demo:
    def __init__(self):
        print("constructor")
    def __str__(self):
        print("In str")
        return super().__str__()
    def __repr__(self):
        print("In repr")
    
obj1 = demo()
print(obj1)

#program14
class demo:
    def __init__(self):
        print("constructor")
    def __str__(self):
        print("In str")
        return super().__str__()
    def __repr__(self):
        print("In repr")
        return "value"
    
obj1 = demo()
print(obj1)

#program15
class demo:
    def __init__(self):
        print("constructor")
    def __str__(self):
        print("In str")
        return super().__str__()
    '''
    def __repr__(self):
        print("In repr")
        return "value"
    '''
    
obj1 = demo()
print(obj1)

#program16
class demo:
    def __init__(self):
        print("constructor")

    def __str__(self):
        print("In str")
        return super().__str__()
    
    def __repr__(self):
        print("In repr")
        return super().__repr__(self)
obj1 = demo()
print(obj1)


#program17
class demo:
    def __init__(self):
        print("constructor")

    def __str__(self):
        print("In str")
        return super().__str__()
    
    def __repr__(self):
        print("In repr")
        return super().__repr__(self)
obj1 = demo()
print(obj1)
obj1
print("End code")

#program18
class demo:
    def __init__(self):
        print("constructor")

    def __str__(self):
        print("In str")
        return super().__str__()
    
    def __repr__(self):
        print("In repr")
        return super().__repr__(self)
obj1 = demo()
print(obj1)
obj1
print("End code")

#program19
class demo:
    def __init__(self):
        print("constructor")

    def __str__(self):
        print("In str")
        return super().__str__()
    
    def __repr__(self):
        print("In repr")
        return super().__repr__(self)

obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)

#program20
class demo:
    def __init__(self):
        print("constructor")

    def __str__(self):
        print("In str")
        return super().__str__()
    
    def __repr__(self):
        print("In repr")
        return super().__repr__(self)

obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)
listobj = [obj1.onj2]
print(listobj)

#program21
class demo:
    def __init__(self):
        print("constructor")

    def __iter__(self):
        print("In str")
        return self
    
    def __next__(self):
        print("In repr")
        raise StopIteration
obj = demo()
for i in obj:
    print(i)
obj = [10,20,30,40,50]
for i in obj:
    print(i)
iterobj = obj.__iter__
while True:
    try:
        print(iter.__next__)
    except StopIteration:
        break

    


    












