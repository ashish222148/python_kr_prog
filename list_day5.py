x=[101,'amit',23,'delhi',45000]
#update in list
x[1]='awnish'
print(x)

#delete from list
del x[3]
print(x)

#get list of method of list
#method is assosiated with perticular behaviour while function is associated with task
# print(dir(list))

#adding -append,insert,extend(only iterable item can be added)
x.append('ashish')
print(x)
x.insert(-1,'yash')
print(x)
x.extend([2,3,5])
print(x)

#Clear the list every time
# x.clear()
print(x)

#copy
y=x
y[1]='avanish'
print(y)
print(x)

y=x.copy()
y[1]='aks'
print(y)
print(x)



#Getting the index of delhi
print(x.index('yash'))
x.append(23)

#count
print(x.count(23))

#pop
print(x.pop())
print(x)

#remove()-first ocuurance
x.remove('yash')
print(x)

#reverse 
x.reverse()
print(x)

#sort
z=[6,8,3,9,10]
z.sort()
print(z)