#program1
num1 = int(input("Enter the number: "))

if num1 % 4 == 0  or num1 % 5 ==0:
    print(num1, "is divisible by 4 or 5")
else:
    print(num1, "is not divisible by 4 or 5")

#program2
angle1 = int(input("Enter the first angle:"))
angle2 = int(input("Enter the second angle:"))
angle3 = int(input("Enter the third angle:"))

if angle1 + angle2 + angle3 == 180:
    print("It is a right angled triangle")
else:
    print("It is not a right angled triangle")

#program3
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

sum = num1 + num2
if sum % 2 == 0:
    print(sum, "is even"  )

#program4
list1 = [10,20,30,40,50]
num = int(input("Enter the number: "))
if num in list1:
    print("available")
else:
    print("not available")

#program5
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Core2web" * num)

#program6
num = int(input("Enter a number: "))

if num % 2 != 0:
    print("odd")

#program7
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 2 != 0 and num2 % 2 != 0:
    print("Sum =", num1 + num2)

#program8
ch = input("Enter a character: ")

ascii_value = ord(ch)

if ascii_value % 2 == 0:
    print(ch)
else:
    print("Odd")

#program9
ch1 = input("Enter a  1 character: ")
ch2 = input("Enter a  2 character: ")

ascii_value1 = ord(ch1)
ascii_value2 = ord(ch2)

if ascii_value1 % 2 != 0 and ascii_value2 % 2 != 0:
    print(ascii_value1 + ascii_value2 )

#program10
num = int(input("Enter a number: "))

rem = num % 8

if rem == 3:
    print(num)
else:
    print(rem)



