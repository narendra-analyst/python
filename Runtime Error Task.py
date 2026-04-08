# Task
# 1.Basic try and except block.
try:
    print(undefined_variable)
except NameError:
    print("This variable is not defined.")

# 2.Handling multiple exceptions.
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError) as e:
    print("Error occurred:", str(e))

# 3.Using the else clause in exception handling.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Result is", result)

# 4.Using the finally clause in exception handling.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
finally:
    print("This block of code will always execute.")

# 5.Raising exceptions using raise.
try:
    raise ValueError("This is a custom error message.")
except ValueError as e:
    print("An error occurred:", str(e))

# 6.Creating custom exceptions.
class CustomError(Exception):
    pass
try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print("An error occurred:", str(e))



# Try and Except Task:-
# 1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def zero_division():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("You cannot divide by zero!")
num = zero_division()
print("Result:", num)

# 2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def integer_input(number):
    try:
        value = int(input(number))
        return value
    except ValueError:
        print('invalid integer')
num = integer_input("integer:")
print("input value:",num)

# 3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('Error: file not found')
file_name = input('File name: ')
open_file(file_name)

# 4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Sum:", num1 + num2)
    except ValueError:
        raise TypeError("Inputs must be numerical")
get_numbers()

# 5.Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
def open_file(filename):
    try:
        with open(filename,'r') as file:
            content = file.read()
            print(content)
    except PermissionError:
        print('Error: no access for this file')    
file_name = input('File name:')
open_file(file_name)

# 6.Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
def my_list():
    numbers = [1, 2, 3]
    try:
        index = int(input("Enter index: "))
        print("Element:", numbers[index])
    except IndexError:
        print("Error: Invalid Index Access")
my_list()

# 7.Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    n = int(input("Input a number: "))
    print("You entered:", n)
except KeyboardInterrupt:
    print("Input canceled by the user.")

# 8.Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def division(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ArithmeticError:
        print("Error: Arithmetic error occurred!")
numerator = int(input("Input the numerator: "))
denominator = int(input("Input the denominator: "))
result = division(numerator, denominator) 
print('result:',result)

# 9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except UnicodeDecodeError:
        print("Error: Cannot decode file")
    except FileNotFoundError:
        print("Error: File not found")
file_name = input("Enter file name: ")
read_file(file_name)

# 10.Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
def list_operation():
    try:
        numbers = [1, 2, 3, 4]
        numbers.push(5)   
    except AttributeError:
        print("Error: This attribute/method does not exist for the list.")
list_operation()

