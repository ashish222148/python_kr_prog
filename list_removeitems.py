data=[10,'amit',23,'delhi',4000,'delhi','delhi']
for item in data:
    if item=='delhi':
        data.remove(item)
print(data)

data1=[10,'amit',23,'delhi',4000,'delhi','delhi']
for item1 in range(data1.count('delhi')):
    data1.remove('delhi')
print(data1)