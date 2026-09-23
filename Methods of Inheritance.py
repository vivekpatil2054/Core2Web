#program1
class demo:
    x = 10
    def __init__(self):
        print("demo constructor")
        self.y = 20
        self.z = 30
    def disp(self):
        print("In display")
        print(self.y)
        print(self.z)
class demochild(demo):
    def __init__(self):
        super().__init__()
        print("demochild constructor")
obj1 = demo()
obj1.disp()
obj2 = demochild()
obj2.disp()

#program2
class demo:
    x = 10
    def __init__(self):
        print("demo constructor")
        self.y = 20
        self.z = 30
    def disp(self):
        print("In display")
        print(self.y)
        print(self.z)
class demochild(demo):
    def __init__(self):
        super().__init__()
        print("demochild constructor")
print(demo.__dict__)
obj1 = demo()
print(obj1.__dict__)
# obj1.disp()
# obj2 = demochild()
# obj2.disp()

#single inheritance

#program1
class demo:
    x = 10
    def __init__(self):
        print("demo constructor")
        self.y = 20
        self.z = 30
    def disp(self):
        print("In display")
        print(self.y)
        print(self.z)
class demochild(demo):
    def __init__(self):
        super().__init__()
        print("demochild constructor")
obj1 = demo()
obj1.disp()
obj2 = demochild()
obj2.disp()

#multilevel inheritance

#program1
class demo:
    def __init__(self):
        print("demo constructor")
        self.x = 10
class demochild1(demo):
    def __init__(self):
        super().__init__()
        print("demochild1 constructor")
        self.y = 20
class demochild2(demochild1):
    def __init__(self):
        super().__init__()
        print("demochild2 constructor")
        self.z = 30
obj = demochild2()
print(obj.x)
print(obj.y)
print(obj.z)


