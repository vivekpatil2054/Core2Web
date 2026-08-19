#program1
age = int(input("Enter the age: "))
weight = int(input("Enter the weight: "))
Hb = float(input("Enter the Hb: "))
if age < 18 and weight < 50 and Hb < 12.5:
    print("you are eligible for blood donation")
elif age > 18 and weight > 50 and Hb > 12.5:
    print("you are not eligible for blood donation")
else:
    print("you are not donate the blood")

#program2
marks = int(input("Enter the marks: "))
if marks >= 90 and marks <= 100 :
    print("A+")
elif marks >= 80 and marks <=89:
    print("A")
elif marks >= 70 and marks <=79:
    print("B")
elif marks >= 60 and marks <=69:
    print("C")
elif marks >= 50 and marks <=59:
    print("D")
else:
    print("Fail")

#program3
units = int(input("Enter the units: "))
if units >= 300:
    print("Rs 15/unit") 
elif units >= 201 and units <= 300:
    print("Rs 10/unit")
elif units >= 101 and units <= 320:
    print("Rs 7/unit")
elif units >= 201 and units <= 300:
    print("Rs 5/unit")
else:
    print("Rs 0/unit")

#program4
income = int(input("Enter the income: "))
if income <= 250000:
    print("No tax")
elif income >= 250000 and income <= 500000:
    print("5%")
elif income >= 500001 and income <= 10000000:
    print("20%")
else:
    print("30%")

#program5
temp = int(input("Enter the temperature: "))
if temp <= 0:
    print("Below 0")
elif temp >= 0 and temp <= 10:
    print("very cold")
elif temp >= 11 and temp <= 20:
    print("cold")
elif temp >= 21 and temp <= 30:
    print("warm")
elif temp >= 31 and temp <= 40:
    print("Hot")
else:
    print("extreme heat")

#prgroam6
ch = input("Enter a single character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

#program7
per = int(input("Enter the percentage: "))
if per >= 90 and per <=100:
    print("Elite Program")
elif per >= 80 and per <= 90:
    print("Standard program")
elif per >= 50 and per <= 80:
    print("Basic program")
else:
    print("Not eligible")

#pragram8
num = int(input("Enter a number: "))

if num == 0:
    print("0")
elif num > 0 and num % 2 == 0:
    print("+ve even number")
elif num > 0 and num % 2 != 0:
    print("+ve odd number")
elif num < 0 and num % 2 == 0:
    print("-ve even number")
else:
    print("-ve odd number")

#prgroam9
amo = int(input("Enter the amount: "))
if amo < 1000:
    print("no discount")
elif amo > 1000 and amo < 4999:
    print("5%")
elif amo > 5000 and amo < 9999:
    print("10%")
elif amo > 10000 and amo < 19999:
    print("20%")
else:
    print("30%")

#program10
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c != 180:
    print("Invalid triangle")
elif a >= 90 or b >= 90 or c >= 90:
    print("Obtuse triangle")
else:
    print("Acute triangle")





