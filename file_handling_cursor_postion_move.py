#tell()-to get position of cursor
f=open(r'C:\Users\s\OneDrive\Desktop\scr.txt','r')
print(f.tell())
f.readline()
print(f.tell())
f.read()
print(f.tell())

#seek()-to move cursor position
print(f.read())
f.seek(0)
# print(f.read())
f.close()

#when we append cursor will move to the end of lien and if we go for read we get nothing
f1=open(r'C:\Users\s\OneDrive\Desktop\scr.txt','a+')
f1.write("hello")
print(f1.read())
f1.close()

f=open(r'C:\Users\s\OneDrive\Desktop\scr.txt','a+')
f.write("ashish")
f.seek(0)
print(f.read())