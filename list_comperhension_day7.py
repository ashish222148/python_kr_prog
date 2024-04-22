#return value should be at first place, loop and condition may be iterchnage
#PROGRAM -1
data=[23,44,82,90,21,12,9,4,58,35,86]

print([x  for x in data   if x%2==0])

#PROGRAM-2
users=['amit','deepak','root','ramesh','sam']
usr=[x.title() for x in users ]
print(usr)


#PROGRAM-3
#if you are only applying if condition , it will be always after loop but if you are applying both if and else then condtion 
#will be before loop  
G=['M','F','F','M','M','F']
print([1 if j=='M' else 0 for j in G])