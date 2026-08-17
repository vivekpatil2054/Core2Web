#while loop
#1
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x < y:
    print(x)
    x = x + 1
print("End Code")

#2
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x < y:
    print(x)
    if x % 5 == 0:
        break
    x = x + 1
print("End Code")    

#3
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x < y:
    print(x)
    if x % 5 == 0:
        break
    x = x + 1
print("End Code") 

#4
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x < y:
    if x % 5 == 0:
        continue
    print(x)
    x = x + 1
print("End Code")

#5
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x < y:
    x = x + 1
    if x % 5 == 0:
        continue
    print(x)
print("End Code")

#6
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x<=y:
    x = x + 1
    if x % 5 == 0:
        continue
    print(x)
print("end code")

#7
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x <= y:
    print(x)
    x = x + 1
    if x%5 == 0:
        break
    print(x)
print("end code")

#else bolck
#1
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x <= y:
    print(x)
    x = x + 1

#2
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x <= y:
    print(x)
    x = x + 1
else:
    print("In else block")

#3
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x<=y:
    print(x)
    x = x + 1
else:
    print("In else block")
    print(x)

#4
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
while x <= y:
    x = x + 1
    if x %5 == 0:
        break
    print(x)
else:
    print("in else block")
    print(x)

#for loop
#1
teamindia = ["rohit","virat","shubman"]
for player in teamindia :
    print(player)

#2
teamindia = ["rohit","virat","shubman"]
for player in teamindia :
    if player == "virat":
        break
    print(player)    

#3
teamindia = ["rohit","virat","shubman"]
for player in teamindia :
    if player == "virat":
       continue
    print(player)    

#4
compName="microsoft"
for x in compName:
    print(x)

#5
compName = "spacex tesla"
for x in compName:
    print(x) 

#6
compName = "spacex tesla"
for x in compName:
    if x == " ":
        break
    print(x)  

#7
countries = ("India","Pak","China","USA")
for x in countries:
    if x == "Pak":
        continue
    print(x)

#8
countries = ("India","Pak","China","USA")
for x in countries:
    if x == "Pak":
        break
    print(x)

#9
data = [2,4,6,8,10]
for x in data:
    if x%3 == 0:
        break  
    print(x) 
else:
    print("In else block")

#range function 
#1
x = int(input("Enter num: "))
y = int(input("Enter nun: ")) 
for data in range(x,y):
    print(data)

#2
x = int(input("Enter num: "))
y = int(input("Enter nun: ")) 
for data in range(x,y+1):
    print(data)

#3
for data in range(10):
    print(data)

#4
for data in range(5,10):
    print(data) 

#5
for data in range(5,10,1):
    print(data) 

#6
for data in range(1,10,2):
    print(data)

#7
for data in range(10,1,-1):
    print(data)

#8
for data in range(10,1,-3):
    print(data)
    if data == 4:
        break
    else:
        print("In else block")

#9
for data in range(10,1,-4):
    print(data)
    if data == 4:
        break
    else:
        print("In else block")



