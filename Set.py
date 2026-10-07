#program1
setobj = {10,20,30,10,20}
print(setobj)

#program2
setobj = {10,20,30,10,20,40}
print(setobj)

#Creating Sets
#program3
setobj1 = {10,20,30}
print(setobj1)
print(type(setobj1))

setobj2 = {}
print(setobj2)
print(type(setobj2))

#program4
setobj1 = {10,20,30}
print(setobj1)
print(type(setobj1))

setobj2 = set()
print(setobj2)
print(type(setobj2))

setobj3 = set({40,50,60})
print(setobj3)
print(type(setobj3))

#Why set is unordered
#program5
setobj1 = {10,20,30,40}
print(setobj1)

#program6
print(hash(10))
print(hash("shashi"))

#program7
setobj1 = {10,20,30,10,20,40,50}
print(setobj1)

#program8
setobj2 = {10,20,30,40,50,60,70}
print(setobj2)

#program9
setobj3 = {10,"kanha",20.6,10,True,1,0.1}
print(setobj3)

#Accessing Set elememts
#program10
setobj1 = {10,20,30,40}
print(setobj1)
print(setobj1[2])

#program11
setobj1 = {10,20,30,40}
print(setobj1)
for i in setobj1:
    print(i)

#Adding elements to set

#Add()
#program12
setobj1 = {10,20,30}
print(setobj1)
setobj1.add(50)
print(setobj1)
setobj1.add(60)
print(setobj1)
setobj1.add(70)
print(setobj1)

#Update()
#program13
setobj2 = {10,20,30}
print(setobj2)
setobj.update([140,150])
print(setobj2)
setobj3 = {110,120,130}
print(setobj3)

listobj = {10,20,30}

setobj3.update(listobj)
print(setobj3)
setobj3.set(listobj)
print(setobj3)

#Removing elements from set
#remove()
#program14
setobj1 = {10,20,30,40}
print(setobj1)
setobj1.remove(2)
print(setobj1)

#program15
setobj1 = {40,10,20,30}
print(setobj1)
setobj.remove(2)

#Discard()
#program16
setobj1 = {10,20,30,40}
print(setobj1)
setobj1.discard(30)
print(setobj1)
setobj1.discard(3)
print(setobj1)

#Pop()
#program17
setobj1 = {10,20,30,40,44,33,22,5,67,22}
print(setobj1)
setobj1.pop()
print(setobj1)
setobj1.pop()
print(setobj1)
setobj1.pop()
print(setobj1)

#clear()
#program18
setobj1 = {10,20,30,40,44,33,22,5,67,22}
print(setobj1)
setobj1.clear()
print(setobj1)

#Set operations
#program19
setobj1 = {1,2,3}
setobj2 = {3,4,5}
#union
print(setobj1|setobj2)
print(setobj1.union(setobj2))

#intersection
print(setobj1&setobj2)
print(setobj1.intersection(setobj2))

#difference
print(setobj1 - setobj2)
print(setobj2 - setobj1)
print(setobj1.difference(setobj2))

#symmetric differnece
print(setobj1^setobj2)
print(setobj1.symmetric_difference(setobj2))

#Frzoen Set
#program20
fzobj = frozenset({10,20,30,10,20})
print(fzobj)
print(type(fzobj))

fzobj.add(40)
print(fzobj)





