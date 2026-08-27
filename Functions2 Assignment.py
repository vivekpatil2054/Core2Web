#program1
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maximum(10, 25, 15))

#program2
def square(n):
    return n * n

print(square(5))

#program3
def cube(n):
    return n ** 3

num = 5
print("Cube:", cube(num))

#program4
def sum(num1, num2):
    total = 0

    while num1 <= num2:
        total += num1
        num2 += 1
    return total

print(sum(1, 10))

#program5
def marks():
    total = 0
    count = 1
    while count <= 5:
        marks = float(input("Enter marks for subject: "))
        total += marks
        count += 1
    average = total / 5
    return average
result = marks()
print("Average marks =", result)

#program6
def product(n):
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i += 1
    return result
print(product(5))

#program7
def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i += 1
    return fact
num = 5
print("Factorial:", factorial(num))

#program8
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return False
        i += 1
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#program9
def is_composite(n):
    if n <= 3:
        return False
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return True
        i += 1
    return False
num = int(input("Enter a number: "))

if is_composite(num):
    print("Composite Number")
else:
    print("Not a Composite Number")

#program10
def is_perfect(n):
    if n <= 1:
        return False
    i = 1
    total = 0
    while i < n:
        if n % i == 0:
            total += i
        i += 1
    return total == n
num = int(input("Enter a number: "))
if is_perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")