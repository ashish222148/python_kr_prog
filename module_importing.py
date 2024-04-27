#by four types we can import the module

#adding the environment variable(path) where the module exist
import sys
sys.path.append(r'C:\Users\s\OneDrive\Desktop\module')


#1-importing module and calling function variable *class
import testmodule_importing
testmodule_importing.add(10,5)
print(testmodule_importing.name)

#2-importing module through alias
import testmodule_importing as ti
ti.add(5,11)
print(ti.name)

#3-importing only selected not all function and varibale as above two
from testmodule_importing import info,name
info()
print(name)

#4-importing all fuction variable and class but no need to specify module name while calling
from testmodule_importing import *
add(20,56)
info()
print(name)

#how to check where the current module is installed
import os
print(os.path.abspath(os.__file__))
