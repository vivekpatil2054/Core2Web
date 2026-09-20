#program1
class player:
    team = "India"
    def __new__(cls,*args,**kwargs):
        print("Memory allocation")
        return super().__new__(cls)
    def __init(self,playername,jerno):
        print("In constructor")
        self.playername = playername
        self.jerno = jerno
obj1 = player("virat",18)
obj2 = player("MSd",7)
obj3 = player("rohit",45)

#program2
class player:
    team = "India"
    def __init(self,playername,jerno):
        print("In constructor")
        self.playername = playername
        self.jerno = jerno
obj1 = player("virat",18)
obj2 = player("MSd",7)
obj3 = player("rohit",45)

#program3
class player:
    team = "India"
    def __init(self,playername,jerno):
        print("In constructor")
        self.playername = playername
        self.jerno = jerno
obj1 = player("virat",18)
print(obj1)
obj2 = player("MSd",7)
print(obj2)
obj3 = player("rohit",45)
print(obj3)

#program4
class player:
    team = "India"
    def __init(self,playername,jerno):
        print("In constructor")
        self.playername = playername
        self.jerno = jerno
obj1 = player("virat",18)
print(obj1.team)
obj2 = player("MSd",7)
print(obj2.team)
obj3 = player("rohit",45)
print(obj3.team)

#program5
class player:
    team = "India"
    def __init(self,playername,jerno):
        print("In constructor")
        self.playername = playername
        self.jerno = jerno
print(player.team)
player.team = "bharat"
obj1 = player("virat",18)
print(obj1.team)
obj2 = player("MSd",7)
print(obj2.team)
obj3 = player("rohit",45)
print(obj3.team)

#program6
class demo:
    a = 50
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @classmethod
    def clsfun(cls):
        print("In class method")
    def instafun(self):
        print("In instance method")
obj = demo(10,20)
obj.clsfun()
obj.instafun()

#program7
class demo:
    x = 10
    def __init__(self):
        self.y = 20
    @classmethod
    def fun(cls):
        print("In class method")
demo.fun()

#program8
class demo:
    x = 10
    def __init__(self):
        self.y = 20
    @classmethod
    def fun(cls):
        print("In class method")
demo.fun()
obj = demo()
obj.fun()

#program9
class demo:
    x = 10
    def __init__(self):
        self.y = 20
    @classmethod
    def fun(cls):
        print("In class method")
        print(demo.y)
        print(cls.x)
demo.fun()
obj = demo()
obj.fun()

#program10
class demo:
    x = 10
    @classmethod
    def fun(cls):
        print("In class method")
        print(demo.x)
#cls.x
demo.fun()

#program11
class demo:
    x = 10
    y = 20
    @classmethod
    def fun(cls):
        print("In class method")
        print(cls.x)
        print(demo.x)

demo.fun()

#program12
class demo:
    x = 10
    y = 20
    @classmethod
    def fun(cls):
        print("In class method")
        print(cls)

demo.fun()
print(demo)

#program13
class demo:
    x = 10
    y = 20
    @classmethod
    def fun(cls):
        print("In class method")
        print(cls)

demo.fun()

#program14
class demo:
    def __init__(self):
        print("constructor")
        self.x = 10
        self.y = 20
    def fun(self):
        print("In fun")
        print(self.x)
        print(self.y)
obj = demo()
demo.fun(obj)

#program15
class demo:
    x = 10
    y = 20
    def __init__(self):
        self.a = 50
        self.b = 60
    @classmethod
    def fun(cls):
        print("In class method")
        print(cls.x)
        print(cls.y)
    def run(self):
        print("In instance method")
        print(self.a)
        print(self.b)
demo.fun()
obj = demo()
demo.run(obj)
#obj.run()










