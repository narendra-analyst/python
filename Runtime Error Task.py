# Task
# 1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    a = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# 2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
  value = int('abc')
except ValueError:
  print('invalid integer')

# 3.

def get_integer_input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("Error: Invalid input, input a valid integer.")
n = get_integer_input("Input an integer: ")
print("Input value:", n)