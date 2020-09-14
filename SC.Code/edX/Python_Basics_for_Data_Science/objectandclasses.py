#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT

Created on Sun Sep 13 14:49:33 2020

@author: scelis - ¯\_(ツ)_/¯

Types:
    
    int: 1, 2, 3,...
    float: 1.0, 2.0, 3.0,...
    String: "uno", "dos", "tres"
    tuple: ("uno", 2, 3.0)
    list: ["uno", 2, 3.0]
    set: {"uno", "dos", "tres"}
    dictionary: {"key1": "uno", "key2": 2, "key3": 3.0, }
    bool: True, False
    The are object, each object has:
        type
        internal representation
        methods
    An object is an instance of a particular type

objectandclasses.py    

"""
import matplotlib.pyplot as plt

# Find the type of a object by using the command:
type() 

# methods are functions that every instance of that class or type provides, 
# it's how you interact with the data in a object
# Sorting is an example of a method that interacts with the data in the object

Rating=[10, 9, 6, 5, 10, 8, 9, -1, 6, -8]

# utilizando el método sort
Rating.sort() # [-8, -1, 5, 6, 6, 8, 9, 9, 10, 10]

# utilizando el método reverse
Rating.reverse() # [10, 10, 9, 9, 8, 6, 6, 5, -1, -8]

# Own Types
# Defining Classes

# Classes has Data Attributes and Methods

# Data Attributes, define the Class

# Methods, interect with the object

# =============================================================================
# Class Circle
# 
# Que constituye un circulo?
# Attributes:
# radius,
# color,
# 
# class Circle(object):
    
    # class => Definition:
    # Circle => Name
    # (object) => Parent
    
    # Object 1: instace of type Circle
    # Data Atributes:
    #     radius=4
    #     color=red

    # Object 2: instace of type Circle
    # Data Atributes:
    #     radius=2
    #     color=green
        
        
# =============================================================================

# define a class
# class Circle (object): # define class

#     def __init__(self, color, radius): 

#         self.radius = radius;
#         self.color = color;
        
        # class => define class
        # __init__ => Constructor used to Initialize data attributes each instance of the class, create a new instance of class
        # radius, color => Initialize the parameters data attributes on the class instance
        # self => parameter refers the newly created instance of the class
        # radius and color parameters can be used in the constructor's body to access the values passed to the class constructor when the class is constructed'
        # can set the value of the radius and color data attributes to the values passed to the constructor method.
        

# create an object of class Circle

    # RedCircle = Circle(10,'red')
        # RedCircle is the Name of Object
        # Circle(10, "red") is the object Constructor 
        # Circle Name of Class
        # (10, "red") Attributes 
        

class Circle (object): # define class

# Constructor
    def __init__(self, color, radius): 

        self.radius = radius;
        self.color = color;
        
# Method used to add r to radius
    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)
    
# Method used to draw the circle       
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

# when create an instance of a Class Circle:
        
c1 = Circle('red', 10)

c1.radius # 10
c1.color # 'red'
        
        
    
# class Circle(object):
#     def __init__(self, 10,  'red'):
#         self.radius = 10;
#         self.color = 'red';
# 

# Access attributes of instance c1:
#   c1.radius # 10
#   c1.color # 'red'

  
# using the methods add_radius() and drawCircle():        


print('Radius of object:',c1.radius)
c1.drawCircle()   
c1.add_radius(8)
print('Radius of object of after applying the method add_radius(8):',c1.radius)
c1.drawCircle()   
c1.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',c1.radius)
c1.drawCircle()   

    # def add_radius(self, 8):
    #    self --> self.radius = 10;
    #             self.color = 'red';
    #     self.radius =  10 + 8
    #     return (18)
    # por tanto    
    #   c1.radius # 18
    #   c1.color # 'red'   


# We can change the object's data attributes: 
c1.radius = 1
print('Radius of object:',c1.radius)
c1.drawCircle()   


# Create a blue circle with a given radius

BlueCircle = Circle(color='blue', radius=100)
print('Radius of object:',BlueCircle.radius)
BlueCircle.drawCircle()  

  
# Another way to define a class add default values for parameters

class Circle2 (object): # define class

    def __init__(self, color='red', radius=3): 

        self.radius = radius;
        self.color = color;
        
# Method used to add r to radius
    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)
    
    # def drawCircle(self):

        # Find out the methods can be used on the object
dir(c1) # obtain the list of data attributes and methods associated whith a class

# __xxxx__ => internal use
        
# 
# =============================================================================
# Class Rectangle
# 
# Que constituye un rectangulo?
# Attributes:
# width,
# height,
# color,
# 
# class Rectangle(object):
    
    # class => Definition:
    # Circle => Name
    # (object) => Parent
    
    # Object 1: instace of type Rectangle
    # Data Atributes:
    # width=2
    # height=2
    # color=blue

    # Object 2: instace of type Rectangle
    # Data Atributes:
    # width=3
    # height=1
    # color=yellow

# =============================================================================



class Rectangle (object): # define class
    
    # Constructor
    # can set the value of the width, height and color data attributes to the values passed to the constructor method.
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
        # __init__ => Constructor used to Initialize data attributes each instance of the class, create a new instance of class
        # width, height, color => Initialize the parameters data attributes on the class instance
        # width, height and color parameters can be used in the constructor's body to access the values passed to the class constructor when the class is constructed'
        # self => parameter refers the newly created instance of the class
        
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()    
    
YellowRectangle = Rectangle(10, 5,'yelow')

YellowRectangle.width # 10
YellowRectangle.height # 5
YellowRectangle.color # 'yelow'

dir(YellowRectangle)

SkinnyBlueRectangle = Rectangle(2, 10, 'blue')

SkinnyBlueRectangle.drawRectangle()


class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1
        
# make="Hiunday"
# model="i30"
# color="red"
my_car = Car("Hiunday", "i30", "red")  
my_car.car_info()
# make:  Hiunday
# model: i30
# color: red
# number of owners: 0

my_car.sell()

my_car.car_info()
# make:  Hiunday
# model: i30
# color: red
# number of owners: 1


for i in range(5):
  my_car.sell()
print("my_car.car_info()", my_car.car_info())     

# make:  Hiunday
# model: i30
# color: red
# number of owners: 6
# my_car.car_info() None

