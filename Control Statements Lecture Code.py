#1
num1 = input("Enter Number: ")
num2 = input("Enter Number: ")

if num1 > num2:
    print("num1 is greater")
else:
    print("num2 is greater")

#2
num1 = input("Enter Number: ")
num2 = input("Enter Number: ")
num3 = input("Enter Number: ")
if num1 > num2 and num1 > num3:
    print(num1,"is greater")
elif num2 > num1 and num2 > num3:
    print(num2,"is greater")
else:
    print(num3,"is greater")

#3Match Case

#1
day = input("Enter day: ")
match day:
    case "Mon":
        print("start of week")
    case "Fri":
        print("weekend is coming")
    case "Sat":
        print("weekend started")
    case "Sun":
        print("Tt's Sunday")
    case _ :
        print("weekday")

#2
num = int(input("Enter num: "))
match num:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("Three")
    case 4:
        print("four")
    case _:
        print("number not matched")

#3
num = float(input("Enter num: "))
match num:
    case 1.5:
        print("one")
    case 2.5:
        print("two")
    case 3.5:
        print("Three")
    case 4.5:
        print("four")
    case _:
        print("number not matched")        

#while loop

#1
print("Coreweb")
print("Coreweb")
print("Coreweb")
print("Coreweb")

#2
num = int(input("Enter num: "))
x = 1
while x < num:
    print(x)

#3
num = int(input("Enter num: "))
x = 1
while x < num:
    print(x)
    x = x + 1

#4
num = int("Enter num: ")
x = 1
while x <=num:
    print(x)
    x = x + 1 

#5
num = int(input("Enter value: "))
x = 1
while x<=num:

    print(x)
    if x == 5:
        break
    x = x + 1

#6
x = 1
while x<=num:

    print(x)
    if x == 5:
        pass
    x = x + 1


    


       

            
