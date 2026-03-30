# Built-In Fucntions:
# In Python, built-in functions are ready-made functions that you can use directly without importing anything. They are generally grouped into types based on what they do.
# 1. Type Conversion Functions
# Convert one data type into another.
# Examples:
# int() → converts to integer
# float() → converts to float
# str() → converts to string
# list(), tuple(), set()
x = "10"
print(int(x))   # 10

# 2. Mathematical Functions
# Used for numeric calculations.
# Examples:
# abs() → absolute value
# round() → round number
# pow() → power
# sum() → total of values
# max(), min()
print(max(10, 20, 5))  # 20

# 3. Input / Output Functions
# Used to take input and display output.
# Examples:
# input() → get user input
# print() → display output
name = input("Enter name: ")
print(name)

# 4. Sequence Functions
# Work with lists, tuples, strings.
# Examples:
# len() → length
# sorted() → sort
# range() → generate numbers
print(len("hello"))  # 5

# 5. Logical / Boolean Functions
# Return True or False.
# Examples:
# all() → True if all elements are True
# any() → True if any element is True
print(all([True, True, False]))  # False

# 6. Object / Type Checking Functions
# Check type or properties of objects.
# Examples:
# type() → check data type
# isinstance() → check type
# id() → memory address
print(type(10))  # <class 'int'>

# 7.Iteration Functions
# Used in loops and iteration.
# Examples:
# enumerate() → index + value
# zip() → combine lists
# map(), filter()
for i, v in enumerate(['a','b']):
    print(i, v)

# 8. Help / Utility Functions
# Used for debugging or info.
# Examples:
# help() → documentation
# dir() → list attributes


