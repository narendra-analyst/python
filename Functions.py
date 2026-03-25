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

# Arbitary Argument:
# Used when you don't know how many positional arguments will be passed and collected into a tuple. Use(*) before the parameters.
def myData(*a):
       print(a)
myData(10,20,30,40)

def myData(c,*a):
       print(c)
       print(a)
myData(10,20,30,40)
