#SyntaxError
print("start code")
x = 10
if x < 20:
    print("In if")
else
    print("In else")
print("end code")

#Identation Error
print("start code")
x = 10
if x < 20:
    print("In if")
else:
print("In else")
print("end code")

#Name Error
print("start code")
print(x)
print("end code")

#program4
class demo:
    x = 10
    def fun(self):
        print("In fun")
obj = demo()
print(obj.x)
obj.fun()

#Attribute Error
class demo:
    x = 10
    def fun(self):
        print("In fun")
obj = demo()
print(obj.x)
obj.fun()
print(obj.y)
#obj.run()

#program6
class demo:
    x = 10
    def fun(self):
        print("In fun")
obj = demo()
print(obj.x)
obj.fun()
#print(obj.y)
obj.run()

#Import Error
from abc import AbcMeta
class demo(metaclass = AbcMeta):
    pass

#Index Error
listobj = [10,20,30,40]
print(listobj[0])
print(listobj[3])
print(listobj[4])

#program9
listobj = [10,20,30,40]
print(listobj[0])
print(listobj[3])
listobj.fun()
print(listobj[4])

#program9
print(x)

#Key Error
players = {45:"rohit",7:"MSD",18:"Virat"}
print(players[7])
print(players[18])
print(players[1])

#ZeroDivision Error
x = int(input("enter num1: "))
y = int(input("enter num2: "))
result = x/y
print("answer:",x/y)

#Value Error
x = int(input("enter num1: "))
y = int(input("enter num2: "))
result = x/y
print("answer:",x/y)

#Type Error
x = "kanha"
y = 10
print(x+y)

#Keyboard Error
while True:
    print("Running...")

#SystemExit
print("start code")
x = 5
if x < 10:
    print("Running")
    exit()
else:
    print("In else")
print("end code")

#Try-Except

#program15
# print("start code")
# # #try:
# #     x = int(input(enter the num1: "))
# #     y = int(input(enter the num2: "))
#     result = x/y
#     print(result)
'''
except:
    print("exception catch")
print("end code")
'''
#program16
print("start code")
try:
    x = int(input(enter the num1: "))
    y = int(input(enter the num2: "))
    result = x/y
    print(result)
except:
    print("exception catch")
print("end code")

#Try with Multiple except block

#program17
print("start code")
try:
    x = int(input(enter the num1: "))
    y = int(input(enter the num2: "))
    result = x/y
    print(result)
except ValueError:
    print("wrong input error")
except ZeroDivisionError:
    print("zero division not allowed")
print("end code")

#program19
print("start code")
try:
    x = int(input(enter the num1: "))
    y = int(input(enter the num2: "))
    result = x/y
    print(result)
except TypeErrorError:
    print("wrong input error")
except ZeroDivisionError:
    print("zero division not allowed")
print("end code")

#program20
print("start code")
try:
    x = int(input(enter the num1: "))
    y = int(input(enter the num2: "))
    result = x/y
    print(result)
except Exception:
    print("konipan yeude")
except TypeErrorError:
    print("wrong input error")
except ZeroDivisionError:
    print("zero division not allowed")
print("end code")

#program21
print("start code")
try:
    x = int(input(enter the num1: "))
    y = int(input(enter the num2: "))
    result = x/y
    print(result)
except TypeErrorError:
    print("wrong input error")
except ZeroDivisionError:
    print("zero division not allowed")
except Exception:
    print("konipan yeude")
print("end code")


    
    

