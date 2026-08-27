#program1
def area_of_square(side):
    return side * side

length = float(input("Enter the length of the square: "))
area = area_of_square(length)
print("Area of the square:", area)

#program2
def cube(num):
    return num ** 3

num = int(input("Enter a number: "))
result = cube(num)
print("Cube of", num, "is", result)

#program3
def find_max(numbers):
    return max(numbers)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
maximum = find_max(numbers)
print("Maximum number is:", maximum)

#program4
def rectangle_area(length, width):
    return length * width

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = rectangle_area(length, width)
print("Area of rectangle =", area)

#program5
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Temperature in Fahrenheit:", fahrenheit)

#program6
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print("Temperature in Celsius:", celsius)

#program7
def last_digit(n):
    return abs(n) % 10

num = int(input("Enter a number: "))
print("Last digit is:", last_digit(num))

#program8
def perimeter_of_square(length):
    return 4 * length

length = float(input("Enter the length of the square: "))
perimeter = perimeter_of_square(length)
print("Perimeter of the square:", perimeter)

#program9
def contains_a(s):
    return 'a' in s

text = input("Enter a string: ")
if contains_a(text):
    print("The string contains 'a'.")
else:
    print("The string does not contain 'a'.")

#program10    
def check_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if check_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")