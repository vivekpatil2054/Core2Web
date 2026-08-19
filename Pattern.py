#program1
rows = int(input("Enter the rows: "))
for i in range(rows):
    num = 1
    for j in range(rows):
        print(num,end="\t")
        num += 2
    print()    

# #program2
rows = int(input("Enter the rows: "))

num = 1

for i in range(rows):
    for j in range(rows):
        print(num, end="\t")
        num += 1
    print()

#program3
rows = int(input("Enter the rows: "))

num = 1

for i in range(rows):
    for j in range(4):
        print(num, end="\t")
        num += 2
    num -= 4
    num += 8
    print()

#program4
rows = int(input("Enter the rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="\t")
    print()

#program5
rows = int(input("Enter the rows: "))

for i in range(1, rows + 1):
    for j in range(4, 4 - i, -1):
        print(j, end=" ")
    print()

#program6
rows = int(input("Enter the rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="\t")
    print()

#program7
rows = int(input("Enter the rows: "))

for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end="\t")
    print()

#program8
rows = int(input("Enter the rows: "))

for i in range(rows, 0, -1):
    print("   " * (rows - i), end="")
    
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()

#program9
rows = int(input("Enter the rows: "))

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print("   ", end="")

    # Print numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    print()

#program10
rows = int(input("Enter the rows: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print("   ", end="")

    for j in range(rows, rows - i, -1):
        print(j, end=" ")

    print()





