# Built-in module
import platform

x = platform.system()
print(x)


# There is a built-in function to list all the function names 
# (or variable names) in a module. The dir() function:

allFunctionAndVariables = dir(platform)
print(allFunctionAndVariables)

# You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1

print (person1["age"])