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