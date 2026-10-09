#Array

#program1
import array
arrobj = array.array('i',[10,20,30,40,50])
print(arrobj)
print(type(arrobj))

#program2
import array
arrobj = array.array('i',[10,20,30,40,50,10,20])
print(arrobj)
print(type(arrobj))

#program3
import array
arrobj = array.array('i',[10,20,30,40,50,10,20])
print(arrobj)
print(type(arrobj))
print(arrobj.typecode)
print(arrobj.itemsize)

#Homogenous elements and continuous allocation
#program4
arrobj1 = array.array('i',[10,20,30,40,50])
arrobj2 = array.array('i',[10,20,30,40,50])
print(arrobj1)
print(arrobj2)

print(arrobj1.buffer_info())
print(arrobj2.buffer_info())

print(id(arrobj1[0]))
print(id(arrobj2[0]))

#Various types of elements
#program5

import array

#integer
arrobj1 = array.array('i',[10,20,30,40,50])
print(arrobj1)

#byte
arrobj2 = array.array('b',[123,124,125,127])
print(arrobj2)

#float
arrobj = array.array('h',[10.5,20.5,30,40.5,50.5])
print(arrobj)

#unicode
arrobj = array.array('i',[10,20,30,40,50])
print(arrobj)

#Accessing array module element

#program6
import array
arrobj = array.array('i',[10,20,30,40,50])
print(arrobj)
print(arrobj[1])
print(arrobj[-1])
print(arrobj[1::2])

#for loop 
for i in arrobj:
    print(i)

#while loop
i = 0
while i < len(arrobj):
    print(arrobj[i])
    i = i + 1

#add element to an array
#program7
import array
arrobj = array.array('i',[10,20,30])
print(arrobj)

#append
arrobj.append(40)
print(arrobj)

arrobj.append(50)
print(arrobj)

#extend
arrobj.extend([50,60])
print(arrobj)

#insert
arrobj.insert(2,25)
print(arrobj)


#program8
import array
arrobj = array.array('i',[10,20,30])
print(arrobj)

#remove
arrobj.remove(30)
print(arrobj)

try:
    arrobj.remove(40)
except ValueError as e:
    print(e)

#pop
arrobj.pop()
print(arrobj)

arrobj.pop(20)
print(arrobj)

#other methods:count(),index(),buffer_info(),reverse(),tolist()

#program9
import array

arrobj = array.array('i',[10,20,30,40,10,20])

print(arrobj.count(20))
print(arrobj.index(20))
print(arrobj.buffer_info())

arrobj.reverse()
print(arrobj)

listobj = arrobj.tolist()
print(arrobj)









