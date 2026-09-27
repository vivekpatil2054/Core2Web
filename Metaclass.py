#program1
from abc import ABC,abstractmethod

class parent(ABC):
    def __init__(self):
        print("parent constructor")
    #@abstractmethod
    def fun(self):
        pass
obj = parent()

#program2
from abc import ABC,abstractmethod
class parent(ABC):
    def __init__(self):
        print("parent constructor")
    #@abstractmethod
    def fun(self):
        pass
class child:
    pass

obj = parent()

#program3
from abc import ABC,abstractmethod
class parent(ABC):
    def __init__(self):
        print("parent constructor")
    #@abstractmethod
    def fun(self):
        pass
class child:
    pass

obj = parent()
print(type(parent))
print(type(child))

#program4
from abc import ABC,abstractmethod
class parent():
    def __init__(self):
        print("parent constructor")
    @abstractmethod
    def fun(self):
        pass
class child:
    pass

parent()
child()
print(type(parent))
print(type(child))

#program5
class demo:
    pass
demo()
print(type(demo))

#program6
class demo:
    pass
class memo:
    pass
demo()
memo()

#program7
from abc import abstractmethod,ABCMeta

class demo(meta = ABCMeta):
    @abstractmethod
    def fun(self):
        pass
class memo:
    def gun(self):
        print("In  gun")
print(type(demo))

#program8
from abc import abstractmethod,ABCMeta

class demo(meta = ABCMeta):
    @abstractmethod
    def fun(self):
        pass
print(type(demo))
demo()

#program9
from abc import abstractmethod,ABCMeta

class demo(meta = ABCMeta):
    def __init__(self):
        print("constructor")
    @abstractmethod
    def fun(self):
        pass
print(type(demo))
demo()

#program10
from abc import abstractmethod,ABCMeta

class demo(meta = ABCMeta):
    def __init__(self):
        print("constructor")
    #@abstractmethod
    def fun(self):
        pass
print(type(demo))
demo()

#program11

from abc import abstractmethod,ABCMeta

class demo(meta = ABCMeta):
    def __init__(self):
        print("constructor")
    #@abstractmethod
    def fun(self):
        pass
class demochild(demo):
    def __init__(self):
        super().__init__()
        print("Demochild constructor")
    def fun(self):
        print("Demochild fun")
print(type(demo))
print(demo.__abstractmethods__)
print(type(demochild))
print(demochild.__abstractmethods__)
demochild()

#program12

from abc import abstractmethod,ABCMeta

class demo(meta = ABCMeta):
    def __init__(self):
        print("constructor")
    #@abstractmethod
    def fun(self):
        pass
class demochild(demo):
    def __init__(self):
        super().__init__()
        print("Demochild constructor")
    def fun(self):
        print("Demochild fun")
print(type(demo))
print(demo.__abstractmethods__)
print(type(demochild))
print(demochild.__abstractmethods__)
demochild()

