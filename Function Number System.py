#program1
def digitcount(x):
    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count

def sepdigit(x):
    while x > 0:
        rem = x % 10
        print(rem)
        x //= 10

def isduck(x):
    temp = x 
    flag = False

    while temp > 0:
        rem = temp % 0
        if rem == 0:
            flag = True
            break
        temp //= 10
    if flag:
        return "Duck Number"
    else:
        return "Not Duck Number"

def isPrime(x):
    if x<= 1:
        return "Not Prime"
    for i in range(1,x+1):
        if x % i == 0:
            count += 1
        if count == 2:
            return "Prime Number"
        else:
            return "Not Prime Number"

#program2
def isPrime2(x):
    if x <= 1:
        return "Not Prime"
    prime = True
    for i in range(2,(x // 2)+1):
        if x % i == 0:
            prime = False
            break
        if prime:
            return "Prime Number"
        else:
            return "Not Prime Number"

#program3
def isPrime3(x):
    if x <= 1:
        return "Prime Number"

    i = 2
    prime = True
    while i * i <= x:
        if x % i == 0:
            prime = False
            break
        i += 1
    if prime:
        return "Prime"
    else:
        return "Not Prime"

def isComposite(x):
    if x <= 1:
        return "Not Composite"
    for i in range(2,(x // 2)+1):
        if x % i == 0:
            count += 1
        if count > 0:
            return "Composite Number"
        else:
            return "Not Composite Number"

def properdivisors(x):
    i = 1
    print("proper divisors of",x)

    while i < x:
        if x % i == 0:
            print(i)
        i += 1

def isperfect(x):
    s = 0
    for i in range(1,x):
        s += i
    if s == x:
        return "Perfect"
    else:
        return "Not Perfect"

def isabundant(x):
    s = 0
    i = 1
    while i < x:
        if x % i == 0:
            s += 1
        i += 1
    if s > x:
        return "Abundant"
    else:
        return "Not Abundant"

def isdefficient(x):
    s = 0
    i = 1
    while i < x:
        if x % 1 == 0:
            s += 1
        i += 1
    if s > x:
        return "Deficient"
    else:
        return "Not Deficient"

def revdigit(x):
    reverse = 0
    while x > 0:
        rem = x % 10
        reverse = reverse * 10 + rem
        x //= 10
    return reverse

def ispalindrome(n):
    if n == revdigit(n):
        return "Palindrome"
    else:
        return "Not Palindrome"

def sumof(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

def prodof(x):
    product = 1
    while x > 0:
        product *= x % 10
        x //= 10
    return product

def isspy(x):
    if sumof(x) == prodof (x):
        return "Spy"
    else:
        return "Not Spy"

def isNiven(x):
    temp = x
    sum = sumof (temp)
    if temp % sum == 0:
        return "Niven/Harshad"
    else:
        return "Not Niven/Harshad"

def isneno(x):
    sq = x * x
    sum = 0
    while sq > 0:
        sum += sq % 10
        sq //= 10
    if sum == x:
        return "Neon"
    else:
        return "Not Neon"

def isArmstrong(x):
    temp = x
    power = digitcount(temp)
    sum = 0
    while x > 0:
        rem = x % 10
        sum += rem ** power
        x //= 10
    if sum == temp:
        return "Armstrong"
    else:
        return "Not Armstrong"

def factorial(x):
    prod = 1
    while x > 0:
        prod *= x
        x -= 1
    return prod

def isstrong(x):
    temp = x 
    sum = 0
    while x > 0:
        sum += factorial(x % 10)
        x //= 10
    if sum == temp:
        return "Strong"
    else:
        return "Not strong"

while True:
    print("**************")

    choice = int(input("Enter choice: "))

    if choice not in range(1,20):
        print("Invalid option")
        print("please re-enter choice")
        choice = int(input("Enter choice: "))

        if choice not in range(1,20):
            print("you again missed it,bye...")
            break

        n = int(input("Enter the number:"))
        match choice:
            case 1:
                print("Digit count: ",digitcount(n))
            case 2:
                sepdigit(n)
            case 3:
                print(n,"is",isduck(n))
            case 4:
                properdivisors(n)
            case 5:
                print(n,"is",isPrime(n))
            case 6:
                print(n,"is",isComposite(n))
            case 7:
                print(n,"is",isabundant(n))
            case 8:
                print(n,"is",isperfect(n))
            case 9:
                print(n,"is",isdefficient(n))
            case 10:
                print(n,"is",sumof(n))
            case 11:
                print(n,"is",prodof(n))
            case 12:
                print(n,"is",isspy(n))
            case 13:
                print(n,"is",isNiven(n))
            case 14:
                print(n,"is",isneno(n))
            case 15:
                print(n,"is",revdigit(n))
            case 16:
                print(n,"is",ispalindrome(n))
            case 17:
                print(n,"is",isstrong(n))
            case 18:
                print(n,"is",factorial(n))
            case 19:
                print(n,"is",isArmstrong(n))

        again = input("Do you want to continue? (y/yes):".lower())
        if again not in ('y','yes'):
            print("Thank you for using Number checker! see ya!")

            break
    
        




