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
from bson import ObjectId
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

# get all clients - all details
def getAllclientdata():
    data = myCollection.find()
    for i in data:
        print(i)
# getAllcliendata()

# get specific client data - one detail
def SpecificData(id):
    print(id)
    data = myCollection.find_one({"_id":ObjectId(id)})
    print(data)
# SpecificData("69e0a20ed7bdaac3b8b35594")

# get clients - limit details
def getLimitclientdata():
    data = myCollection.find().limit(2)
    for i in data:
        print(i)
# getLimitclientdata()

# sorting
def getclientDataSorting():
    data = myCollection.find().sort("name",-1)
    for i in data:
        print(i)
# getclientDataSorting()

# Query
def usingQuery():
    query = {"Age":{"$gt":30}}
    data = myCollection.find(query)
    for i in data:
        print(i)
# usingQuery()

# update
def updateUserById(id, newData):
    print("Updating user:", id)
    result = myCollection.update_one(
        {"_id": ObjectId(id)},   # find using _id
        {"$set": newData}        # update data
    )
    print("Matched:", result.matched_count)
    print("Modified:", result.modified_count)
# updateUserById(
#     "69e0a20ed7bdaac3b8b35596",
#     {"Name":"Harish", "Age": 26, "Mobile": 9345452842}
# )  

def deleteUserById(id):
    print("Deleting user:", id)
    result = myCollection.delete_one(
        {"_id": ObjectId(id)}   # find using _id
    )
    print("Deleted:", result.deleted_count)
# deleteUserById("69e0a20ed7bdaac3b8b35596")