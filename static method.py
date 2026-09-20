#program1
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
obj = demo()

#program2
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
obj = demo(50,60)
demo.clsfun()

#program3
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
        def instafun(self):
            print("In instance method")
            print(self.a)
            print(self.b)
obj = demo(50,60)
demo.clsfun()

#program4
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
        def instafun(self):
            print("In instance method")
            print(self.a)
            print(self.b)
obj = demo(50,60)
demo.clsfun()
obj1 = demo(50,60)
obj1.instafun()

#program5
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
        def instafun(self):
            print("In instance method")
            print(self.a)
            print(self.b)
obj = demo(50,60)
demo.clsfun()
obj1 = demo(50,60)
#obj1.instafun()
print(obj1.a)
print(obj1.b)
print(obj1.x)
print(obj1.y)

#program6
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
        def instafun(self):
            print("In instance method")
            print(self.a)
            print(self.b)
            print(self.x)
            print(self.y)
obj = demo(50,60)
demo.clsfun()
obj1 = demo(50,60)
obj1.instafun()

#program7
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
        def instafun(self):
            print("In instance method")
            print(self.a)
            print(self.b)
            print(self.x)
            print(self.y)
obj = demo(50,60)
demo.clsfun()
obj1 = demo(50,60)
obj1.instafun()
print(obj1.__dict__)

#program8
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
        def instafun(self):
            print("In instance method")
            print(self.a)
            print(self.b)
            print(self.x)
            print(self.y)
obj = demo(50,60)
demo.clsfun()
obj1 = demo(50,60)
obj1.instafun()
print(obj1.__class__.x)

#program9
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
        def instafun(self):
            print("In instance method")
            print(self.a)
            print(self.b)
            print(self.x)
            print(self.y)
obj = demo(50,60)
demo.clsfun()
obj1 = demo(50,60)
obj1.instafun()
print(obj1.__class__)

#program10
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
        def instafun(self):
            print("In instance method")
            print(self.a)
            print(self.b)
            print(self.__class__.x)
            print(self.__class__.y)
obj = demo(50,60)
demo.clsfun()
obj1 = demo(50,60)
obj1.instafun()
print(obj1.__class__)

#program11
class demo:
    x = 10
    y = 20

    def __init__(self,a,b):
        print("constructor")
        self.a = a
        self.b = b
        @classmethod
        def clsfun(cls):
            print("In class method")
            print(cls.x)
            print(cls.y)
        def instafun(self):
            print("In instance method")
            print(self.a)
            print(self.b)
            print(self.__class__.x)
            print(self.y)
obj = demo(50,60)
demo.clsfun()
obj1 = demo(50,60)
obj1.instafun()

#Static method
#program1
class demo:
    x  = 10
    def __init__(self):
        self.y = 20
    @staticmethod
    def add(a,b):
        print("Add:",a+b)
demo.add(10,20)

#program2
class demo:
    x  = 10
    def __init__(self):
        self.y = 20
    @staticmethod
    def add(a,b):
        print("Add:",a+b)
demo.add(10,20)
obj1 = demo()
obj1.add(50,60)









