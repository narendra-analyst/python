# File Handling:
# File handling in Python means working with files—like creating, reading, writing, and updating files stored on your computer.
# In simple terms, it allows your program to store data permanently instead of losing it when the program ends.
# 1.Why file handling is used
# Save data (like user input, logs, results)
# Read data from files (like text files, CSV, etc.)
# Modify or update existing files.

# 2.Basic operations in file handling
# Open a file
# Read or write data
# Close the file
file = open("example.txt", "r")
# Modes:
# "r" → read
# "w" → write (overwrites file)
# "a" → append (adds to file)
# "x" → create new file

# Reading a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Writing to a file
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()

# Best practice (using with)
# Python provides a cleaner way that automatically closes the file:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Closing File:
# close() in Python is a method used to close a file after you finish working with it.
# Why close() is important
# Frees system resources (memory)
# Saves changes properly (especially in write mode)
# Prevents file corruption
# Avoids errors when reopening the file

# Eg:
file = open("data.txt", "w")
file.write("Hello")
file.close()

# Here:
# File is opened
# Data is written
# close() safely closes the file

#1. What happens if you don’t use close()?
# Data may not be saved properly 
# File may remain locked 
# Memory gets wasted 

# 2.Better way (recommended)
# Use with statement instead of close():
with open("data.txt", "w") as file:
    file.write("Hello")
# Here Python automatically closes the file for you

# In Python, rename() is a function used to change the name of a file or folder.
# Where it comes from?
# rename() is part of the os module.
# import os
# os.rename(old_name, new_name)
# old_name → current file name
# new_name → new file name you want
import os
os.rename("data.txt", "new.txt")
# What happens?
# If data.txt exists
# It will be renamed to new.txt