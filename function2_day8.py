#type of parameterized function

#1-required parameter
def info(id,name,salary,city):
    print(f"{id},{name},{salary},{city}")
info(1,'ashish',10000,'jaunpur')

#2-keyword argument/name argument
def info1(id,name,city,salary):
    print(f"{id},{name},{salary},{city}")
info1(name='ashish',salary=10000,city='jaunpur',id=1)

#3-Default argument- always should be in right
def info2(id,name,city,salary=25000):
    print(f"{id},{name},{salary},{city}")
info2(name='ashish',city='jaunpur',id=1)


#4-Variable length argument
def add(*n):
    result=0
    for i in n:
        result=result+i
    print(result)
add(2,3,5)

#5-keyword variable length argument
def adduser(**var):
    print(var)
    print(var['name'])
adduser(name='root',password='redhat')
