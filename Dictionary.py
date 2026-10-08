#program1
player=-{18:"virat",7:"MSD",45:"rohit"}
print(player)

#program2
player=-{18:"akaay",7:"MSD",45:"rohit"}
print(player)

#program3
player={18:"virat",7:"msd",45:"rohit","jadeja":8}
print(player)

#object creation of dictionary
#program4
dictobj1 = {}
print(dictobj1)
print(type(dictobj1))

#program5
dictobj1 = {}
print(dictobj1)
print(type(dictobj1))
dictobj2 = dict()
print(dictobj2)
print(type(dictobj2))
dictobj3 = dict({18:"virat",7:"msd"})
print(dictobj3)
print(type(dictobj3))

#program6
dictobj1 = {}
print(dictobj1)
print(type(dictobj1))
dictobj2 = dict()
print(dictobj2)
print(type(dictobj2))
# dictobj3 = dict({18:"virat",7:"msd"})
# print(dictobj3)
# print(type(dictobj3))

#program7
dictobj1 = {}
print(dictobj1)
print(type(dictobj1))
dictobj2 = dict()
print(dictobj2)
print(type(dictobj2))
dictobj3 = dict({18:"virat",7:"msd"})
print(dictobj3)
print(type(dictobj3))

#program8
dictobj1 = {}
print(dictobj1)
print(type(dictobj1))
dictobj2 = dict()
print(dictobj2)
print(type(dictobj2))
dictobj3 = dict({18:"virat",7:"msd"})
print(dictobj3)
print(type(dictobj3))

#program9
dictobj1 = {1:"kanha","age":25,3.5:True,{10,20}:{1,2},"salary":None}
print(dictobj1)
print(type(dictobj1))

#program10
player=-{18:"virat",7:"MSD",45:"rohit"}
print(player)
print(player[7])
print(player[1])

#program11
player=-{18:"virat",7:"MSD",45:"rohit"}
print(player)
print(player[7])
print(player[1])
try:
    print(player[1])
except KeyError:
    print("key not error")
print(player.get(18))

#program12
player=-{18:"virat",7:"MSD",45:"rohit"}
print(player)
player[7]  = "mahi"
print(player)

#program13
player=-{18:"virat",7:"MSD",45:"rohit"}
print(player)
player[7]  = "mahi"
print(player)
print[8] = "jadeja"
print(player)
player.update({1:"klrahul",33:"hardik",18:"chiku"})
print(player)

#Deleting dictionary elements

#program14
player=-{18:"virat",7:"MSD",45:"rohit",33:"hardik"}
print(player)
player.popitem()
print(player)

#program15
player=-{18:"virat",7:"MSD",45:"rohit",33:"hardik"}
print(player)
player.popitem(18)
print(player)

#program16
player=-{18:"virat",7:"MSD",45:"rohit",33:"hardik"}
print(player)
player.popitem(33)
print(player)

#program17
player=-{18:"virat",7:"MSD",45:"rohit",33:"hardik"}
print(player)
player.popitem(18)
print(player)
del player
print(player)

#program18
player=-{18:"virat",7:"MSD",45:"rohit",33:"hardik"}
print(player)
player.popitem(18)
print(player)
del player[45]
print(player)

#program19
player=-{18:"virat",7:"MSD",45:"rohit",33:"hardik"}
print(player)
player.popitem(18)
print(player)
player.clear()
print(player)

#Dictionary methods:keys(),values(),items()
#program20
player1 = {18:"virat",7:"msd",45:"rohit"}
print(player1.keys())

#program21
player1 = {18:"virat",7:"msd",45:"rohit"}
print(player.keys())
print(player.values())
print(player.items())

#program22
player1 = {18:"virat",7:"msd",45:"rohit"}
print(player.keys())
print(player.values())
print(player.items())
#listobj1 = {"shiv","subodh","vishal","govind"}
player1.fromkeys()

#program23
player1 = {18:"virat",7:"msd",45:"rohit"}
print(player.keys())
print(player.values())
print(player.items())
listobj1 = {"shiv","subodh","vishal","govind"}
dictobj1 = player1.fromkeys(listobj1)
print(dictobj1)

#program24
player1 = {18:"virat",7:"msd",45:"rohit"}
print(player.keys())
print(player.values())
print(player.items())
listobj1 = {"shiv","subodh","vishal","govind"}
dictobj1 = player1.fromkeys(listobj1,"core2web")
print(dictobj1)

#program25
player1 = {18:"virat",7:"msd",45:"rohit"}
print(player.keys())
print(player.values())
print(player.items())
listobj1 = {"shiv","subodh","vishal","govind"}
dictobj1 = player1.fromkeys(listobj1,[])
dictobj1["shiv"].append("core2web")
dictobj1["shiv"].append("incubators")
print(dictobj1)

#program26
player1 = {18:"virat",7:"msd",45:"rohit"}
print(player.keys())
print(player.values())
print(player.items())
listobj1 = {"shiv","subodh","vishal","govind"}
dictobj1 = player1.fromkeys(listobj1,())
dictobj1["shiv"].append("core2web")
dictobj1["shiv"].append("incubators")
print(dictobj1)

#program27
player1 = {18:"virat",7:"msd",45:"rohit"}
print(player.keys())
print(player.values())
print(player.items())
listobj1 = {"shiv","subodh","vishal","govind"}
dictobj1 = player1.fromkeys(listobj1,())
dictobj1["shiv"].append("incubators")
print(dictobj1)
player1.setdefault(18,"kohli")
print(player1)

#program28
player1 = {18:"virat",7:"msd",45:"rohit"}
print(player.keys())
print(player.values())
print(player.items())
listobj1 = {"shiv","subodh","vishal","govind"}
dictobj1 = player1.fromkeys(listobj1,())
dictobj1["shiv"].append("incubators")
print(dictobj1)
player1.setdefault(18,"kohli")
print(player1)
player1.setdefault(8,"jedeja")
print(player1)

#program29
player = {31:"warner",32:"maxwell"}
print(player)
for i in player.keys():
    print(i)
for i in player.values():
    print(i)
for k,v in player.items():
    print(k,v)

#program30
player = {45:["DC","MI"],7:["csk","rps"]}
print(player)
player1 = {{"DC","MI"}:"rohit",{"csk","rps"}:"msd"}
print(player1)
player1 = {frozenset({"DC","MI"}):"rohit",frozenset({"csk","rps"}):"msd"}
print(player1)

#shallow copy,deep copy
#program31
player = {"india": {"virat","msd","rohit"}, "austraila": {"warner","maxwell","pointing"}}
print(player["india"])
print(player["india"][2])

player1 = {"india":{"virat","msd","rohit"},"australia":{"warner","maxwell","pointing"}}
print(player1)
player2 = player1
print(player2)
print(player2)
print(id(player1))
print(id(player2))

#program32
import copy
player = {"india": {"virat","msd","rohit"}, "austraila": {"warner","maxwell","pointing"}}
print(player["india"])
print(player["india"][2])

player1 = {"india":{"virat","msd","rohit"},"australia":{"warner","maxwell","pointing"}}
print(player1)
player2 = player1
print(player2)
print(player2)
print(id(player1))
print(id(player2))
player2["india"].append({"kl rahul"})
print(player1)
print(player2)
player2 = copy.copy(player1)
print(id(player1))
print(id(player2))
player2["india"].append({"kl rahul"})
print(player1)
print(player2)
player2 = copy.deepcopy(player1)
print(id(player1))
print(id(player2))

#program33
player1 = {"india":{18:"virat",7:"msd",45:"rohit"},"austraila":{31:"warner",32:"maxwell"}}
print(player1)
print(player2)
print(player1["india"][7])











