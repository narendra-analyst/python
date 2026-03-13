# A dictionary in Python is a built-in, mutable, and ordered collection data structure used to store data in key-value pairs. 
# Format : {key : word} , {name : narendra}
student = {'Name': 'Narendra', 'Age': 28, 'City': 'Pondy'}
print(student)

# To access specific value
print(student['Name'])
print(student.get('Name'))

# To add or update value
# print(student['Phone'])  # Through error if we access unknown value
print(student.get('Phone'))  # does not show any error, shows None

# Pop method
print(student.pop('Age'))  # remove the value inside the pop
print(student.popitem())   # removes the last added value

# Delete Method
del student['Age']
print(student)

# Clear Method
student.clear()
print(student)
