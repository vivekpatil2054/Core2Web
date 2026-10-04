#program1
class demoexception(Exception):
    pass
class nomral:
    counter = 1
    def __init__(self):
        print("constructor")
    def fun(self):
        if counter < 1:
            raise demoexception("value less than 1") 
obj = normal()

#program2
class demoexception(Exception):
    pass
class nomral:
    counter = 1
    def __init__(self):
        print("constructor")
    def fun(self):
        if counter < 1:
            raise demoexception("value less than 1") 
        else:
            print("counter..")
            self.counter = self.counter - 1
print("end code")

obj = normal()
obj.fun()
obj.fun()

#program3
class demoexception(Exception):
    pass
class nomral:
    counter = 1
    def __init__(self):
        print("constructor")
    def fun(self):
        if self.counter < 5:
            raise demoexception("value less than 1") 
        else:
            print("counter..")
            self.counter = self.counter - 1
print("end code")

obj = normal()
obj.fun()
obj.fun()
print("end code")

#program4
class demoexception(Exception):
    def __init__(self):
        print("In demoexception constructor")
class nomral:
    counter = 1
    def __init__(self):
        print("constructor")
    def fun(self):
        if self.counter < 5:
            raise demoexception("value less than 1") 
        else:
            print("counter..")
            self.counter = self.counter - 1
print("end code")
obj = normal()
obj.fun()
obj.fun()


#program5
class demoexception(Exception):
    def __init__(self):
        print("In demoexception constructor")
class nomral:
    counter = 1
    def __init__(self,msg):
        print("constructor")
    def fun(self):
        if self.counter < 5:
            raise demoexception("value less than 1") 
        else:
            print("counter..")
            self.counter = self.counter - 1
print("end code")

obj = normal()
obj.fun()
obj.fun()


#program6
class demoexception(Exception):
    def __init__(self):
        print("In demoexception constructor")
class nomral:
    counter = 1
    def __init__(cls,args):
        print("constructor")
        return super().__new__(cls)
    def fun(self):
        if self.counter < 5:
            raise demoexception("value less than 1") 
        else:
            print("counter..")
            self.counter = self.counter - 1
obj = normal()
obj.fun()
obj.fun()
print("end code")

#program7
class demoexception(Exception):
    def __init__(self):
        print("In demoexception constructor")
class nomral:
    counter = 1
    def __init__(cls,args):
        print("constructor")
        return super().__new__(cls)
    def fun(self):
        if self.counter < 5:
            raise demoexception("value less than 1") 
        else:
            print("counter..")
            self.counter = self.counter - 1
try:
    obj.fun()
    obj.fun()
except ValueError as e:
    print(e)
print("end code")

obj = normal()
obj.fun()
obj.fun()

#program8
class demoexception(Exception):
    def __init__(self):
        print("In demoexception constructor")
class nomral:
    counter = 1
    def __init__(cls,args):
        print("constructor")
        return super().__new__(cls)
    def fun(self):
        if self.counter < 5:
            raise demoexception("value less than 1") 
        else:
            print("counter..")
            self.counter = self.counter - 1
try:
    obj.fun()
    obj.fun()
except ValueError as e:
    print(e)
except demoexception as e:
    print(e)
print("end code")
      
obj = normal()
obj.fun()
obj.fun()

#program9
#Handling keyboard Interrupt Exception
def fun():
    while True:
        print("In fun")
try:
    fun()
except BaseException:
    print("exception catch")
print("end code")

#program10
def fun(value):
    if value < 5:
        print("value less than 5")
        exit()
    else:
        print("value greater than 5")
data = int(input("enter value: "))
fun(data)
print("end code")

#program11
def fun(value):
    if value < 5:
        print("value less than 5")
        exit()
    else:
        print("value greater than 5")
data = int(input("enter value: "))
try:
    fun(data)
except SystemExit:
    print("Systemexit")
print("end code")
fun(data)

