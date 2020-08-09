
# Classes and Objects

# Objects are an encapsulation of variables and functions into a single entity. 
# Objects get their variables and functions from classes. 
# Classes are essentially a template to create your objects.

class MyClass:
    variable = "one string"

    def function(self):
        print("This is a message inside the class.")

# assign the above class(template) to an object you would do the following:
# myobjectx is an object of the class "MyClass" 

myobjectx = MyClass()

# To access the variable inside of the newly created object "myobjectx":

myobjectx.variable

print(myobjectx.variable)

# -O-J-O- Ejecución
# one string

# You can create multiple different objects that are of the same class(have the same variables and functions defined). 
# However, each object contains independent copies of the variables defined in the class. 

# if we were to define another object with the "MyClass" class

myobjecty = MyClass()

print(myobjecty.variable)

# -O-J-O- Ejecución
# one string

# Now if change the string in the variable

myobjecty.variable = "other string"

print(myobjecty.variable)

# -O-J-O- Ejecución
# other string

print(myobjectx.variable)
print(myobjecty.variable)

# -O-J-O- Ejecución
# one string
# other string

# Accessing Object Functions
# To access a function inside of an object you use notation similar to accessing a variable:

myobjectx.function() # -O-J-O- Ejecución - This is a message inside the class.

###############
#  Excercise  #
###############

# We have a class defined for vehicles. Create two new vehicles called car1 and car2. 
# Set car1 to be a red convertible worth €53901.00 with a name of Fer, 
# and car2 to be a blue van named Jump worth €8983.50.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 53901.00

car2 = Vehicle()
car2.color = "blue"
car2.kind = "van"
car2.name = "Jump"
car2.value = 8983.50


# test code
print(car1.description())
print(car2.description())

# -O-J-O- Ejecución
# Fer is a red convertible worth $53901.00.
# Jump is a blue van worth $8983.50.

