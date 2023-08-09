# Create a class with a property
class MyClass:
  x = 5

# Create an object from the class

i1= MyClass()
print(i1.x)

# Use constructor method to instantiate an object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
class PersonWithString:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)

p2 = PersonWithString("John",45)
print(p2)
p2.myfunc()

