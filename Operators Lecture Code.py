#Arithmetic Operator
x = 3
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x**y)

#Assignment operator
x = 10

x += 20
print(x)

x -= 20
print(x)

x *=20
print(x)

x /= 20
print(20)

x %= 20
print(x)

x //= 20
print(x)

x **= 20
print(x)

#Realtionship operator
x = 10
y = 20
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)

#code7
x = 10
print(x)
y = ++x
print(y)

#logical operator

x = 10
y = 15
z = 30
print(x<y and y<z)
print(x>y and y<z)

print(x<y or y<z)
print(x>y or y<z)

print(not(x<y))

#code11
x = 10
y = 10
print(id(x))
print(id(y))

print(x==y)
print(id(x) == id(y))

#code13
x = 257
y = 257
print(id(x))
print(id(y))

print(x==y)
print(id(x) == id(y))

#code14
str1 = "kahna"
str2 = "kahna"
print(str1 == str2)
print(id(str1) == id(str2))

#code17
list1 = [10,20,30]
print(list1)

list2 = [10,20,30]
print(list2)

print(type(list1))
print(type(list2))
print(id(list1) == id(list2))

#identity operator
x = 50
y = 50
list1 = [10,20,30]
list2 = [10,20,30]
print(x is y)
print(list1 is list2)
print(list1 is not list2)

#membership operator
listData = [10,20,30,40,50]
tplData = (10,20,30,40,50)
print(10 in listData)
print(60 in listData)

#Bitwise operator
x = 5
y = 7
print(x&7)
print(x|y)
print(x^y)
print(x<<2)
print(x>>y)
print(~x)
print(~y)

#output
#code32
print("kahna","rahul")
print("Ashish")

#code32
print("kanha",end=" ")
print("ashish")

#code36
print("kahna",end=" ")
print("ashish",end="\n")

#code37
print("kahna","ashish",sep="-")

#input
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

print("x=",x)
print("y=",y)

print("sum = ",x+y)

