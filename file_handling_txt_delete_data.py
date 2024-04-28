#clear the content of the file.file become empty
f=open(r'C:\Users\s\OneDrive\Desktop\abc.txt','r+')
data=f.read()
print(data)
f.truncate(0)
print(f.read())
f.close()