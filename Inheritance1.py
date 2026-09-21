#program1
class demo:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.z = 30
obj = demo()
print(obj.x)
print(obj.y)
print(obj.z)

#program2
class demo:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.z = 30
obj = demo()
print(obj.x)
print(obj._y)
print(obj.z)

#program3
class demo:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.__z = 30
obj = demo()
print(obj.x)
print(obj.y)
print(obj.z)
print(obj.__dict__)

#program4
class demo:
    def __init__(self):
        print("In constructor")
        self.x = 10
        self.y = 20
        self.__z = 30
obj = demo()
print(obj.x)
print(obj.y)
print(obj.z)
print(obj.__dict__)



