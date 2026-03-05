# Tuple():
# It is used to store multiple values in a single variable.What ever we enter in this (,)bracket it shows the type is tuple.
mydata= (10,20,30)
print(type(mydata))

# Ordered it allows the duplicate and we can access this using indexed values.
myTuple=(10,20,30,40)
print(myTuple[1])

# Immuatble: You cannot add, remove, or change items after the tuple is created. This ensure data intergrity.
department = (('ECE'), ('EEE'))
print(department)

# Concatenation is used to add the two data in a same tuple.
ConcatedData= myTuple+mydata
print(ConcatedData)

# Repetation it repeates the value how many times we mentioned using (*).
myName= "Narendra "*3
print(myName)

# Unpacking it means it shows the exact value what we want to print.
name,age,city = ('Stark',28, 'New York')
print(name)

# Count - It counts the repeated value.
myTuple = (10,20,55,24,60,20)
print(myTuple.count(20))

# Index - It shows the index value for the given number.
myNumber = (10,20,30,40,50)
print(myNumber.index(10))

# 1.Create a tuple that contains an integer, a string, and a float.
myTuple = (28,'stark',67.5)
print(myTuple)

# 2.Access the second element of the tuple (5, 10, 15, 20).
numbers = (5,10,15,20)
print(numbers[1])

# 3.Slice the tuple (1, 2, 3, 4, 5) to get the last two elements
values = (1,2,3,4,5)
print(values[3:])

# 4.Concatenate the tuples (1, 2) and (3, 4).
value1 = (1,2)
value2 = (3,4)
concatenateValue = value1+value2
print(concatenateValue)

# 5.Repeat the tuple (7, 8) three times.
myTuple = (7,8) *3
print(myTuple)

# 6.Check if 15 is present in the tuple (10, 20, 15, 25).
numbers = (10,20,15,25)
if 15 in numbers :
    print("15 is present")
else:
    print("15 not present")

# 7.Find the length of the tuple (3, 6, 9, 12).
myTuple = (3,6,9,12)
print(len(myTuple))

# 8.Find the maximum and minimum values in the tuple (4, 1, 8, 3).
values = (4,1,8,3)
print("Maximum value is:", max(values))
print("Minimum value is:", min(values))
# or
maximum = values[0]
minimum = values[0]
for i in values:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print("Maximum value is:", maximum)
print("Minimum value is:", minimum)

# 9.Convert the list [1, 2, 3, 4] into a tuple.
myList =[1,2,3,4]
listtotuple = tuple(myList)
print(listtotuple)

# 10.Convert the tuple (10, 20, 30) into a list.
myTuple = (10,20,30)
tupletolist = list(myTuple)
print(tupletolist)

# 11.Find the index of the element 30 in the tuple (10, 20, 30, 40).
elements = (10,20,30,40)
print(elements.index(30))

# 12.Count how many times 2 appears in the tuple (2, 3, 2, 4, 2).
myTuple = (2,3,2,4,2)
print(myTuple.count(2))

# 13.Unpack the tuple (100, 200, 300) into three separate variables.
values = (100, 200, 300)
mark1, mark2, mark3 = values
print(mark1)
print(mark2)
print(mark3)

# 14.Swap the values of two tuples (1, 2) and (3, 4).
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple1, tuple2 = tuple2, tuple1
print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

# 15.Create a tuple that contains two other tuples (1, 2) and (3, 4).
tuples = ((1, 2), (3, 4))
print(tuples)

# 16.Access the number 4 from the nested tuple ((1, 2), (3, 4)).
myTuple = ((1,2),(3,4))
print(myTuple[1][1])

# 17.Find the sum of all numbers in the tuple (5, 10, 15).
values = (5,10,15)
total = 0
for i in values :
    total += int(i)
print('sum:',total)

# 18.Sort the elements of the tuple (40, 10, 30, 20) in ascending order.
numbers = (40,10,30,20)
# tupletollist
values = list(numbers)
values.sort()
# listtotuple
numbers = tuple(values)
print(numbers)

# 19.Reverse the elements of the tuple (1, 2, 3, 4, 5).
numbers = (1, 2, 3, 4, 5)
reversed_tuple = numbers[::-1]
print(reversed_tuple)

# 20.Check if all elements in the tuple (5, 5, 5, 5) are identical.
numbers = (5, 5, 5, 5)
if all(i == numbers[0] for i in numbers):
    print("All elements are identical")
else:
    print("Elements are not identical")