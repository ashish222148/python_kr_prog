#local variable=declare inside function, and can be accessible within the function
#global function =declare outside function and can be accessible inside and ouside the function
p1=100
def m1():
    global q1
    q1=200 # First we declare then assign
    g1=300
m1()
def m2():
    print(q1)
    print(p1)
    print(g1) # can not be accessed as it is local variable
m2()
