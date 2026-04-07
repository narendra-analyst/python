# Exceptional Handling:
# Is the process of responding to the occurrance of exceptions, Exceptions are unwanted conditions that disturbs the program execution it occurred.

# Types of Error:
# There are three types of errors,
# Syntax Error
# Runtime Error
# Logical Error

# What is syntax Error?
# Syntax error (or passing error) occur when the code violated the formal rules of the python language. These are caught by the interpreter before the program starts running.
# Indentation Error
# Tab Error
# General Syntax Error like (:)
# Eg:
if 5 > 2
    print("Hello")

# Error because : is missing

# What is Runtime Error?
# A runtime error happens while the program is running
# Your code is written correctly (no syntax error)
# But something goes wrong during execution
# Eg:
a = 10
b = 0
print(a / b)

# Error → ZeroDivisionError
# Code is correct, but while running → error happens

# Types of Runtime Errors in Python
# 1.ZeroDivisionError
# When you divide a number by zero
print(5 / 0)

# 2.TypeError
# When you use wrong data types together
print("Age: " + 25)
# You can't add string + integer

# 3.ValueError
# When the value is correct type but wrong format
num = int("abc")
# "abc" cannot be converted to integer

# 4.IndexError
# When accessing invalid index in list
my_list = [1, 2, 3]
print(my_list[5])
# Index 5 doesn't exist

# 5.KeyError
# When accessing a dictionary with wrong key
data = {"name": "Tony"}
print(data["age"])
# "age" key not found

# 6.FileNotFoundError
# When file does not exist
open("data.txt", "r")
# File not found

# 7.NameError
# When variable is not defined
print(x)
# x is not declared

# 8.AttributeError
# When object has no such attribute
x = 10
x.append(5)
# int has no append()

# 9.ImportError / ModuleNotFoundError
# When module is not found
import abcxyz
# Module doesn't exist

# What is Logical Error?
# A logical error means:
# Your program runs
# No error message
# But output is wrong
# Eg:
num = 4
if num % 2 == 1:
    print("Even")
else:
    print("Odd")

# Output = Wrong
# Condition is incorrect → logic mistake

# Difference b/w Error and Exceptions
# Error - Issues in the program logic such as syntax error, etc. It occurs at compile time.
# Exceptions - Problems that occurs at runtime and can be mananged using exceptions handling (eg.,invalid input,mixing files)