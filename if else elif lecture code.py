#IF

#1
x = 10
if x > 5:
    print("x is grester than 5")

#2
x = int(input("Enter num: "))
print("Start code")
print(x,"is greater than 10")
print("End Code")  

#3
x = int(input("Enter num: "))
print("start code")
if x > 10:
    print(x,"is greater than 10")
print("End code") 

#4
x = int(input("Enter num1: "))
if x%5 ==  0:
    print(x,"is divisble by 5")


val = int(input("Enter num1: "))
if val%3 == 0 and val%5 == 0:
    print(val,"is divisible by 3 and 5")

#Else
#1
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
if num1 > num2:
    print(num1,"is greater")
else:
    print(num2,"is greater")

#2
num1 = int(input("Enter num1: "))
if num1%3 == 0 or num1%5 == 0:
    print(num1,"it is divisible by 3 or5")
else:
    print(num1,"it is not divisible by 3 or 5 ")

#3
num1 = int(input("Enter num1: "))
if num1%3 == 0:
    print(num1,"it is divisible by 3")
    print("in if block")
else:
    print(num1,"is not divisible by 3")

#4
num1 = int(input("Enter num1: "))
if (num1%3 == 0):
    print("in outer if block")
    if num1 >= 10:
        print(num1,"is greater than 10")
print("End Code")

#elif
#1
x = 10
if x>10:
    print("x is greater than 10")
elif x==10:
    print("x is equal to 10")
else:
    print("x is less than 10")

#2
day = input("Enter day: ")
if day == "Mon" or day == "Monday":
    print("start of week")
elif day == "Fri" or day == "Friday":
    print("weekend is coming")
elif day == "Sat" or day == "Saturday":
    print("weekend started")
elif day == "Sun" or day == "Sunday":
    print("relax,it's sunday")
else:
    print("yet another day")
    

    
