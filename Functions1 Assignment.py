#program1
def func():
    x = 10
    print("In func x: ",x)
func()

#program2
def func(x):
    if x % 2 == 0:
        print("Even No")
    else:
        print("Odd no")
func(12)
func(11)

#program3
def func(x):
    if x < 18:
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")
func(12)
func(41)

#program4
def func(a, b):
    print("Add:", a + b)
    print("Sub:", a - b)
    print("Mult:", a * b)
    print("Div:", a / b)
    print("Floor Division :", a // b)
    print("Mod:", a % b)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

func(num1, num2)

#program5
def func(char):
    if char.lower() in "aeiou":
        print("The character is a Vowel")
    else:
        print("The character is a Consonant")

ch = input("Enter a character: ")
func(ch)

#program6
def func(char):
    print("ASCII value of", char, "is:", ord(char))

ch = input("Enter a character: ")
func(ch)

#program7
def max(a, b):
    if a > b:
        print("Maximum number is:", a)
    else:
        print("Maximum number is:", b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
max(num1, num2)

#program8
def func(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

func(name="Vinay", age=22, course="Btech")

#program9
def average(*args):
    total = sum(args)
    avg = total / len(args)
    print("Average:", avg)

average(10, 20, 30, 40, 50)

#program10
import math

def circle_area(radius):
    return math.pi * radius * radius

radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)

print("Radius:", radius)
print("Area of circle:", area)



