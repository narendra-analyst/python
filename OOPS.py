# # What is OOPS in python?
# # OOPS in python (object oriented programming system) is a way of writing code by using objects and classes, just like real-world things.

# # Why do we use OOPS?
# # OOPS is used because it makes your code:
# # 1.Easy to Understand - Looks like real-life objects, Easy for beginners to follow.
# # 2.Reusable - Write once, use many times, Example: one class → many objects
# # 3.Organized -  Code is clean and structured, No messy long programs
# # 4.Easy to Maintain - If error comes → easy to fix,Changes won’t affect entire program, Code is divided into small parts(classes)
# # 5.Scalable (for big projects)- Used in real companies for large applications
# # 6.Real-World Modeling - Representing real-life objects and their behavior in code using classes and objects.
# # 7.Security (encapsulation) - You can hide important data and control access
# # 8.Fexibility(polymorphism) - One function or method can behave in different ways depending on the object using it.

# # Difference between Classes and Objects
# # Classes :         
# # Class is blueprint or templates for creating objects.
# # We create only one class.
# # Memory is not allowcated when we create an class.

# # Objects:
# # Ojects is a real world things.
# # We can create multiple objects for one class.
# # Memory allowcated when we create an object.

# # Class:
# # __init__() is a constructor method that runs automatically when a new object is created. It is used to initialize object data.
# # Self refers to the current object, allowing each objects to store and access its own data.
# #Eg:
# # Class is like a design(blueprint)
# # syntax
# class car:
#     pass
# # Object (real thing)
# c1 = car()
# # m1 is real mobile object

# # with data + data
# class Car:
#     def __init__(self, color):
#         self.color = color
#     def start(self):
#         print("Car started")
# my_car = Car("Red")
# print(my_car.color)
# my_car.start()

# # Eg 2:
# class Dog:
#     species = "Canine"  # Class attribute
#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute
# # Creating an object of the Dog class
# dog1 = Dog("Buddy", 3)
# print(dog1.name) 
# print(dog1.species)

# The four pillars of OOPS:
# Inheritance
# Encapsulation
# Polymorphism
# Abstraction

