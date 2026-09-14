#program1
def fun(x):
    print(x)
fun(10)

#program2
def fun(x):
    print(x)
print(fun)

#program3
def fun(x):
    print(x)
def run():
    print("In run")
print(fun)
print(run)

#program4
def fun(x):
    print(x)
def run():
    print("In run")
fun(run)

#program5
def fun(x):
    print(x)

    x()
def run():
    print("In run")
fun(run)

#program6
def fun(funcref):
    funcref()
def run():
    print("In run")
fun(run)

#program7
def outerfun(funcref):
    def innerfunc():
        print("start inner function")

        funcref()
        print("end inner function")

        return innerfunc
def run():
    print("In run")
retref = outerfun(run)
retref()

#program8
def outerfun(funcref):
    def innerfunc():
        print("start inner function")

        funcref()
        print("end inner function")

        return innerfunc
def run():
    print("In run")
retref = outerfun(run)
print(retref.__closure__)
retref()

#program9
def outerfun(funcref):
    def innerfunc():
        print("start inner function")

        funcref()
        print("end inner function")

        return innerfunc
def run():
    print("In run")
retref = outerfun(run)
print(hex(id(run)))
print(retref.__closure__)
retref()

#program10
def outerfun(funcref):
    def innerfunc():
        print("start inner function")

        funcref()
        print("end inner function")

        return innerfunc
def run():
    print("In run")
retref = outerfun(run)
print(retref.__closure__)
retref()

#program12
def outerfun(funcref):
    def innerfunc():
        print("start inner function")

        funcref()
        print("end inner function")

        return innerfunc
def run():
    print("In run")
retref = outerfun(run)
retref()

#program13
def outerfun(funcref):
    def innerfunc():
        print("start inner function")

        funcref()
        print("end inner function")

        return innerfunc
def run():
    print("In run")
retref = outerfun(run)
print(hex(id(run)))
print(retref.__closure__)
retref()

#program14
def outerfun(funcref):
    def innerfunc():
        print("start inner function")

        funcref()
        print("end inner function")

        return innerfunc
def run():
    print("In run")
# retref = outerfun(run)
# retref()

#program15
def outerfun(funcref):
    def innerfunc():
        print("start inner function")

        funcref()
        print("end inner function")

        return innerfunc
def run():
    print("In run")
retref = outerfun(run)
retref()
run()


