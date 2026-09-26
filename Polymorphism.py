#Method Overloading
#program1
class demo:
    def __init__(self):
        print("demo constructor")
    def disp(self):
        print("demo first disp")
    def disp(self):
        print("demo second disp")
obj = demo()
obj.disp()

#program2
class demo:
    def __init__(self):
        print("demo constructor")
    def disp(self,*args):
        print("demo first disp")
    def disp(self,*args):
        print("demo second disp")
obj = demo()
obj.disp(10)
obj.disp(20,30)

#Method Overriding
#program3
class parent:
    def __init__(self):
        print("parent constrctor")
    def career(self):
        print("doctor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("child constrctor")
obj = demo()
obj.career()

#program4
class parent:
    def __init__(self):
        print("parent constrctor")
    def career(self):
        print("doctor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("child constrctor")
    def career(self):
        print("youtuber")
obj = demo()
obj.career()

#program5
class parent:
    def __init__(self):
        print("parent constrctor")
    def career(self,x):
        print("doctor")
class child(parent):
    def __init__(self,a,b):
        super().__init__()
        print("child constrctor")
    def career(self):
        print("youtuber")
obj = demo()
obj.career(20,30)

#Abstract Classes
#program6
from abc import abstractmethod,ABC

class Parent():
    def __init__(self):
        print("parent constructor")
    def career(self):
        print("doctor")
    @abstractmethod
    def marry(self):
        pass
obj = parent()

#program7
class Parent(ABC):
    def __init__(self):
        print("parent constructor")
    def career(self):
        print("doctor")
    @abstractmethod
    def marry(self):
        pass
class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")
    def marry(self):
        print("disha patni")
obj = child()
obj.career()
obj.marry()

#Interfaces
#program8
from abc import ABC

class parent(ABC):
    def __init__(self):
        print("parent constructor")
class parent2():
    def __init__(self):
        print("parent2 constructor")
print(type(parent))
print(type(parent2))

#program9
from abc import ABCmeta

class parent(metaclass=ABCmeta):
    def __init__(self):
        print("parent constructor")
class parent2():
    def __init__(self):
        print("parent2 constructor")
print(type(parent))
print(type(parent2))

#program10
from abc import ABCmeta

class parent(metaclass=ABCmeta):
    def __init__(self):
        print("parent constructor")
class parent2():
    def __init__(self):
        print("parent2 constructor")
parent()
parent2()
print(type(parent))
print(type(parent2))


