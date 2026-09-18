#program1
class demo:
    pass
obj = demo()

#program2
class demo:
    def ___new__(cls):
        print("memory allocation")
        return super().__new__(cls)

    def __init__(self):
        print("In constructor")

obj = demo()
#init = __new__(demo)
#__init__(obj)

#program3
class demo:
    def ___new__(cls):
        print("memory allocation")
        return super().__new__(cls)
    '''
    def __init__(self):
        print("In constructor")
    '''
obj = demo()
#init = __new__(demo)
#__init__(obj)

#program4
class demo:
    def ___new__(cls):
        print("memory allocation")
    
    def __init__(self):
        print("In constructor")
    
obj = demo()
#init = __new__(demo)
#__init__(obj)

#program5
class player:
    team = "india"
    def __new__(cls):
        print("memory allocation")
        super().__new__(cls)
    def __init__(self):
        self.playername = "virat"
        self.jerno = 18
        print("constructor")
print(globals())

#program6
class player:
    team = "india"
    def __new__(cls):
        print("memory allocation")
        super().__new__(cls)
    def __init__(self):
        self.playername = "virat"
        self.jerno = 18
        print("constructor")
print(globals())
print(player.__dict__)

#program7
class player:
    team = "india"
    def __new__(cls):
        print("memory allocation")
        super().__new__(cls)
    def __init__(self):
        self.playername = "virat"
        self.jerno = 18
        print("constructor")
print(globals())
print(player.__dict__)
print(obj.__dict__)

#program8
class demo:
    x  = 10
    def __init__(self):
        print("In constructor")
obj = demo()

#program9
class demo:
    x  = 10
    def __init__(self):
        print("In constructor")
obj = demo()
print(obj.x)

#program10
class demo:
    x  = 10
    def __init__(self):
        print("In constructor")
obj = demo()
print(obj.x)
print(demo.__dict__)

#program11
class demo:
    x = 10
    def __init__(self):
        print("In constructor")

        self.a = 20
        self.b = 30
obj = demo()
print(demo.x)
print(obj.x)
print(obj.a)
print(obj.b)
print(demo.a)
print(demo.b)

#program12
class demo:
    x  = 10
    def __init__(self):
        self.x = 20
obj = demo()
print(obj.x)
print(demo.x)

#program13
class demo:
    x  = 10
    def __init__(self):
        self.x = 20
        self.y = 30
obj = demo()
print(obj.x)
print(demo.x)

#program14
class demo:
    x  = 10
    def __init__(self):
        self.x = 20
        self.y = 30
obj = demo()
print(obj.x)
print(demo.x)
print(obj.y)

#program15
class demo:
    x  = 10
    y = 50
    def __init__(self):
        self.x = 20
        self.y = 30
obj = demo()
print(obj.x)
print(demo.x)
print(obj.y)

#program16
class demo:
    x = 10
    def __init__(self):
        print("constructor")
obj1 = demo()
obj2 = demo()

#program17
class demo:
    x = 10
    def __init__(self):
        print("constructor")
obj1 = demo()
obj2 = demo()
print(obj1.x)
print(obj2.x)
obj1.x = 50
print(obj1.x)
print(obj2.x)

#program18
class demo:
    x = 10
    def __init__(self):
        print("constructor")
obj1 = demo()
obj2 = demo()
print(obj1.x)
print(obj2.x)
obj1.x = 50
print(obj1.x)
print(obj2.x)
print(obj1.__dict__)
print(obj2.__dict__)

#program19
class demo:
    x = 10
    def __init__(self):
        print("constructor")
obj1 = demo()
obj2 = demo()
print(obj1.x)
print(obj2.x)
demo.x = 50
print(obj1.x)
print(obj2.x)
print(obj1.__dict__)
print(obj2.__dict__)

#program20
class employee:
    def __init__(self):
        self.empid = 10
        self.emmpname = "kanha"
obj1 = employee()
obj2 = employee()
print(obj1.empid)
print(obj1.empname)
print(obj2.empid)
print(obj2.empname)

#program21
class employee:
    def __init__(self,empid, empname):
        self.empid = empid
        self.emmpname = empname
obj1 = employee(10,"kanha")
obj2 = employee(15,"ashish")
print(obj1.empid)
print(obj1.empname)
print(obj2.empid)
print(obj2.empname)

#program22
class employee:
    def __new__(cls,*args,**kwargs):
        print("memory allocation")
        return super().__new__(cls)
    def __init__(self,empid, empname):
        self.empid = empid
        self.emmpname = empname
obj1 = employee(10,"kanha")
obj2 = employee(15,"ashish")
print(obj1.empid)
print(obj1.empname)
print(obj2.empid)
print(obj2.empname)

#program23
class employee:
    def __new__(cls,*args,**kwargs):
        print("memory allocation")
        return super().__new__(cls)
    def __init__(self,empid, empname):
        print("constructor")
        self.empid = empid
        self.emmpname = empname
obj1 = employee(10,"kanha")
obj2 = employee(15,"ashish")
print(obj1.empid)
print(obj1.empname)
print(obj2.empid)
print(obj2.empname)

#program24
class employee:
    '''
    def __new__(cls,*args,**kwargs):
        print("memory allocation")
        return super().__new__(cls)
    '''    
    def __init__(self,empid, empname):
        print("constructor")
        self.empid = empid
        self.emmpname = empname
obj1 = employee(10,"kanha")
obj2 = employee(15,"ashish")
print(obj1.empid)
print(obj1.empname)
print(obj2.empid)
print(obj2.empname)











