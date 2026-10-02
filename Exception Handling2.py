#program1
print("start code")
try:
    x = int(input("enter num1: "))
    y = int(input("enter num2": ))
    result  = x/y
    print("result:",x/y)
except Exception:
    print("handling code")
print("end code")

#program2
print("start code")
try:
    x = int(input("enter num1: "))
    y = int(input("enter num2": ))
    result  = x/y
    print("result:",x/y)
except Exception:
    print("handling code")
print("end code")

#program3
print("start code")
try:
    x = int(input("enter num1: "))
    y = int(input("enter num2": ))
    result  = x/y
    print("result:",x/y)
except ValueError:
    print("wrong imput format")
except ZeroDivisionError:
    print("divide by zero")
except Exception:
    print("handling code")
print("end code")

#program4
print("start code")
try:
    x = int(input("enter num1: "))
    y = int(input("enter num2": ))
    result  = x/y
    print("result:",x/y)
except ValueError:
    print("wrong imput format")
except ZeroDivisionError:
    print("divide by zero")
except Exception:
    print("handling code")
print("result:",x/y)
print("end code")

#Try Except Else

#program1
print("start code")
try:
    x = int(input("enter num1: "))
    y = int(input("enter num2": ))
    result  = x/y
    print("result:",x/y)
except ValueError:
    print("wrong imput format")
except ZeroDivisionError:
    print("divide by zero")
except Exception:
    print("handling code")
else:
    print("result:",x/y)
print("end code")

#Try Except Finally

#program1
print("database/network connection")
try:
    x = int(input("enter data1: "))
    y = int(input("enter data2: "))
    result = x/y
    print("result: ",x/y)
except ValueError:
    print("wrong format")
except ZeroDivisionError:
    print("divided by zero")
finally:
    print("connection close")
print("connection close")

#program2
print("database/network connection")
try:
    x = int(input("enter data1: "))
    y = int(input("enter data2: "))
    result = x/y
except ValueError:
    print("wrong format")
except ZeroDivisionError:
    print("divided by zero")
else:
    print("result: ",x/y)
finally:
    print("connection close")
print("connection close")

#program2
print("start code")
def voting(age):
    if age < 18:
        print("not eligible for voting")
    else:
        print("eligible")
age  = int(input("enter your age: "))
voting(age)
print("end code")

#Raise
#program1
print("start code")
def voting(age):
    if age < 18:
        raise ValueError("not eligible for voting")
    else:
        print("eligible")
age  = int(input("enter your age: "))
voting(age)
print("end code")

#program2
print("start code")
def voting(age):
    if age < 18:
        raise ValueError("not eligible for voting")
    else:
        print("eligible")
age  = int(input("enter your age: "))
try:
    voting(age)
except ValueError:
    print("age below age")
voting(age)
print("end code")

#program3
print("start code")
def voting(age):
    if age < 18:
        raise ValueError("not eligible for voting")
    else:
        print("eligible")
age  = int(input("enter your age: "))
try:
    voting(age)
except ValueError as e:
    print(e)
voting(age)
print("end code")

#program4
print("start code")
def voting(age):
    if age < 18:
        raise ValueError("not eligible for voting")
    else:
        print("eligible")
age  = int(input("enter your age: "))
try:
    voting(age)
except ValueError as e:
    print(type(e).__name__,":",e)
voting(age)
print("end code")

#program16
class biryanisampleyexception(Exception):
    pass
class order():
    biryanicount = 1
def __init__(self):
    if self.biryanicount == 0:
        raise biryanisampleyexception("Ghari ja..")
obj = order()
obj.getbiryani()
obj.getbiryani()
print("end code")


