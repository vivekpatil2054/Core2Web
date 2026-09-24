#program1
class a(object):
    def __init__(self):
        print("a constructor")
class b(object):
    def __init__(self):
        print("b constructor")
class c(a,b):
    def __init__(self):
        print("c constructor")
        super().__init__()
c()

#program2
class a(object):
    def __init__(self):
        print("a constructor")
        super().__init__()
        
class b(object):
    def __init__(self):
        print("b constructor")
class c(a,b):
    def __init__(self):
        print("c constructor")
        super().__init__()
c()

#program3
class a(object):
    def __init__(self):
        print("a constructor")
        super().__init__()
        
class b(object):
    def __init__(self):
        print("b constructor")
        super().__init__()

class c(a,b):
    def __init__(self):
        print("c constructor")
        super().__init__()
c()

#program4
class demo(object):
    def __init__(self):
            print("demo constructor")
            super().__init__()

class a(object):
    def __init__(self):
        print("a constructor")
        super().__init__()
        
class b(object):
    def __init__(self):
        print("b constructor")
        super().__init__()

class c(a,b):
    def __init__(self):
        print("c constructor")
        super().__init__()
c()

#program5
class demo(object):
    def __init__(self):
            print("demo constructor")
            super().__init__()

class a(object):
    def __init__(self):
        print("a constructor")
        super().__init__()
        
class b(object):
    def __init__(self):
        print("b constructor")
        super().__init__()

class c(a,b):
    def __init__(self):
        print("c constructor")
        super().__init__()
c()
print(c.__mro__)

#program6
class demo(object):
    def __init__(self):
            self.x = 20
            print("demo constructor")
            super().__init__()
    def disp():
        print("demo disp")

class a(object):
    def __init__(self):
        print("a constructor")
        super().__init__()
        
class b(object):
    def __init__(self):
        print("b constructor")
        super().__init__()

class c(a,b):
    def __init__(self):
        print("c constructor")
        super().__init__()
print(object.__mro__)
print(demo.__mro__)
print(a.__mro__)
print(b.__mro__)
print(c.__mro__)

#program7
class demo():
    def __init__(self):
            print("demo constructor")
            super().__init__()
    def disp():
        print("demo disp")

class a(demo):
    def __init__(self):
        print("a constructor")
        super().__init__()
        
class b(demo):
    def __init__(self):
        print("b constructor")
        super().__init__()

class c(demo):
    def __init__(self):
        print("c constructor")
        super().__init__()

class x(a,b):
    def __init__(self):
        print("x constructor")
        super().__init__()

class y(b,c):
    def __init__(self):
        print("y constructor")
        super().__init__()

class z(x,y):
    def __init__(self):
        print("z constructor")
        super().__init__()

#z()
print(z.__mro__)

#program8
class demo():
    def __init__(self):
            self.x = 20
            print("demo constructor")
            super().__init__()
    def disp():
        print("demo disp")

class a(demo):
    def __init__(self):
        print("a constructor")
        super().__init__()
        
class b(demo):
    def __init__(self):
        print("b constructor")
        super().__init__()

class c(demo):
    def __init__(self):
        print("c constructor")
        super().__init__()

class x(a,b):
    def __init__(self):
        print("x constructor")
        super().__init__()

class y(b,c):
    def __init__(self):
        print("y constructor")
        super().__init__()

class z(x,y,c):
    def __init__(self):
        print("z constructor")
        super().__init__()

z()
print(z.__mro__)

#program9
class demo():
    def __init__(self):
            print("demo constructor")

class x(demo):
    def __init__(self):
        print("x constructor")
       

class y(demo):
    def __init__(self):
        print("y constructor")
       

class z(demo):
    def __init__(self):
        print("z constructor")

print(z.__mro__)

#program10
class demo():
    def __init__(self):
            print("demo constructor")

class x(demo):
    def __init__(self):
        print("x constructor")
       

class y(demo):
    def __init__(self):
        print("y constructor")
       

class z(x,y):
    def __init__(self):
        print("z constructor")

print(z.__mro__)
obj = z()
obj.disp()

#program11
class demo():
    def __init__(self):
            print("demo constructor")

class x(demo):
    def __init__(self):
        print("x constructor")
       

class y(demo):
    def __init__(self):
        print("y constructor")
       

class z(x,y,demo):
    def __init__(self):
        print("z constructor")

print(z.__mro__)

#program11
class demo():
    def __init__(self):
            self.x = 20
            print("demo constructor")
            super().__init__()
    def disp():
        print("demo disp")

class a(demo):
    def __init__(self):
        print("a constructor")
        super().__init__()
        
class b(demo):
    def __init__(self):
        print("b constructor")
        super().__init__()

class c(demo):
    def __init__(self):
        print("c constructor")
        super().__init__()

class x(a,b,c):
    def __init__(self):
        print("x constructor")
        super().__init__()

class y(a,b,c):
    def __init__(self):
        print("y constructor")
        super().__init__()

class z(x,y):
    def __init__(self):
        print("z constructor")
        super().__init__()

z()
obj = z()
print(z.__mro__)
print(obj.x)


      






