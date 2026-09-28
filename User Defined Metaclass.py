#program1
class demo:
    def __init__(self):
        print("demo constructor")
obj1 = demo()
obj2 = demo()
print(obj1 is obj2)

#program2
class demo:
    def __init__(self):
        print("demo constructor")
    def __new__(cls,*args,**kwargs):
        print("demo new memory")
        super().__new__(cls)
obj1 = demo()
obj2 = demo()
print(obj1 is obj2)

#program3
class demo:
    def __init__(self):
        print("demo constructor")
    def __new__(cls,*args,**kwargs):
        print("demo new memory")
        return super().__new__(cls)
obj1 = demo()
obj2 = demo()
print(obj1 is obj2)

#program4
class demo:
    def __init__(self):
        print("demo constructor")
    def __new__(cls,*args,**kwargs):
        print("demo new memory")
        #return super().__new__(cls)
obj1 = demo()
obj2 = demo()
print(obj1 is obj2)

#program5
class demo:
    demoInstance =  0
    def __init__(self):
        print("demo constructor")
    def __new__(cls,*args,**kwargs):
        print("demo new memory")
        if cls.demoInstance is None:
            cls.demoInstance = super().__new__(cls)
            return cls.demoInstance
obj1 = demo()
obj2 = demo()
print(obj1 is obj2)

#program6
class demo:
    demoInstance =  0
    def __init__(self):
        print("demo constructor")
    def __new__(cls,*args,**kwargs):
        print("demo new memory")
        # if cls.demoInstance is None:
        #     cls.demoInstance = super().__new__(cls)
        #     return cls.demoInstance
obj1 = demo()
obj2 = demo()
obj3 = demo()
obj4 = demo()
obj5 = demo()
print(obj1 is obj2)

#program7
class demo:
    demoInstance =  0
    def __new__(cls,*args,**kwargs):
        print("demo new memory")
        if cls.demoInstance is None:
            cls.demoInstance = super().__new__(cls)
            return cls.demoInstance
obj1 = demo()
obj2 = demo()
print(obj1 is obj2)

#program8
class demo:
    demoInstance =  0
    def __new__(cls,*args,**kwargs):
        print("demo new memory")
        if cls.demoInstance is None:
            cls.demoInstance = super().__new__(cls)
            return cls.demoInstance
obj1 = demo()
obj2 = demo()
obj3 = demo()
print(obj1 is obj2)
print(obj1 is obj3)

#program9
class demo:
    demoInstance = 0
    def __new__(cls,*args,**kwargs):
        if cls.demoInstance < 2:
            cls.demoInstance = cls.demoInstance + 1
            return super().__init__(cls)
        else:
            print("object restricted")
obj1 = demo()
obj2 = demo()
obj3=  demo()
print(obj1 is obj2)
print(obj2 is obj3)

#program10
class demo:
    demoInstance = 0
    def __new__(cls,*args,**kwargs):
        if cls.demoInstance < 2:
            cls.demoInstance = cls.demoInstance + 1
            return super().__init__(cls)
        else:
            print("object restricted")
obj1 = demo()
obj2 = demo()
obj3=  demo()
print(obj1)
print(obj2)
print(obj3)
print(obj1 is obj2)
print(obj2 is obj3)

#program11
class demo:
    def __init__(self):
        print("demo constructor")
    def __new__(cls,*args,**kwargs):
        print("In memory allocation")
        super().__init__(cls)
    def __call__(self):
        print("In call method")
obj1 = demo()
obj1()


