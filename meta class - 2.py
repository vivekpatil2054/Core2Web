#program1
class demo:
    def __init__(self):
        print("constructor")
    def __new__(cls):
        print("memory allocation")
obj1 = demo()
obj2 = demo()

#program2
class demo:
    def __init__(self):
        print("constructor")
    def __new__(cls):
        print("memory allocation")
obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)

#program3
class demo:
    def __demo__(self):
        print("constructor")
    def __new__(cls):
        print("memory allocation")
    def __call__(cls,*args,**kwargs):
        print("call method")
obj1 = demo()
print(obj1)
obj1()

#program4
class demo:
    def __demo__(self):
        print("constructor")
    def __new__(cls):
        print("memory allocation")
    def __call__(cls,*args,**kwargs):
        print("call method")
obj1 = demo()
print(obj1)
obj1()

#program5
class parent:
    def __init__(self):
        print("constructor")
    def __new__(cls,*args,**kwargs):
        print("memory allocation")
    def __call__(cls,*args,**kwargs):
        print("parent call method")
obj = parent()
'''
parent().type(parent).__call__(parent).type.__call__(parent)
parent.__new__(parent)
parent.__init__(obj)
'''

#program6
class demo:
    instance = None
    def __new__(cls,*args,**kwargs):
        if cls.instance is None:
            print("memory allocatipn")
            cls.instance = super().__new__(cls)
        return cls.instance
obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)

#program7
class demo:
    instance = None
    def __init__(self):
        print("constructor")
    def __new__(cls,*args,**kwargs):
        if cls.instance is None:
            print("memory allocatipn")
            cls.instance = super().__new__(cls)
        return cls.instance
obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)

#program8
class demo:
    instance = None
    def __init__(self):
        if not self.intialized:
            print("constructor")
            self.intialized = True
    def __new__(cls,*args,**kwargs):
        if cls.instance is None:
            print("memory allocatipn")
            cls.instance = super().__new__(cls)
        return cls.instance
obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)

#program9
class singletonmeta(type):
    instance = None
    def __call__(cls,*args,**kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args,**kwargs)
        return cls.instance
class demo:
    def __init__(self):
        print("constructor")
obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)

#program10
class singletonmeta(type):
    instance = None
    def __call__(cls,*args,**kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args,**kwargs)
        return cls.instance
class demo(metaclass = singletonmeta):
    def __init__(self):
        print("constructor")
obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)

#program11
class singletonmeta(type):
    instance = None
    def __call__(cls,*args,**kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args,**kwargs)
        return cls.instance
class demo:
    def __init__(self):
        print("constructor")
obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)
print(type(demo))

#program12
class singletonmeta(type):
    instance = None
    def __call__(cls,*args,**kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args,**kwargs)
        return cls.instance
class demo:
    def __init__(self):
        print("constructor")
class demochild(demo):
    def __init__(self):
        print("demochild constructor")
obj1 = demo()
obj2 = demo()
print(obj1)
print(obj2)
print(type(demo))
print(type(demochild))

