# Fucntions:
# A function is a block of code that performs a specific task.
# syntax:
# def myFun():
      # //code
# myFun()

# Argument vs Parameters:
#  A parameter is a variable in a function definition that act as a placeholder for data it expects to receive, while an argument is the actual value passed to the function when it is called.
# eg: 
def add():
        a=10
        b=20     #parameter(placeholder)
        c=a+b
        print(c)
add()    #argument(original value)

# Scope:
# Scope refers to accessbility and visibility of the variable.
# Types of scope:
# 1.Local Scope
# Variable defined inside a fucntion and accessbility only with the function. 
def localscope():
        x=100
        print(x)
localscope()

# 2.Enclosing Scope
# Applies to nested functions (fucntion inside function) and inner fucntions can access variable from the outer(enclosing) function.
def outer():
        x=20
        def inner():
                print(x)
        inner()
outer()

# 3.Golbal Scope
# Variable defined at the top level of a script or module and accessible throughout the file.
n1=100
def data():
        print(n1)
data()
# To modify a global variable inside a funtion use "Global"-keyword.
n1=200
def data():
        global n1
        n1=300
        print('inside the fn:',n1)
data()
print('outside the fn:',n1)

# Types of functions:
# 1.Built-in functions
# Predefined functions available in python and no need to define them.
# eg: print('hello')
#     len(1,2,3)
#     type(10)

# 2.User-defined functions:
# Functions created using def.
def great():
  print('tony')
great()

# Arbitary Positional Argument (*):
# Used when you don't know how many positional arguments will be passed and collected into a tuple. Use(*) before the parameters.
# We pass only the value
def myData(*a):
       print(a)
myData(10,20,30,40)

def myData(c,*a):
       print(c)
       print(a)
myData(10,20,30,40)

# Arbitary Keyword Argument (**):
# It allows a function to accept any number of keyword arguments and store them in a dictionary.
# It lets a function accept a variable number of named(key=value) arguments.
# We pass key = value
def myData(**a):
       print(a)
myData(x=10,y=20)

def myData(c,**a):
       print(c)
       print(a)
myData(10,name="Narendra", age=28)

# Lambda Function:
# A lambda function is a small fucntion is otherwise known as anonymous fucntion(unamed) is defined in a single line using the lambda keyword.
# syntax: lambda argument:expression
add = lambda a,b,c : a+b+c
print(add(10,20,30))
# Can have any number of arguments, must have only one expression automatically returns the result(no return keyword).

# Return Keyword:
# In python the return keyword is used inside a function to send result back to the caller and exit the function.
def add(a,b):
       return a+b
result=add(3,4)
print(result)

# Recursive Function:
# The process in which a function calls itself directly or indirectly is called recursive function.
def factorial(n):
       if n==0 or n==1:
        return 1
       else:
        return n*factorial(n-1)
result=factorial(5)
print(f'the factorial of 5 is {result}')

# Function Task:
#1.write a program to check even or odd using function.
num = 16
def even():
      if num % 2 == 0:
        return 'even'
      else:
        return 'odd'
result=even()
print(f'the number 16 is {result}')

# 2.write a program to check the number 6 is divisible by 2 and 3 using function.
n=6
def divisible():
      if n %2 %3 == 0 :
       return'6 is divisible by 2 and 3'
      else:
       return'6 is not divisible by 2 and 3'
result=divisible()
print(f'the number {result}')

# 3.write a program to find greater of two numbers a = 20 and b = 30 using function.
def greater(a,b):
     if a > b :
      return 'greater number is a'
     else:
      return 'greater number is b'
result=greater(20,30)
print(f'the {result}')

# 4.write a program to check vowel or consonant using function.
def check_char(ch):
     if ch in ('a','e','i','o','u'):
       return 'is vowel'
     else:
        return 'is consonant'
result= check_char('a')
print(f'the character {result}')

# 5.write a program using a function to check whether a given number is positive, negative, or zero.
def check_num(number):
     if number > 0 :
          return 'is positive'
     elif number < 0 :
          return 'is negative'
     else:
          return 'is zero'
result=check_num(6)
print(f'the number {result}')

# 6.Write a program using a function to print numbers from 1 to 10 and also use for loop.
def num():
        for i in range(1,11):
             print(i)
num()

# 7.Write a function to print all even numbers from 1 to 20 using a for loop.
def check_num():
     for even in range(1,20):
          if even % 2 == 0 :
               print(even)
check_num()

# 8.Write a function to find the sum of numbers from 1 to n (n is given as input).
def check_num(n):
     total = 0
     for i in range (1,n+1):
          total = total + i
     return total
result = check_num(10)
print(result)

# 9.Write a function to print the multiplication table of a given number.
def check_num(n):
    for i in range(1, 11):
        print(i * n)
check_num(3)

# 10.Write a function to count how many vowels are present in a given string using a for loop.
def check_char(text):
     count = 0
     for ch in text:
        if ch in ('a', 'e', 'i', 'o', 'u'):
                count = count + 1
     return count
result=check_char('narendra')
print(f'Total no. of vowel is {result}')

# 11.Write a function to count how many consonants are in a string.
def check_char(text):
    count = 0
    for ch in text:
        if ch not in ('a', 'e', 'i', 'o', 'u'):
            count = count + 1
    return count
result = check_char('narendra')
print(f'Total no. of consonants is {result}')

# 12.Write a function to reverse a given string using a for loop.
def reverse_string(text):
     rev = ""
     for ch in text:
          rev = ch + rev
     return rev
result = reverse_string('tony stark')
print(result)
          
# 13.Write a function to count how many digits are present in a string.
def check_string(text):
     count = 0
     for ch in text:
          if ch.isdigit():
               count = count + 1
     return count
result = check_string('narendra1997')
print(f'the no. of digits is {result}')

# 14.Write a function to find the largest number in a list.
def check_largest(num):
     largest = num[0]
     for i in num :
          if i > largest :
               largest = i
     return largest
result = check_largest([10,30,50,20,60,40])
print(f'the largest no. is {result}')

# 15.Write a function to count how many even numbers are in a list.
def check_even(num):
     count = 0
     for i in num :
          if i % 2 == 0 :
               count = count + 1
     return count
result=check_even([2,3,12,5,16,14,18,15,9,10])
print(f'There are {result} even numbers in a list')

# 16.Write a function to find the sum of all elements in a list.
def sum(num):
     total = 0
     for i in num:
          total = total + i
     return total
result = sum([15,9,6,22,25,30])
print(f'Total : {result}')

# 17.Write a function to print each character of a string using a for loop.
def check_char(text):
     for ch in text:
         print(ch)
result=check_char('hello world')

# 18.Write a function to count how many spaces are in a string.
def check_space(text):
     count = 0
     for ch in text:
          if ch in " ":
               count += 1
     return count
result=check_space('hello world')
print(f'space : {result}')

# 19.Write a function to check whether a string is a palindrome.
def check_palindrome(text):
     rev = ""
     for ch in text:
          rev = ch + rev
          if text == rev:
               return rev
result=check_palindrome('madam')
print(f'{result} is a palindrome')

# 20.Write a function to find the factorial of a number using a for loop.
def chek_factorial(n):
     if n==0 or n==1:
          return 1
     else:
          return n*factorial(n-1)
result=chek_factorial(6)
print(f'the factorial of 6 is {result}')
