#program1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num1, "id maximum")
else:
    print(num2, " is maximum")

#program2
num1 = int(input("Enter the number: "))
if num1 > 0:
    print(num1, "is positive")
elif num1 < 0:
    print(num1, "is negative")
else:
    print(num1, "is zero")  

#program3
num1 = int(input("Enter the number: "))
if num1 % 2 == 0:
    print(num1, "is even")
else:
    print(num1, "is odd")

#program4
num1 = int(input("Enter the number: "))
if num1 % 5 == 0:
    print(num1, "is divisible by 5")
else:
    print(num1, "is not divisible by 5 ")

#program5
num1 = int(input("Enter the number: "))
if num1 == 1:
    print("Monday")
elif num1 == 2:
    print("Wednesday")
else:
    print("Weekday")

#program6
num1 = str(input("Enter the alphabet: "))
if (num1 =="v"):
    print("v is an alphabet")
else:
    print("Is not a alphabet")

#program7
num = int(input("Enter the number: "))
if num == 1:
    print("Jan is 31-day month")
elif num == 2:
    print("Feb is 28-days month")
elif num == 3:
    print("Mar is 31-day month")
elif num == 4:
    print("April is 30-day month")
else:
    print("It is another month")

#program8:
num1 = int(input("Enter the number: "))
if num1 < 10:
    print("no",num1,"is lesser than 10")
else:
    print("yes",num1,"is greater than 10")

#program9
num = str(input("Enter the number: "))
if num == "a" or num == "e" or num == "i" or num == "o" or num == "u" or num == "A" or num == "E" or num == "I" or num == "O" or num == "U":
    print(num, "It is a Vowel")
else:
    print(num , "It is a Consonant")

#program10
num = int(input("Enter the year: "))
if num%4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")
