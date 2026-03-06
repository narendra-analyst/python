# Self Task:
# 1.Create a tuple with the values 10, 20, 30, 40 and print it.
myTuple=(10,20,30,40)
print(myTuple)

# 2.Access the first element of the tuple (100, 200, 300, 400).
numbers=(100,200,300,400)
print(numbers[0])

# 3.Access the last element of the tuple (5, 10, 15, 20, 25)
numbers=(5,10,15,20,25)
print(numbers[4])

# 4.Slice the tuple (2, 4, 6, 8, 10) to get the first three elements.
myTuple=(2,4,6,8,10)
print(myTuple[:3])

# 5.Check if the number 50 is present in the tuple (10, 20, 30, 40, 50).
values=(10,20,30,40,50)
if 50 in values :
 print("50 is present")
else :
 print("50 is not present")

# 6.Find the length of the tuple ("apple", "banana", "cherry", "mango")
myTuple=('apple','banana','cherry','mango')
print(len(myTuple))

# 7.Convert the tuple (7, 14, 21, 28) into a list.
myTuple=(7,14,21,28)
tupletolist = list(myTuple)
print(tupletolist)

# 8.Convert the list [9, 18, 27, 36] into a tuple.
myList=[9,18,27,36]
listtotuple = tuple(myList)
print(listtotuple)

# 9.Count how many times "apple" appears in the tuple ("apple", "banana", "apple", "orange", "apple").
fruits = ("apple", "banana", "apple", "orange", "apple")
print(fruits.count('apple'))
       
# 10.Unpack the tuple (10, 20) into two variables and print them.
a,b = (10,20)
print(a)
print(b)

# 11.Write a Python program to create a list with values 10, 20, 30, 40, 50 and print the list.
myList=[10,20,30,40,50]
print(myList)

# 12.Write a Python program to find the largest number in the list [12, 45, 7, 23, 56, 19].
numbers=[12,45,7,23,56,19]
largest = numbers[0]
for i in numbers :
 if i > largest :
  largest = i
print(largest)
 
# 13.Write a Python program to count how many even numbers are in the list [10, 21, 32, 43, 54, 65].
myList=[10,21,32,43,54,65]
count = 0
for i in myList :
 if i %2==0 :
  count += 1
print(count)

# 14.Write a Python program to print all elements of a tuple (5, 10, 15, 20) using a for loop.
myTuple=(5,10,15,20)
for i in myTuple:
 print(i)

# 15.Write a Python program to find the sum of all numbers in the list [3, 6, 9, 12].
numbers=[3,6,9,12]
total = 0
for i in numbers :
 total += i
print('sum:',total)

# 16.Write a Python program to check if a number is present in a list [5, 15, 25, 35, 45] Check for number 25.
myList=[5,15,25,35,45]
if 25 in myList :
 print('25 is present')
else:
 print('25 is not present')

# 17.Write a Python program to reverse a list [1, 2, 3, 4, 5].
values=[1,2,3,4,5]
print(values[::-1])

# 18.Write a Python program to count the number of positive numbers in the list [-10, 5, 20, -3, 7, -1]
numbers=[-10,5,20,-3,7,-1]
count = 0
for i in numbers :
 if i > 0 :
  count += 1
print(count)

# 19.Write a Python program to print numbers from 1 to 10 using a for loop.
for i in range (1,11):
 print(i)

# 20.Write a Python program to check whether a number is even or odd. Use the number 17.
number = 17
if number %2 == 0:
 print('even number')
else:
 print('odd number')