# Decorators:
# A decorators function in python is a way to modify or extended the behavior of another function without changing its actual code. It's commonly used for things like logging, authentication, timing, coching, etc.
# A decorator warps a function inside another function
# @symbol is used to denote a decorator function
# Basic Syntax:
def decorator_function(original_function):
    def wrapper():
        print("before hello")
        original_function()
        print("after hello")
    return wrapper
@decorator_function
def say_hello():
    print('hello')
say_hello()

# Eg with Arguments:
def decorator(func):
    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")
    return wrapper
@decorator
def greet(name):
    print(f"Hello {name}")
greet("Tony")

# Why Use Decorators?
# Decorators are used to:
# Add logging
# Check permissions
# Measure execution time
# Handle errors
# Authentication (very common in web apps)

# Real Use Case (Important)
def login_required(func):
    def wrapper():
        print("Checking login...")
        func()
    return wrapper
@login_required
def dashboard():
    print("Welcome to dashboard")
dashboard()

# Key Points to Remember
# Decorator = function that wraps another function
# Uses @decorator_name syntax
# Helps reuse code
# Keeps original function clean
