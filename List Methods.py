# List is used to store multiple values in a single variable.
myList = [10,20,30,40,50]
print(myList)

myList = ['NA1997','Narenrda',861347810,True]
print(myList)

# Index Method
print(myList[1:])
print(myList[1:4])
print(myList[:2])
print(myList[::-1])

# Append
myList.append('Narendra')
print(myList)

# Pop - if index value is given it removes only that or it removes the last element.
myList.pop(2)
print(myList)

# Extended - Add multiple items to the end, for that we should have to create list like myTuple.
myTuple = ('ECE','EEE')
myList.extend(myTuple)
print(myList)

# Insert - used to add the element exactly in which position we want for that we have to mention that in index().
myList.insert(1,'IT')
print(myList)

# Remove - It removes the first occurence of value.
myList.remove(20)
print(myList)

# Index - It checks the index position.
print(myList.index(40))

# Count - It counts the given value how many times it repeated.
print(myList.count('ECE'))

# Sort - It arranges the value that stored in variable in a ascending order.
numbers=[12,4,63,1,0,56]
numbers.sort()
print(numbers)

# Reverse - It arranges the value that stored in variable in a reverse order.
numbers.reverse()
print(numbers)

# Clear - It removes all elements from the list and makes it empty and it don't delete the variable.
myList.clear()
print(myList)

# Copy - It creates a new list with the same elements as the original list.
newList=myList.copy()
print(newList)

# To print the even numbers using list method.
for i in numbers :
  if i %2 == 0:
    print(i)
    
# To print the even numbers and assign in new list.
evennumbers=[] 
for i in numbers :
  if i % 2 == 0:
    evennumbers.append(i)
print(evennumbers)

# Print the even and odd numbers and assign in seperate list.
evennumbers = []
oddnumbers = []
for i in numbers:
    if i % 2 == 0:
        evennumbers.append(i)
    else:
        oddnumbers.append(i)
print("Even:", evennumbers)
print("Odd:", oddnumbers)

