#loop works on sequence like list tuple set string range
def prog1():
    for i in 1,5,7:
        print(i)
        print("hello")
prog1()

def prog2():
    for x in '1','amit','yash','delhi':
        print(x)
prog2()

a=[1,2,3,4,5,6]
def prog3():
    for y in a:
        print(y)
prog3()


def prog4():
    for v in range(5):
        print("Hi")
prog4()

def prog5():
    for t in range(len(a)):
        print(t)
prog5()

def prog6():
    for l in range(1,10,2):
        print(l)
prog6()