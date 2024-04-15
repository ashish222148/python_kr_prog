#list-collection of objects
x=[101,'amit',23,'delhi',89000]
print(type(x))
print(len(x))
print(x[0])
# for n in x:
#     print(n)
print(x[-1])
try:
    print(x[5])
except Exception as ex:
    print(ex)

#------------------Slicing--------------------

#Golden rule=always starting should be less that end
x=[101,'amit',23,'delhi',89000,'deepak',100,'sam',90,87,122]
print(x[1:4])
print(x[:4])
print(x[4:])
print(x[1:8:2])
print(x[:])
print(list(range(1,8,2)))
print(x[-4:-1])
print(x[-4:-1:2])
print(x[-4:-1:-1])
print(x[4:1:-1])
