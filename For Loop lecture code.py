#1
data = [1,2,3,4,5]
print(data[2])

#2
data = [0,1,2,3,4,5]
for x in data:
    print(x)

#3
for x in range(1,5,2):
    print(x)

#4
for x in range(1,10,3):
    print(x)    

#5
for x in range:
    print("c2w")

#6
for x in range(5,0,-1):
    print(x)

#7 
for x in range(0,5):
    print("c2w",end=" ")

#8
for x in range(0,5):
    print("c2w")
    for y in range(2):
        print("python")

#9
for i in range(3):
    for j in range(2):
        print("c2w")        

#4
for i in range(3):
    for j in range(3):
        print("*") 
    print()
   
#5
for i in range(3):
    for j in range(3):
        print("*",end= " ") 
    print()

#6  
for i in range(3):
    for j in range(1,3):
        print(j,end=" ") 
    print()

#7
for i in range(2,3):
    for j in range(1,3):
        print(i,"\t") 
    print()

#8
for i in range(1,4):
    for j in range(1,4):
        print(i*j,end="\t") 
    print()

#9
for i in range(1,4):
    for j in range(1,4):
        print(i+j,end="\t") 
    print()

#10
for i in range(128):
        print(y,"=",chr(y)) 

#11
for i in range(4):
    for j in range(2):
        if y % 2 == 0:
          print("c2w") 
    print()

#12
for i in range(3):
    for j in range(2):
        if y%2 == 0:
          print(x,end=" ") 
    print()
   
#13
for i in range(4):
    for j in range(3):
        if x % 2 == 0:
           print("#",end="") 
        else:
            print("$",end="\t")
        print()    

#14
rows = int(input("Enter rows: "))
for i in range(1,rows + 1):
    for j in range(3):
        if i% 3 == 1:
            print("#",end="\t")
        elif i%3 == 2:
            print("$",end="\t")
        else:
            print("@",end="\t")    
    print()

#15
rows = int(input("Enter rows: "))
for i in range(rows):
    for j in range(4):
        if i% 4 == 0:
            print("#",end="\t")
        elif i%4 == 1:
            print("$",end="\t")
        elif i%4 == 2:
            print("@",end="\t")
        else:
            print("*",end="\t")    
    print()


   

     
   
