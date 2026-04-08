# What is Exception Handling?
# Exception = Error during program execution
print(10 / 0)
# This gives error → ZeroDivisionError. This kind of error is called an exception

# Why do we use Exception Handling?
# Without exception handling:
# Program stops suddenly

# With exception handling:
# Program continues safely
# syntax
# try:
    # risky code
# except:
    # what to do if error occurs

# Simple Example
try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Error occurred!")

# If user enters 0 or text → it won’t crash,It will print: Error occurred!

# How it works (Very Important)
# 1.Python tries to run try block
# 2.If error happens → jumps to except
# 3.If no error → except is skipped

# Important Keywords Summary
# Keyword	   Meaning
# try	       risky code
# except	   handle error
# else	     runs if no error
# finally	   always runs

