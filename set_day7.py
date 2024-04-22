#set is collections of unique items
#{}
#item will not be store based on index
#mutable
#unordered data collectio
x={10:15}
print(type(x))
y={10,15,15}
print(type(y))
print(y)
s1={10,5,2,4,9,7,5,8}
s2={8,6,2,1,4,7,9,5}
print(s1)
print(s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
