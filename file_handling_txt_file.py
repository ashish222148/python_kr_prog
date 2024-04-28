f=open(r'C:\Users\s\OneDrive\Desktop\abc.txt','w')
# print(f.name)
# print(f.readable())
# print(f.writable())
# print(f.closed)

#-----------------------------Olny to method is for writing write() and writelines()----------------------

#----------------------------------Write------------------------------------------------

#while writing, it will write in a single line , so that we have to put \n at the end of every line
#1-V-IMP-write will only accept string not list or any other value
f.write("Welcome to KR Network\n")
f.write("Hello\n")
f.write("world\n")
#if string is already multiline then no need to put \n at the end of the line
mt="""sunny
bunny
hunny
"""
f.write(mt)
f.close()


#----------------------------WriteLines-------------------------------------------------------
#we have to put \n at the end of every line
#2-writelines-lines should be in list and string only
st=['line1\n','line2\n','line3\n']
f=open(r'C:\Users\s\OneDrive\Desktop\abc.txt','w')
f.writelines(st)
f.close()
#-------------------**---------------
pt=['line1','line2','line3']
f=open(r'C:\Users\s\OneDrive\Desktop\abc.txt','w')
for i in pt:
    f.write(i)
    f.write('\n')
f.close()

#writelines accepting string
nt="My name is ashish"
lt="second name is arun"
f=open(r'C:\Users\s\OneDrive\Desktop\abc.txt','w')
f.writelines(nt)
f.writelines('\n')
f.writelines(lt)



#----------------------------------------------Reading Data------------------------------------
#------------------Three methods for reading----------------------------------------------------

file=open(r'C:\Users\s\OneDrive\Desktop\scr.txt','r')

#1-read()-read all data from the current cursor position and return in string
data2=file.read(10)
print(data2)
data=file.read()
print(data)
file.close()

#2-readline-read only one line from the current cursor postion and return in to string
file=open(r'C:\Users\s\OneDrive\Desktop\scr.txt','r')
data1=file.readline()
print(data1)
file.close()


#3-readlines() -read all lines from current cursor position and return in to list
file=open(r'C:\Users\s\OneDrive\Desktop\scr.txt','r')
data3=file.readlines()
print(data3)










