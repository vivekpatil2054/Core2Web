#program1
listobj = [10,"kanha",10.5,True]
print(listobj)
print(listobj[0])
print(listobj[3])
print(listobj[4])

#program2
listobj = [10,"kanha",10.5,True]
print(listobj)
print(listobj[0])
print(listobj[3])
print(listobj[4])
print(listobj[1:])
print(listobj[1:4])
print(listobj[:4])
print(listobj[::2])
print(listobj[-1])
print(listobj[-4])
print(listobj[-4:-1])

#prporam3
listobj = [10,"kanha",10.5,True]
print(listobj)
print(listobj[0])
print(listobj[3])
print(listobj[4])
print(listobj[1:])
print(listobj[1:4])
print(listobj[:4])
print(listobj[::2])
print(listobj[-1])
print(listobj[-4])
print(listobj[-4:-1])

#program4
listobj = [10,"kanha",10.5,True]
print(listobj)
print(listobj[0])
print(listobj[3])
print(listobj[4])
print(listobj[1:])
print(listobj[1:4])
print(listobj[:4])
print(listobj[::2])
print(listobj[-1])
print(listobj[-4])
print(listobj[-4:-1])
print(listobj[-1:-4])
print(listobj[-4:-1:])
print(listobj[-1:-4:-1])
print(listobj[::-2])

#program5
listobj = [10,20,30,40,50]
print(listobj)
listobj[3]= 35
print(listobj)

#program6
listobj = ["ashish",10,20.5,True,"kanha"]
print(listobj)
for i in range(len(listobj)):
    print(listobj[1])

i = 0
while i < len(listobj):
    print(listobj[i])
    i = i + 1

#Methods of List
#program7
listobj = [10,20,30,40,50]
print(listobj)
listobj.append(35)
print(listobj)
listobj.insert(2,25)
print(listobj)
listobj.extend([60,65])
print(listobj)

#program8
listobj = [10,20,30,40,50]
print(listobj)
listobj.append(35)
print(listobj)
listobj.insert(2,25)
print(listobj)
listobj.extend([60,65])
print(listobj)
listobj.extend(75)
print(listobj)

#program8
listobj = [10,20,30,40,50]
print(listobj)
listobj.append(35)
print(listobj)
listobj.insert(2,25)
print(listobj)
listobj.extend([60,65])
print(listobj)
listobj.extend(75)
print(listobj)
listobj.extend("kanha")
print(listobj)

#program10
listobj = [10,20,30,40,50]
print(listobj)
listobj.remove(1)
print(listobj)

#program11
listobj = [10,20,30,40,50]
print(listobj)
listobj.remove(5)
print(listobj)

#program12
listobj = [10,20,30,40,50]
print(listobj)
listobj.remove(30)
print(listobj)
listobj.pop()
print(listobj)
listobj.pop(2)
print(listobj)
listobj.pop(10)
print(listobj)

#program13
listobj = [10,20,30,40,50]
print(listobj)
listobj.remove(30)
print(listobj)
listobj.pop()
print(listobj)
listobj.pop(2)
print(listobj)
# listobj.pop(10)
# print(listobj)
listobj.clear()
print(listobj)

#program14
listobj = [10,20,30,40,50]
print(listobj)
listobj.remove(30)
print(listobj)
listobj.pop()
print(listobj)
listobj.pop(2)
print(listobj)
listobj.pop(10)
print(listobj)
listobj.clear()
print(listobj)
del listobj[0]

#program15
listobj = [10,20,30,40,50]
print(listobj)
listobj.remove(30)
print(listobj)
listobj.pop()
print(listobj)
listobj.pop(2)
print(listobj)
listobj.pop(10)
print(listobj)
listobj.clear()
print(listobj)
del listobj[0]
print(listobj)

#program16
listobj = [20,25,10,45,30]
print(listobj)
listobj.sort()
print(listobj)
listobj.reverse()
print(listobj)

#program17
listobj = [20,25,10,45,30]
print(listobj)
listobj.sort(reverse=True)
print(listobj)
listobj.reverse()
print(listobj)

#Nested List
#program18
listobj = [[10,20,30],[40,50]]
print(listobj)
print(listobj[1])

#program19
listobj = [[10,20,30],[40,50]]
print(listobj)
print(listobj[1])
print(listobj[1][2])

#program20
listobj = [[10,20,30],[40,50,[55,56,57]]]
print(listobj)
print(listobj[1])
print(listobj[1][2])
print(listobj[1][1])

#program21
listobj = [[10,20,30],[40,50,[55,56,57]]]
print(listobj)
print(listobj[1])
print(listobj[1][2])
print(listobj[1][1])
print(listobj[1][2][1])

#Shallow Copy

#program22
listobj1 = [[10,20],[40,50,60]]
print(listobj1)
listobj2 = listobj1
print(listobj2)
print(listobj1 is listobj2)

#program23
listobj1 = [[10,20],[40,50,60]]
print(listobj1)
listobj2 = listobj1
print(listobj2)
print(listobj1 is listobj2)
listobj1[0][2]= 35
print(listobj1)
print(listobj2)

#Shallow Copy

#program24
import copy
listobj1 = [[10,20,30],[40,50,60]]
print(listobj1)
listobj2 = copy.copy(listobj1)
print(listobj2)

#Deep Copy

#program25
import copy
listobj1 = [[10,20,30],[40,50,60]]
print(listobj1)
listobj2 = copy.deepcopy(listobj1)
print(listobj2)














