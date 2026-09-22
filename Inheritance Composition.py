1#program
class demo:
    def __init__(self):
        self.x = 10
        self.y = 20
    def disdata(self):
        print(self.x)
        print(self.y)
class memo:
    def __init__(self):
        print("memo Constructor")
        self.demo = demo()
obj = demo()
obj.demo.disdata()

#program2
class demo:
    def __init__(self):
        self.x = 10
        self.y = 20
    def disdata(self):
        print(self.x)
        print(self.y)
class memo:
    def __init__(self):
        print("memo Constructor")
        self.demo = demo()
obj = demo()
#obj.demo.disdata()
#print(obj.demo.x)
#print(obj.demo.y)

#program3
class demo:
    def __init__(self):
        self.x = 10
        self.y = 20
    def disdata(self):
        print(self.x)
        print(self.y)
class memo:
    def __init__(self):
        print("memo Constructor")
        def memofun(self):
            obj = demo()
            obj.disdata()
obj = demo()
obj.memodata()

#program4
class macd:
    def taste(self):
        print("Burger and fries taste:same in all outlets")
    def price(self):
        print("price:same in all outlets")
class macdpune(macd):
    def __init__(self):
        print("constructor pune")
    def location(self):
            print("location:pune")
class macdmumbai(macd):
    def __init__(self):
            print("constructor mumbai")
    def location(self):
            print("location:mumbai")
obj1 = macdpune()
obj1.taste()
obj1.price()
obj1.price()
obj1.location()
obj2 = macdmumbai()
obj2.taste()
obj2.price()
obj2.price()
obj2.location()

#program5
class demo:
    def __init__(self):
        print("demo constructor")
    def dispdemo(self):
        print("instance constructor")
class demochild:
    def __init__(self):
        print("demochild constructor")
obj = demochild()
obj.dispdemo()

#program6
class demo:
    def __init__(self):
        print("demo constructor")
        self.x = 10
        self.y = 20
    def dispdemo(self):
        print(self.x)
        print(self.y)
class demochild(demo):
    def __init__(self):
        print("demochild constructor")
obj = demochild()
obj.dispdemo()

#program7
class demo:
    def __init__(self):
        print("demo constructor")
        self.x = 10
        self.y = 20
    def dispdemo(self):
        print(self.x)
        print(self.y)
class demochild(demo):
    def __init__(self):
        super().__init__()
        print("demochild constructor")
obj = demochild()
obj.dispdemo()

#program8
class demo:
    def __init__(self):
        print("demo constructor")
        self.x = 10
        self.y = 20
    def dispdemo(self):
        print(self.x)
        print(self.y)
class demochild(demo):
    def __init__(self):
        demo.__init__(self)
        print("demochild constructor")
              
obj = demochild()
obj.dispdemo()

#program9
class demo:
    def __init__(self):
        print("demo constructor")
        self.x = 10
        self.y = 20
    def dispdemo(self):
        print(self.x)
        print(self.y)
class demochild(demo):
    def __init__(self):
        super().__init__()
        print("demochild constructor")
obj = demochild()
obj.dispdemo()
print(obj.__dict__)

#program10
class demo:
    def __init__(self):
        print("demo constructor")
        self.x = 10
        self.y = 20
    def dispdemo(self):
        print(self.x)
        print(self.y)
class demochild(demo):
    def __init__(self):
        super().__init__()
        print("demochild constructor")
obj = demochild()
obj.dispdemo()
print(obj.y)
print(obj.__dict__)
print(demochild.__dict__)
print(obj.__dict__)

#program11
class demo:
    z = 30
    def __init__(self):
        print("demo constructor")
        self.x = 10
        self.y = 20
    def dispdemo(self):
        print(self.x)
        print(self.y)
class demochild(demo):
    def __init__(self):
        super().__init__()
        print("demochild constructor")
obj = demochild()
obj.dispdemo()
print(obj.y)
print(obj.z)
print(demochild.__mro__)
# print(obj.__dict__)
# print(demochild.__dict__)
# print(obj.__dict__)










