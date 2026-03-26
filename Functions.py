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
#1.Write a program to check even or odd using function.
num = 16
def even():
      if num % 2 == 0:
        return 'even'
      else:
        return 'odd'
result=even()
print(f'the number 16 is {result}')

# 2.write a program to check the number 6 is divisible by 2 and 3.
n=6
def divisible():
      if n %2 %3 == 0 :
       return'6 is divisible by 2 and 3'
      else:
       return'6 is not divisible by 2 and 3'
result=divisible()
print(f'the number {result}')