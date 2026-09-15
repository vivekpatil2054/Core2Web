#program1
x = 50
name = "ashish"
def demo():
    x = 10
    name = "kanha"
    print(x)
    print(name)
print(x)
print(name)

#program2
a = 50
class demo:
    x = 10
    def disp():
        print("x:",x)
def fun():
    print("In fun")
print(a)
fun()
print(demo.x)

#program3
a = 50
class demo():
    x = 10
    def disp():
        print("x:",x)
def fun():
    print("In fun")
print(a)
fun()
print(demo.x)
demo.disp()

#Class
#program1
class demo:
    x = 10
    def disp():
        print("In disp")
obj = demo()
print(obj.x)

#Object creation in Python

#program1
class demo:
    x = 10
    def disp(self):
        print("In disp")
obj = demo()
print(obj.x)
obj.disp()

#program2
class demo:
    def __init__(self):
        print("In constructor")
print("start main")
obj = demo()
print("end main")

#program3
class demo:
    x = 10
    def disp():
        print("In disp")
obj = demo()
print(obj.x)

#program4
class demo:
    x = 10
    def __new__(cls):
        print("In new method")
        return super().__new__(cls)
    def __init__(self):
        print("In init:constructor")
    def disp(self):
        print("In disp")
obj = demo()
print(obj.x)
obj.disp()

#program5
class demo:
    x = 10
    def __new__(cls):
        print("In new method")
        return super().__new__(cls)
    def __init__(self):
        print("In init:constructor")
    def disp(self):
        print("In disp")
demo()

#program6
class demo:
    x = 10
    def __new__(cls):
        print("In new method")
        return object (cls)
    def __init__(self):
        print(self)
        print("In init:constructor")
    def disp(self):
        print(" ")
obj = demo()
print(obj)

#program7
class demo:
    x = 10
    def __new__(cls):
        print("In new method")
        return object (cls)
    def __init__(self):
        print(self)
        print("In init:constructor")
    def disp(self):
        print(" ")
print(obj.x)
obj.disp()

#program8
class demo:
    x = 10
    def __new__(cls):
        print("In new method")
        return object (cls)
    def __init__(self):
        print(self)
        print("In init:constructor")
    def disp(self):
        print(" ")
obj = demo()
print(obj.x)
obj.disp()
print(type(demo))

#program9
import __main__
class demo:
    x = 10
    def __new__(cls):
        print("In new method")
        return object (cls)
    def __init__(self):
        print(self)
        print("In init:constructor")
    def disp(self):
        print(" ")
obj = demo()
print(obj.x)
obj.disp()
print(type(demo))
print(__main__.__dict)







