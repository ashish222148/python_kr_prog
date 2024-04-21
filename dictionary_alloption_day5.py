#dictionary=collection of keys and values
#dict={key1:val1,key2:value2}
#dictionary: key should be immutable and unique
#dictinary: mutable
d1={'id':101,'name':'amit','age':40,'city':'delhi'}
print(d1)
print(d1['name'])
print(d1.get('name'))
#if key does not exist in dict-will return None
print(d1.get('salary'))
print(d1.get('salary',20000))


#update the value
d1['name']='awnish'
print(d1)

#delete
del d1['name']
print(d1)

#add -f value not provided it will add as None
d1.setdefault('name','amit')
print(d1)
d1.setdefault('salary')
print(d1)

d2={'id':101,'name':'amit','age':40,'city':['noida','delhi']}
print(d2)
print(d2['city'][0])


#clear()
# d1.clear()

#copy()
#d1.copy()

#loop will work on key only not on value
for x in d2:
    print(x)

#to get all the keys in a dict
k=list(d2.keys())
print(k)
#to get all the values from a dictionary
v=list(d2.values())
print(v)
#to get all the items from a dict
a=list(d2.items())
print(a)

for n in d2.items():
    print(n[0])

#this is possible in tuple only
for d,f in d2.items():
    print(d,f)

#pop method
print(d1.pop('name'))
print(d1)

#popitem -only remove last key
print(d1.popitem())
print(d1)
d1.update(d2)
print(d1)

print(dir(dict))