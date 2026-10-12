#program1
fileobj = open("core2web.txt","r")

#program2
fileobj = open("core2web.txt","r")

#program3
fileobj = open("core2web.txt","r")
data = fileobj.read()
print(data)

#program4
fileobj = open("core2web.txt","r")
data = fileobj.read()
print(data)

#program5
fileobj = open("core2web.txt","w")
data = fileobj.read()
print(data)

#program6
fileobj = open("core2web.txt","r")
print(type(fileobj))
print(fileobj)
print(data)

#program7
fileobj = open("core2web.txt","r")
print(type(fileobj))
print(fileobj)
data = fileobj.read()
print(data)

#program8
fileobj = open("incubators.txt","r")
print(type(fileobj))
print(fileobj)
data = fileobj.read()
print(data)

#program10
fileobj = open("core2web.txt","a")
fileobj.write("frontend")

#program11
fileobj = open("core2web.txt","a")
fileobj.write("frontend")
data = fileobj.read()
print(data)

#program12
fileobj = open("core2web.txt","a+")
fileobj.write("frontend")
data = fileobj.read()
print(data)

#program13
fileobj = open("core2web.txt","a+")
fileobj.write("frontend")
fileobj.seek(0)
data = fileobj.read()
print(data)

#program14
fileobj = open("core2web.txt","r+")
data = fileobj.read()
print(data)

#program15
fileobj = open("core2web.txt","r+")
fileobj.write("backend")
data = fileobj.read()
print(data)

#program16
fileobj = open("core2web.txt","r+")
fileobj.write("backend")
print(data)
data = fileobj.read()
fileobj.seek(0)
data = fileobj.read()
print(data)

#program17
fileobj = open("core2web.txt","r+")
fileobj.write("backend")
print(data)
data = fileobj.read()
fileobj.seek(0)
data = fileobj.read()
print(data)
fileobj.seek(10)
value = fileobj.readline()
print(value)

#program18
fileobj = open("core2web.txt","r+")
fileobj.write("dart")
fileobj.seek(0)
data = fileobj.read()
print(data)

#program19
fileobj = open("core2web.txt","r+")
fileobj.writelines("java\n","abcdef\n")
fileobj.seek(0)
data = fileobj.read()
print(data)

#program21
fileobj = open("core2web.txt","r+")
fileobj.writelines("java\n","abcdef\n")
fileobj.seek(10)
data = fileobj.read()
print(data)

#program20
fileobj = open("core2web.txt","r+")
fileobj.writelines("java\n","abcdef\n")
fileobj.seek(12)
data = fileobj.read()
print(data)

#program21
fileobj = open("core2web.txt","r+")
# fileobj.writelines("java\n","abcdef\n")
# fileobj.seek(10)
print(fileobj.tell())

#program22
fileobj = open("core2web.txt","r")
data = fileobj.read()
print(data)
fileobj.close()
fileobj.write("frontend")

#program23
with open ("core2web.txt","r") as fileobj:
    data = fileobj.read()
    print(data)

#program24
fileobj = open("/root/test.txt","r")

#program25
fileobj = open("core2web.txt","r")
print(fileobj)
print(type(fileobj))

#program26
filelist = []
while True:
    with open ("core2web.txt","r") as fobj:
        filelist.append(fobj)
        print(filelist)

#program27
# filelist = []
# while True:
#     #with open ("core2web.txt","r") as fobj:
#         filelist.append(fobj)
#         print(filelist)

#program28
import pickle
fobj = open("Incubators.pkl","wb")
player = {18:"virat",45:"rohit",7:"msd"}
pickle.dump(player,fobj)
fobj.close()

#program29
import pickle
fobj = open("Incubators.pkl","wb")
player = {18:"virat",45:"rohit",7:"msd"}
pickle.dump(player,fobj)
fobj.seek(0)
obj = pickle.load(fobj)
print(obj)
fobj.close()

#program30
import pickle
fobj = open("Incubators.pkl","wb")
player = {18:"virat",45:"rohit",7:"msd"}
pickle.dump(player,fobj)
pickle.dump(data,fobj)
fobj.seek(0)
obj1 = pickle.load(fobj)
obj2 = pickle.load(fobj)
print(obj1)
print(obj2)

#program31
import pickle
fobj = open("Incubators.pkl","wb")
player = {18:"virat",45:"rohit",7:"msd"}
pickle.dump(player,fobj)
pickle.dump(data,fobj)
fobj.seek(0)
obj1 = pickle.load(fobj)
obj2 = pickle.load(fobj)
print(obj1)
print(obj2)
fobj.close()

















