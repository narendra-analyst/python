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

# Task:
# 1.Create a decorator that prints Start" before the function "End" after the function.
def decorator(func):
    def wrapper():
        print('before start')
        func()
        print('after start')
    return wrapper
@decorator
def func():
    print("engine starts")
func()

# 2.Create a decorator that prints "Calling function..." apply it to a function say_hi() that prints "Hi".
def decorator(calling_function):
    def wrapper():
        print("before hello")
        calling_function()
        print("after hello")
    return wrapper
@decorator
def say_hello():
    print('hi')
say_hello()

# 3.Create a decorator that works with a function that takes a name
def decorator(func):
    def wrapper(name):
        print('before calling')
        func(name)
        print('after calling')
    return wrapper
@decorator
def greet(name):
    print(f"hello {name}")
greet("narendra")

# 4.Create a decorator that prints "User logged in" Apply it to a function profile() that prints "This is your profile".
def login_required(func):
    def wrapper():
        print('before login')
        func()
        print('after login')
    return wrapper
@login_required
def user():
    print('this is your profile')
user()

# 5.Create a decorator that counts how many times a function is called
def count_calls(func):
    count = 0 
    def wrapper():
        nonlocal count
        count += 1
        print(f"Called {count} times")
        func()
    return wrapper
@count_calls
def say_hello():
    print("Hello")
say_hello()
say_hello()
say_hello()

# 6.Create a decorator that prints 'function is running' apply it to a function that prints "Task completed".
def decorator(func):
    def wrapper():
        print('function is running')
        func()
    return wrapper
@decorator
def func():
    print('task completed')
func()

# 7.Create a decorator that Doubles the return value of a function.
def double_result(value):
    def wrapper():
        result = value()   # call original function
        return result * 2  # double the result
    return wrapper
@double_result
def get_number():
    return 5
print(get_number())

# 8.Create a decorator that prints "Checking number..." apply it to a function that takes a number and prints whether it is even or odd.
def decorator(func):
    def wrapper(n):
        print('checking number')
        func(n)
    return wrapper
@decorator
def check_even_odd(n):
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
check_even_odd(6)

# 9.Create a decorator that prints "Access Denied" does NOT call the original function apply it to a function that prints "Secret Data".
def decorator(func):   
    def wrapper():
        print("Access Denied")
        # do not call func()
    return wrapper
@decorator
def secret(): #original function
    print("Secret Data")
secret()

# 10.Create a decorator that prints "Welcome!" before function.
def decorator(func):
    def wrapper():
        print('welcome!')
        func()
    return wrapper
@decorator
def greet():
    print("User page")
greet()