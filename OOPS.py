# What is OOPS in python?
# OOPS in python (object oriented programming system) is a way of writing code by using objects and classes, just like real-world things.

# Why do we use OOPS?
# OOPS is used because it makes your code:
# 1.Easy to Understand - Looks like real-life objects, Easy for beginners to follow.
# 2.Reusable - Write once, use many times, Example: one class → many objects
# 3.Organized -  Code is clean and structured, No messy long programs
# 4.Easy to Maintain - If error comes → easy to fix,Changes won’t affect entire program, Code is divided into small parts(classes)
# 5.Scalable (for big projects)- Used in real companies for large applications
# 6.Real-World Modeling - Representing real-life objects and their behavior in code using classes and objects.
# 7.Security (encapsulation) - You can hide important data and control access
# 8.Fexibility(polymorphism) - One function or method can behave in different ways depending on the object using it.

# Difference between Classes and Objects
# Classes :         
# Class is blueprint or templates for creating objects.
# We create only one class.
# Memory is not allowcated when we create an class.

# Objects:
# Ojects is a real world things.
# We can create multiple objects for one class.
# Memory allowcated when we create an object.

# Class:
# __init__() is a constructor method that runs automatically when a new object is created. It is used to initialize object data.
# Self refers to the current object, allowing each objects to store and access its own data.
#Eg:
# Class is like a design(blueprint)
# syntax
class car:
    pass
# Object (real thing)
c1 = car()
# m1 is real mobile object

# with data + data
class Car:
    def __init__(self, color):
        self.color = color
    def start(self):
        print("Car started")
my_car = Car("Red")
print(my_car.color)
my_car.start()

# Eg 2:
class Dog:
    species = "Canine"  # Class attribute
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.species)

# The four pillars of OOPS:
# Inheritance
# Encapsulation
# Polymorphism
# Abstraction

# Inheritance:
# The mechanism by which one class (called the child or derived class) can access the attributes and methods of another class (called the Parent or Base class)
# Types of classes:
# Parent class (Base class) → gives properties
# Child class (Derived class) → receives properties
# Eg:
class Parent:
    def show(self):
        print("This is parent class")
class Child(Parent):   # Inheriting Parent
    def display(self):
        print("This is child class")
obj = Child()
obj.show()      # from parent
obj.display()   # from child

# Why we use Inheritance?
# Code reuse - Avoid duplicating code in multiple classes
# Organized structure - Logical grouping of related classes.
# Extensibility - Easy to add new features extending existing classes.
# Eg:
class Animal:
    def sound(self):
        print("Animals make sound")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.sound()   # from Animal
d.bark()    # from Dog

# Types of Inheritance - There are five types of inheritance,
# 1.Single Inheritance:
# One parent → One child
class Parent:
    def show(self):
        print("Parent class")
class Child(Parent):
    def display(self):
        print("Child class")
obj = Child()
obj.show()
# Meaning: Child gets from only one parent

# 2.Multiple Inheritance
# One child → Multiple parents
class Father:
    def skill1(self):
        print("Driving")
class Mother:
    def skill2(self):
        print("Cooking")
class Child(Father, Mother):
    pass
obj = Child()
obj.skill1()
obj.skill2()
# Meaning: Child gets from more than one parent

# 3. Multilevel Inheritance
# Grandparent → Parent → Child
class Grandparent:
    def home(self):
        print("Grandparent house")
class Parent(Grandparent):
    def car(self):
        print("Parent car")
class Child(Parent):
    def bike(self):
        print("Child bike")
obj = Child()
obj.home()
obj.car()
# Meaning: Inheritance happens in levels

# 4. Hierarchical Inheritance
# One parent → Multiple children
class Parent:
    def property(self):
        print("Parent property")
class Child1(Parent):
    pass
class Child2(Parent):
    pass
obj1 = Child1()
obj2 = Child2()
obj1.property()
obj2.property()
# Meaning: Many children share same parent

# 5. Hybrid Inheritance
# Combination of different types
class A:
    def show(self):
        print("Class A")
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
obj = D()
obj.show()
# Meaning: Mix of multiple + multilevel etc.

# Easy way to remember:
# Single → 1 parent
# Multiple → many parents
# Multilevel → chain (grandparent → parent → child)
# Hierarchical → one parent, many children
# Hybrid → combination

# Task:
# 1.Create a Student class that inherits from Person and calls both methods.
class Person:
    def name(self):
        print('Person name is Tony')
class Student(Person):
    def study(self):
        print('Student is studying')
childObj = Student()
childObj.name()    
childObj.study()   

# 2.Create a Car class that inherits from Vehicle and uses both start() and drive() methods.
class vehicle:
    def start(self):
        print('car started')
class car(vehicle):
    def drive(self):
        print('drive to airpot')
childObj = car()
childObj.start()
childObj.drive()

# 3.Create a Puppy class using multilevel inheritance and call all inherited methods.
class Animal:
    def eat(self):
        print('Animal eats')
class Dog(Animal):
    def bark(self):
        print('Dog barks')
class Puppy(Dog):
    def cute(self):
        print('Puppy is cute')
obj = Puppy()
obj.eat()    
obj.bark()  
obj.cute()   

# 4.Create a Child class using multiple inheritance from Father and Mother.
class Father:
    def occupation(self):
        print('My dad is a businessman')
class Mother:
    def work(self):
        print('My mom is a housewife')
class Child(Father, Mother):
    pass
obj = Child()
obj.occupation()
obj.work()

# 5.Override the work() method in Manager class inherited from Employee.
class Employee:
    def work(self):
        print("Working")
class Manager(Employee):
    def work(self):   # overriding
        print("Managing")
obj = Manager()
obj.work()

# Polymorphism:
# Polymorphism is the ability of the same method or function to perform different actions based on the object.
# Real-life Example
# Think of a person:
# A person can be a teacher in school
# The same person can be a father at home
# Same person, different roles → many forms

# Example 1: Same method, different classes
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
d = Dog()
c = Cat()
d.sound()   # Dog barks
c.sound()   # Cat meows
# Here, both classes have the same method sound(),but output is different → Polymorphism

# Example 2: Using same function for different objects
def make_sound(animal):
    animal.sound()
make_sound(Dog())  # Dog barks
make_sound(Cat())  # Cat meows
# Same function, different behavior depending on object

# Types of Polymorphism in Python
# 1.Method Overriding or Runtime Polymorphism (Important) - Child class changes the parent class method
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
obj = Dog()
obj.sound()

# 2.Operator Overloading or Compile Polymorphism - Same operator behaves differently
print(5 + 3)        # 8
print("Hello " + "World")  # Hello World

# Important (Python point)
# Python does NOT truly support compile-time polymorphism like C++/Java (no method overloading in same way).
# But we still consider:
# Operator overloading = compile-time polymorphism (conceptually)

# Easy Difference Table
# Feature	          Compile-time	        Runtime
# When decided	      Before execution	    During execution
# Speed	              Faster	            Slightly slower
# Example	          + operator	        Method overriding
# Python support	  Limited	            Fully supported

# What is Operator Overloading?
# Operator Overloading means giving a different meaning to the same operator depending on the data.
# Simple Meaning:
# The same operator (+, -, *, etc.) can do different tasks based on what you use it with.
# Example 1 (Basic)
print(5 + 3)          # 8  → addition
print("Hello " + "AI")  # Hello AI → string joining
# Same + operator:
# Adds numbers
# Joins strings
# This is operator overloading

# Example 2 (In OOP - Custom Overloading)
# We can define our own behavior using special methods
class Student:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, other):
        return self.marks + other.marks
s1 = Student(50)
s2 = Student(60)
print(s1 + s2)   # 110
# Here:
# +is overloaded using __add__()
# Instead of normal addition, it adds student marks
# Common Operator Methods
# Operator	Method
# +	        __add__()
# -	        __sub__()
# *	        __mul__()
# /	        __truediv__()