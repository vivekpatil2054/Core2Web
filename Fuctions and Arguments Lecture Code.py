#code1
def fun():
    print("start fun")
    print("In fun")
    print("end code")

print("start code")

#2
def fun():
    print("start fun")
    print("In fun")
    print("end code")

print("start code")
fun()
print("End code")

#3
def fun():
    print("start fun")
    print("In fun")
print("end code")

print("start code")
fun()
print("End code")

#4
def add(x,y):
    print(x+y)
add(10,20)

#5
def add(x,y):
    print(x+y)
add(10)    
add(10,20)
add(50,30)

#Positional Arguments
#1
def empdata(empname,empid):
    print("Employee Name:",empname)
    print("Employee ID:",empid)
print("start code")
empdata("kahna",30)  #postioinal 
empdata(40,"rahul")
print("End Code") 

#Keyword Arguments
#1
def empdata(empname,empid):
    print("Employee Name:",empname)
    print("Employee ID:",empid)
print("start code")
empdata("kahna",30)  #postioinal 
empdata(empid=40,empname="rahul") #keyword
print("End Code") 

#2
def empdata(empname,empid):
    print("Employee Name:",empname)
    print("Employee ID:",empid)
print("start code")
empdata(empname="kahna",empid=30)  #postioinal 
empdata(empid=40,empname="rahul") #keyword
print("End Code") 

#3
def playerdata(playername,jerno,country):
    print(playername)
    print(jerno)
    print(country)
playerdata("virat",18,"India") 
playerdata("rohit",45,"India")
playerdata("Aus","warner",3)

#4
def playerdata(playername,jerno,country):
    print(playername)
    print(jerno)
    print(country)
playerdata("virat",18,"India") 
playerdata("rohit",45,"India")
playerdata(country="Aus",playername="warner",jerno=3)

#Default Arguments
#1
def playerdata(playername,jerno,country="India"):
        print(playername)
        print(jerno)
        print(country)
playerdata("virat",18,) 
playerdata("rohit",45,"India")
playerdata(country="Aus",playername="warner",jerno=3)

#2
def playerdata(playername,jerno=25,country="India"):
        print(playername)
        print(jerno)
        print(country)
playerdata("virat",18,) 
playerdata("hardik")
playerdata("rohit",45,"India")
playerdata(country="Aus",playername="warner",jerno=3)

#Var-args Arguments
#1
def fun(data):
     print(data)
fun(10)

#2
def fun(*data):
     print(data)
fun()
fun(10)
fun(10,20)
print(10,20,30)
print(10,20,30,"kahna",5,20.5)    

#3
def fun(*data):
     print(data)
fun()
fun(10)
'''
fun(10,20)
print(10,20,30)
print(10,20,30,"kahna",5,20.5)  
'''

#4
def fun(*data):
     for i in data:
          print(i)
fun()
fun(10)
fun(10,20)
print(10,20,30)
print(10,20,30,"kahna",5,20.5)  

#keywords var-args
#1
def playerdata(playername,jerno):
     print(playername)
     print(jerno)
playerdata("virat",18)
playerdata("rohit",45)

#2
def fun(**data):
     for i,j in data.items():
          print(i,":",j)
fun(jerno=45)
def fun(**data):
     for i,j in data.items():
          print(i,":",j)
fun(jerno=18,playername="virat",runs=18)                    

#3
def fun(**data):
     for i,j in data.items():
          print(i,":",j)
fun(jerno=45)
fun(jerno=18,playername="virat",runs=18)

#4
def fun(*args,**kwargs):
     for i in args:
          print(i)
     for i,j in kwargs.items():
          print(i,":",j)
fun(jerno=45)
fun(10,20,30,rno=18,playername="virat",runs=50000)

#5
def fun(*args,**kwargs):
     for i in args:
          print(i)
     for i,j in kwargs.items():
          print(i,":",j)
fun(jerno=45)
fun(10,20,30,40,50,60,rno=18,playername="virat",runs=50000)