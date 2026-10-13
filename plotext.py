#to import a libaray
#program1
import math
print(dir(math))

#program2
import pip
print(dir(pip))

#program2
import plotext as plt
print(dir(plt))

#For List
#program4
import plotext as plt
list1 = [10,20,30,40]
plt.plot(list1)
plt.show()

#program5
import plotext as plt
list1 = [10,20,30,40]
plt.plot(list1)
plt.scatter(x,y)
plt.title("demoplot")
plt.show()

#For Tuple
#program6
month = ("june","july","august","september")
rainfall = [20.5,33,2,20,10]

plt.bar(month,rainfall)
plt .title("rainfall")
plt.show()

#For set
#program7
import plotext as plt
votes = ["yes","no","yes","yes","maybe","no"]

uniquedata = set(votes)
print(uniquedata)
print(type(uniquedata))

#program8
import plotext as plt
votes = ["yes","no","yes","yes","maybe","no"]

uniquedata = set(votes)
print(uniquedata)
print(type(uniquedata))

print("#########")

uniquedata = list(uniquedata)

print(uniquedata)
print(type(uniquedata))

result = []

#program9
print(uniquedata)
print(type(uniquedata))

print("#########")

uniquedata = list(uniquedata)

print(uniquedata)
print(type(uniquedata))

result = []

for x in uniquedata:
    result.apppend(votes.count(x))
print(result)

#program10
print(uniquedata)
print(type(uniquedata))

print("#########")

uniquedata = list(uniquedata)

print(uniquedata)
print(type(uniquedata))

result = []

for x in uniquedata:
    result.apppend(votes.count(x))
print(result)

plt.bar(uniquedata,result)
plt.title("exitpoll")
plt.show()

#program11
import plotext as plt

fruit_inventory = {
    "apples":45,
    "bananas":70,
    "oranges":32,
    "grapes":55
}

fruits = list(fruit_inventory.keys())
quantities = list(fruit_inventory.values())

plt.title("friut inventory levels")
plt.xlabel("fruit type")
plt.ylabel("quantity")

plt.show()

