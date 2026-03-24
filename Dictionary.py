# A dictionary in Python is a built-in, mutable, and ordered collection data structure used to store data in key-value pairs. 
# Format : {key : word} , {name : narendra}
student = {'Name': 'Narendra', 'Age': 28, 'City': 'Pondy'}
# print(student)

# To access specific value
print(student['Name'])
print(student.get('Name'))

# To check key and value
# print(student['Phone'])  # Through error if we access unknown value
print(student.get('Phone'))  # does not show any error, shows None

# To add or update value
student['Age'] = 29 # to change the value in dictionary
student.update({'course': 'Data Analyst'}) # to update the key and value in dictionary
print(student)

# Pop method
print(student.pop('Age'))  # remove the value inside the pop
print(student.popitem())   # removes the last added value

# Delete Method
del student['Age']
print(student)

# Clear Method
student.clear()
print(student)

# To print full dictionary
print(student.items())

# For Loop
for key,value in student.items() : # print both key and values.
    print(key, value)

for i in student : # print only key.
    print(i)

# Nested Dictionary :
# Nested Dictionary
details = {
    'student1': {'Name': 'Narendra', 'Age': 28, 'City': 'Pondy'},
    'student2': {'Name': 'Vijay', 'Age': 50, 'City': 'Chennai'}
}
print(details)

# 1.Count Frequency of Elements Given a list, create a dictionary that stores the frequency of each element.
numbers = [1,2,2,3,3,3,4]
freq = {}
for i in numbers:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1
print(freq)

# 2.Find Key with Maximum Value Write a program to find the key with the highest value in a dictionary {"a":10, "b":25, "c":15}.
d = {"a":10, "b":25, "c":15}
max_key = ""
max_value = 0
for i in d:
    if d[i] > max_value:
        max_value = d[i]
        max_key = i
print('the highest value is:', max_key)

# 3.Merge two dictionaries into one d1 = {"a":1, "b":2} d2 = {"c":3, "d":4}.
d1 = {"a":1, "b":2}
d2 = {"c":3, "d":4}
d1.update(d2)
print(d1)

# 4.Invert a Dictionary {"a":1,"b":2,"c":3} Swap keys and values.
d = {"a":1, "b":2, "c":3}
new_dict = {}
for i in d:
    new_dict[d[i]] = i
print(new_dict)

# 5.Remove duplicate values from a dictionary {"a":10,"b":20,"c":10,"d":30}.
d = {'a':10, 'b':20, 'c':10, 'd':30}
new_dict = {}
for i in d:
    if d[i] not in new_dict.values():
        new_dict[i] = d[i]
print(new_dict)

# 6.Group Words ["cat","dog","elephant","bat","tiger"] by Length Create a dictionary that groups words by their length.
words = ["cat","dog","elephant","bat","tiger"]
result = {}
for i in words:
    l = len(i)
    if l not in result:
        result[l] = [i]
    else:
        result[l].append(i)
print(result)

# 7.Sort Dictionary by Values Sort a dictionary {"a":3,"b":1,"c":2} based on values.
d = {'a':3,'b':1,'c':2}
sorted_values = sorted(d.values())
print(sorted_values)

# 8.Find common keys in two dictionaries  {"a":1,"b":2,"c":3} , {"b":20,"c":30,"d":40}.
d1 = {"a":1,"b":2,"c":3}
d2 = {"b":20,"c":30,"d":40}
common = []
for i in d1:
    if i in d2:
        common.append(i)
print(common)

# 9.Write a program to find the sum of all values in dictionary {"a":10,"b":20,"c":30}.
d = {"a":10, "b":20, "c":30}
total = 0
for i in d:
    total = total + d[i]
print(total)

# 10.Create a dictionary using two lists keys = ["a","b","c"] values = [10,20,30].
keys = ["a","b","c"]
values = [10,20,30]
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)

# Class Task
# 1.Write a program to find the total marks of the student.
student = {'name' : 'Narendra',
          'marks' : [86,90,80,95,90]
}
sum = 0
for i in student['marks'] :
 sum = sum + i
print('total:',sum)

# 2.Write a program to find the total marks and arrange them from 1 to 5 rank.
students = [
    {'Name': 'Narendra','Marks': [86,90,80,95,90]},
    {'Name': 'Venkat','Marks': [86,85,68,70,85]},
    {'Name': 'Srinivasan','Marks': [65,90,95,75,80]},
    {'Name': 'Sidtharthan','Marks': [78,85,98,89,63]},
    {'Name': 'Prakash','Marks': [52,78,88,85,68]}
]
for s in students:
    total = 0
    for i in s['Marks']:
        total = total + i
        s['total'] = total
# sort
n = len(students)
for i in range(n):
    for j in range(0,n-i-1):
        if students[j]['total'] < students[j+1]['total']:
            temp = students[j]
            students[j] = students[j+1]
            students[j+1] = temp
rank = 1
for s in students:
    print("Rank", rank, ":", s['Name'], "- total:", s['total'])
    rank = rank + 1

# students = sorted(students, key=lambda x: x['total'], reverse=True)

# Self Task
# 1.Write a program to print only the keys d = {"a":10, "b":20, "c":30}.
d = {"a":10, "b":20, "c":30}
for i in d.keys() :
    print(i)

# 2.Write a program to print only the values d = {"a":10, "b":20, "c":30}.
d = {"a":10, "b":20, "c":30} 
for i in d.values():
    print(i)

# 3.Write a program to print key and value d = {"a":10, "b":20, "c":30}.
d = {"a":10, "b":20, "c":30}
for key, value in d.items() :
    print(key,value)

# 4.Write a program to print sum of all values d = {"a":10, "b":20, "c":30}.
d = {"a":10, "b":20, "c":30}
sum = 0
for i in d :
    sum = sum + d[i]
print(sum)

# 5.Write a program to print count number of items d = {"a":10, "b":20, "c":30}.
d = {"a":10, "b":20, "c":30}
count = 0
for i in d.items():
    count += 1
print(count)

# 6.Write a program to check if key exists d = {"name":"Narendra", "age":28, "city":"Pondy"}.
d = {"name":"Narendra", "age":28, "city":"Pondy"}
if "age" in d:
    print("Key exists")

# 7.Write a program to add a new key d = {"a":10, "b":20}.
d = {"a":10, "b":20}
d["c"] = 30
print(d)

# 8.Write a program to d = {"a":10, "b":20} change value of "a" to 100.
d = {"a":10, "b":20}
d["a"] = 100
print(d)

# 9.Write a program to remove a key "b" d = {"a":10, "b":20, "c":30}.
d = {"a":10, "b":20, "c":30}
d.pop('b')
print(d)

# 10.Write a program to find largest value d = {"a":10, "b":50, "c":30}.
d = {"a":10, "b":50, "c":30}
largest = 0
for i in d.values():
    if i > largest:
        largest = i
print(largest)

# 11.Write a program to count total values greater than 20 d = {"a":10, "b":25, "c":30, "d":5}.
d = {"a":10, "b":25, "c":30, "d":5}
count = 0
for i in d :
    if d[i] > 20 :
        count += d[i]
print(count)

# 12.Write a program to print only keys with even values d = {"a":10, "b":15, "c":20, "d":25}.
d = {"a":10, "b":15, "c":20, "d":25}
for i in d :
    if d[i] %2 == 0 :
        print('even:',d[i])

# 13.Write a program to multiply all values d = {"a":2, "b":3, "c":4}.
d = {"a":2, "b":3, "c":4}
total = 1
for i in d.values():
    total = total * i
print("total:", total)

# 14.Write a program to create a new dictionary with squared values d = {"a":2, "b":3, "c":4}.
d = {"a":2, "b":3, "c":4}
new_d = {}
for key, value in d.items():
    new_d[key] = value * value
print(new_d)

# 15.write a program to find smallest value d = {"a":10, "b":5, "c":30}.
d = {"a":10, "b":5, "c":30}
smallest = list(d.values())[0]
for i in d.values():
    if i < smallest:
        smallest = i
print("smallest:", smallest)

# 16.Write a program to count how many times value appears d = {"a":10, "b":20, "c":10, "d":30}.
d = {"a":10, "b":20, "c":10, "d":30}
count = 0
for i in d.values():
    if i == 10 :
        count = count + i
print(count)

# 17.Write a program to print dictionary in reverse order (keys) d = {"a":10, "b":20, "c":30}.
d = {"a":10, "b":20, "c":30}
keys = list(d.keys())
for i in keys[::-1]:
    print(i)

# 18.Write a program to create dictionary from two lists keys = ["a", "b", "c"] values = [10, 20, 30].
keys = ["a", "b", "c"]
values = [10, 20, 30]
d = {}
for i in range(len(keys)):
        d[keys[i]] = values[i]
print(d)

# 19.Write a program to remove items with value less than 20 d = {"a":10, "b":25, "c":5, "d":30}.
d = {"a":10, "b":25, "c":5, "d":30}
new_d = {}
for key, value in d.items():
    if value >= 20:
        new_d[key] = value
print(new_d)

# 20.Write a program to find key with maximum value d = {"a":10, "b":50, "c":30}.
d = {"a":10, "b":50, "c":30}
max_value = list(d.values())[0]
max_key = ""
for key, value in d.items():
    if value > max_value:
        max_value = value
        max_key = key
print(max_key)

# 21.Write a program to find total marks {'A', 'Marks': [10,20,30]},{'B', 'Marks': [40,50,60]}.
students = [
    {'Name': 'A', 'Marks': [10,20,30]},
    {'Name': 'B', 'Marks': [40,50,60]}
]
for s in students:
    total = 0
    for i in s['Marks']:
        total = total + i
    print(s['Name'], "- Total:", total)

# 22.write a program to find highest total (no sorting).
students = [
    {'Name': 'A', 'Marks': [10,20,30]},
    {'Name': 'B', 'Marks': [40,50,60]}
]
highest = 0
topper = ""
for s in students:
    total = 0
    for i in s['Marks']:
        total = total + i
    print(s['Name'], "- Total:", total)
    # check highest
    if total > highest:
        highest = total
        topper = s['Name']
print("Topper:", topper, "-", highest)

# 23.Write a program to swap manually (understand sorting)
students = [
    {'Name': 'A', 'total': 50},
    {'Name': 'B', 'total': 80}
]
for s in students:
    if s['Name': 'A', 'total': 50]  > s['Name': 'B', 'total': 80] :
        print(s)

# 24.Write a program to sort in descending order.
students = [
    {'Name': 'A', 'total': 70},
    {'Name': 'B', 'total': 90},
    {'Name': 'C', 'total': 80}
]
n=len(students)
for i in range(n):
    for j in range(n-1):
        if students[j]['total'] < students[j+1]['total']:
            temp = students[j]
            students[j] = students[j+1]
            students[j+1] = temp
print(students)

# 24.Write a program to create a dictionary with 5 country - capital pairs, print all keys and values separately.
countries = {
    "India": "New Delhi",
    "USA": "Washington D.C",
    "France": "Paris",
    "Japan": "Tokyo",
    "Australia": "Canberra"
}
for key in countries:
    print(key)
for value in countries.values():
    print(value)

# 25.Write a program to create a dictionary of numbers (1 to 5) where values are their squares. #output {1:1,2:4.....}.
d = {}
for i in range(1, 6):
    d[i] = i * i 
print(d)

# 26.write a program to Merge two dictionaries. If keys are same add their values
d1 = {"a":10, "b":20, "c":30}
d2 = {"d":20, "b":30, "f":40}
result = {}
for key in d1:
    result[key] = d1[key]
for key in d2:
    if key in result:
        result[key] = result[key] + d2[key]   # add values if key same
    else:
        result[key] = d2[key]                 # add new key
print(result)

# 27.Write a program to Invert a dictionary (key become values and value become key).
d = {'a':10,'b':20,'c':30}
new_d = {}
for key in d:
    value = d[key]
    new_d[value] = key
print(new_d)
    
# 28.Write a program to create a nested dictionary for 3 students with : Name, Age, Marks.
details = {
    'student1' : {'name':'tony', 'age' : 28 , 'marks' : 450},
    'student2' : {'name':'stark', 'age' : 28 , 'marks' : 480}
}
print(details)

