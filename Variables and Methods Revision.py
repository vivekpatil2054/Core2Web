#program1
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
obj  = demo()
print(globals())

#program2
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
obj  = demo()
print(demo.z)
print(demo.x)

#program3
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
obj  = demo()
print(demo.__dict__)
print(demo.__dict__)

#program4
class demo:
    z = 30
    x = 50
    def __init__(self):
        self.x = 10
        self.y = 20
obj  = demo()
print(demo.z)
print(demo.x)
print(obj.x)
print(obj.y)

#program5
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
    def instfun(self):
        print("instance method")
    @classmethod
    def clsfun(cls):
        print("class method")
    @staticmethod
    def staticfun():
        print("ststic method")
obj = demo()
print(demo.__dict__)

#program6
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
    def instfun(self):
        print("instance method")
    @classmethod
    def clsfun(cls):
        print("class method")
    @staticmethod
    def staticfun():
        print("ststic method")
obj = demo()
demo.instfun()

#program7
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
    def instfun(self):
        print("instance method")
    @classmethod
    def clsfun(cls):
        print("class method")
    @staticmethod
    def staticfun():
        print("ststic method")
obj = demo()
obj.instfun()

#program8
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
    def instfun(self):
        print("instance method")
    @classmethod
    def clsfun(cls):
        print("class method")
    @staticmethod
    def staticfun():
        print("ststic method")
obj = demo()
obj.instfun()
demo.clsfun()

#program9
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
    def instfun(self):
        print("instance method")
    @classmethod
    def clsfun(cls):
        print("class method")
    @staticmethod
    def staticfun():
        print("ststic method")
obj = demo()
#obj.instfun()
demo.clsfun()

#program10
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
    def instfun(self):
        print("instance method")
    @classmethod
    def clsfun(cls):
        print("class method")
    @staticmethod
    def staticfun():
        print("ststic method")
obj = demo()
demo.staticfun()

#program11
class demo:
    z = 30
    def __init__(self):
        self.x = 10
        self.y = 20
    def instfun(self):
        print("instance method")
    @classmethod
    def clsfun(cls):
        print("class method")
    @staticmethod
    def staticfun():
        print("ststic method")
obj = demo()
obj.staticfun()







