# What is a Database?
# A database is like a digital storage box where you keep data in an organized way.

# Example:
# Student names
# Marks
# Employee details

# Instead of writing in a notebook, we store them in a database.

# What is Database in Python?
# In Python, a database means:

# Using Python to:
# Store data
# Read data
# Update data
# Delete data

# So Python acts like a manager of the database.

# Real-Life Example
# Think like this:

# Database = Bank locker (stores data)
# Python = Bank employee (handles data)

# You don’t touch the locker directly → Python helps you access it.

# What is SQL?
# SQL (Structured Query Language) is used to work with structured data (data in table format).

# Data is stored like Excel sheets:
# id	name	marks
# 1	    John	85
# 2	    Ravi	90

# Features of SQL:
# Data stored in tables (rows & columns)
# Fixed structure (schema)
# Uses SQL language like:
# SELECT * FROM students;

# Examples:
# MySQL
# PostgreSQL
# SQLite

# What is NoSQL?
# NoSQL (Not Only SQL) is used for unstructured or flexible data.
# Data is stored like JSON (dictionary in Python):
# {
#   "name": "John",
#   "marks": 85,
#   "skills": ["Python", "SQL"]
# }

# Features of NoSQL:
# No fixed structure
# Flexible data (you can change format anytime)
# Faster for large and changing data

# Examples:
# MongoDB
# Cassandra


from pymongo import MongoClient
mongoUrl = MongoClient("mongodb+srv://Narendra:Narendra15@cluster0.6gqovw3.mongodb.net/?appName=Cluster0")
myDB = mongoUrl['Python-class']

# 1.One data
myCollection = myDB['user']
print('working')
userdata = {
    "Name" : "Narendra",
    "Age" : 29,
    "E-mail" : "narendrastark15@gmail.com",
    "Mobile" : 8610347810
}
# add data
def createuserdetails(data):
    print(data)
    usercreation = myCollection.insert_one(data)
    print(usercreation)
# createuserdetails(userdata)

# 2.Many data
myCollection = myDB['client data']
print('working')
clientdata = [
    {
    "Name" : "Narendra",
    "Age" : 29,
    "E-mail" : "narendrastark15@gmail.com",
    "Mobile" : 8610347810
    },
    {   
     "Name" : "Tony",
    "Age" : 39,
    "E-mail" : "tony@gmail.com",
    "Mobile" : 9610347811   
    },
    {
    "Name" : "Stark",
    "Age" : 28,
    "E-mail" : "stark@gmail.com",
    "Mobile" : 9299347810
    },
    {
    "Name" : "Thor",
    "Age" : 42,
    "E-mail" : "thor@gmail.com",
    "Mobile" : 9626647810
    }
]
# add data
def createclientdetails(data):
    print(data)
    usercreation = myCollection.insert_many(data)
    print(usercreation)
# createclientdetails(clientdata)