# # Self Task:
# # 1.Create a tuple with the values 10, 20, 30, 40 and print it.
# myTuple=(10,20,30,40)
# print(myTuple)

# # 2.Access the first element of the tuple (100, 200, 300, 400).
# numbers=(100,200,300,400)
# print(numbers[0])

# # 3.Access the last element of the tuple (5, 10, 15, 20, 25)
# numbers=(5,10,15,20,25)
# print(numbers[4])

# # 4.Slice the tuple (2, 4, 6, 8, 10) to get the first three elements.
# myTuple=(2,4,6,8,10)
# print(myTuple[:3]) 

# # 5.Check if the number 50 is present in the tuple (10, 20, 30, 40, 50).
# values=(10,20,30,40,50)
# if 50 in values :
#  print("50 is present")
# else :
#  print("50 is not present")

# # 6.Find the length of the tuple ("apple", "banana", "cherry", "mango")
# myTuple=('apple','banana','cherry','mango')
# print(len(myTuple))

# # 7.Convert the tuple (7, 14, 21, 28) into a list.
# myTuple=(7,14,21,28)
# tupletolist = list(myTuple)
# print(tupletolist)

# # 8.Convert the list [9, 18, 27, 36] into a tuple.
# myList=[9,18,27,36]
# listtotuple = tuple(myList)
# print(listtotuple)

# # 9.Count how many times "apple" appears in the tuple ("apple", "banana", "apple", "orange", "apple").
# fruits = ("apple", "banana", "apple", "orange", "apple")
# print(fruits.count('apple'))
       
# # 10.Unpack the tuple (10, 20) into two variables and print them.
# a,b = (10,20)
# print(a)
# print(b)

# # 11.Write a Python program to create a list with values 10, 20, 30, 40, 50 and print the list.
# myList=[10,20,30,40,50]
# print(myList)

# # 12.Write a Python program to find the largest number in the list [12, 45, 7, 23, 56, 19].
# numbers=[12,45,7,23,56,19]
# largest = numbers[0]
# for i in numbers :
#  if i > largest :
#   largest = i
# print(largest)
 
# # 13.Write a Python program to count how many even numbers are in the list [10, 21, 32, 43, 54, 65].
# myList=[10,21,32,43,54,65]
# count = 0
# for i in myList :
#  if i %2==0 :
#   count += 1
# print(count)

# # 14.Write a Python program to print all elements of a tuple (5, 10, 15, 20) using a for loop.
# myTuple=(5,10,15,20)
# for i in myTuple:
#  print(i)

# # 15.Write a Python program to find the sum of all numbers in the list [3, 6, 9, 12].
# numbers=[3,6,9,12]
# total = 0
# for i in numbers :
#  total += i
# print('sum:',total)

# # 16.Write a Python program to check if a number is present in a list [5, 15, 25, 35, 45] Check for number 25.
# myList=[5,15,25,35,45]
# if 25 in myList :
#  print('25 is present')
# else:
#  print('25 is not present')

# # 17.Write a Python program to reverse a list [1, 2, 3, 4, 5].
# values=[1,2,3,4,5]
# print(values[::-1])

# # 18.Write a Python program to count the number of positive numbers in the list [-10, 5, 20, -3, 7, -1]
# numbers=[-10,5,20,-3,7,-1]
# count = 0
# for i in numbers :
#  if i > 0 :
#   count += 1
# print(count)

# # 19.Write a Python program to print numbers from 1 to 10 using a for loop.
# for i in range (1,11):
#  print(i)

# # 20.Write a Python program to check whether a number is even or odd. Use the number 17.
# number = 17
# if number %2 == 0:
#  print('even number')
# else:
#  print('odd number')

# # 21.Write a Python program to print all elements of a list [10, 20, 30, 40, 50] using a for loop.
# myList = [10,20,30,40,50]
# for i in myList :
#  print(i)

# # 22.Write a Python program to find the smallest number in the list [34, 12, 78, 5, 23].
# numbers = [34,12,78,5,23]
# smallest = numbers[0]
# for i in numbers:
#  if i < smallest :
#   smallest = i
# print(smallest)

# # 23.Write a Python program to count how many odd numbers are in the list [11, 20, 33, 40, 55, 60].
# myList = [11,20,33,40,55,60]
# count = 0
# for i in myList:
#  if i %2 != 0 :
#   count += 1
# print(count)

# # 24.Write a Python program to find the sum of all even numbers in the list [2, 5, 8, 11, 14, 17].
# myList = [2,5,8,11,14,17]
# total = 0
# for i in myList :
#  if i %2 == 0 :
#   total += i
# print(total)

# # 25.Write a Python program to print numbers from 10 to 1 using a for loop.
# for i in range (11,0,-1) :
#  print(i)

# # 26.Write a Python program to find the second largest number in the list [10, 45, 32, 67, 89, 54].
# numbers = [10,45,32,67,89,54]
# largest = numbers[0]
# second_largest = numbers[0]
# for i in numbers :
#     if i > largest :
#         largest = i
# # second largest
# for i in numbers :
#     if i > second_largest and i != largest:
#        second_largest = i
# print(second_largest)

# # 27.Write a Python program to remove duplicates from a list [10, 20, 30, 20, 40, 10, 50].
# myList = [10,20,30,20,40,10,50]
# duplicates = []
# for i in myList :
#     if myList.count(i) > 1 and i not in duplicates :
#         duplicates.append(i)
# print(duplicates)

# # 28.Write a Python program to check whether a list [10,20,30,40,50] is sorted in ascending order.
# myList = [10, 20, 30, 40, 50]
# for i in range(len(myList)-1):
#     if myList[i] > myList[i+1]:
#         print("list is not sorted in ascending order")
#         break
# else:
#     print("list is sorted in ascending order")
# # or
# myList = [10,20,30,40,50]
# if myList == sorted(myList):
#     print("list is sorted in ascending order")
# else:
#     print("list is not sorted")

# # 29.Write a Python program to count how many times the number 5 appears in the list [5, 3, 5, 7, 5, 9, 1].
# myList = [5,3,5,7,5,9,11]
# print(myList.count(5))

# # 30.Write a Python program to print only negative numbers from the list [10, -5, 7, -2, 15, -8].
# numbers = [10,-5,7,-2,15,-8]
# for i in numbers:
#     if i < 0 :
#         print(i)

# # 31.Write a Python program to print all numbers greater than 25 from the list [10, 30, 20, 40, 15, 50].
# numbers = [10,30,20,40,15,50]
# for i in numbers :
#   if i > 25 :
#     print(i)

# # 32.Write a Python program to count how many numbers are divisible by 3 in the list [3, 10, 15, 22, 30, 41].
# numbers = [3,10,15,22,30,41]
# count = 0
# for i in numbers :
#   if i %3 == 0 :
#     count += 1
# print(count)

# # 33.Write a Python program to find the product (multiplication) of all numbers in the list [1, 2, 3, 4, 5].
# numbers = [1, 2, 3, 4, 5]
# product = 1
# for i in numbers:
#     product *= i
# print("Product:", product)

# # 34.Write a Python program to print the index and value of each element in the list [10, 20, 30, 40].
# elements = [10,20,30,40]
# print('index 0 value is :',elements[0])
# print('index 1 value is :',elements[1])
# print('index 2 value is :',elements[2])
# print('index 3 value is :',elements[3])
# # or
# elements = [10,20,30,40]
# for i in range(len(elements)):
#     print("Index", i, "Value", elements[i])

# # 35.Write a Python program to find the average of numbers in the list [10, 20, 30, 40, 50].
# myList = [10,20,30,40,50]
# total = 0
# for i in myList:
#     total += i
# average = total / len(myList)
# print("Average:", average)

# # 36.Write a Python program to print only even numbers from the list [11, 22, 33, 44, 55, 66].
# myList = [11,22,33,44,55,66]
# for i in myList :
#    if i % 2 == 0 :
#       print(i)

# # 37.Write a Python program to count how many numbers are greater than 50 in the list [23, 67, 45, 89, 12, 90].
# myList = [23, 67, 45, 89, 12, 90]
# count = 0
# for i in myList :
#    if i > 50 :
#       count += 1
# print(count)

# # 38.Write a Python program to create a new list containing the square of numbers from the list [1, 2, 3, 4, 5].
# myList = [1, 2, 3, 4, 5]
# newList = []
# for i in myList:
#     newList.append(i ** 2)
# print(newList)

# # 39.Write a Python program to find the smallest and largest number in the list [14, 2, 89, 45, 7].
# numbers = [14, 2, 89, 45, 7] 
# largest = numbers [0]
# for i in numbers :
#    if i > largest :
#       largest = i
# # for smallest number
# smallest = numbers[0]
# for i in numbers:
#     if i < smallest:
#         smallest = i
# print(largest)
# print(smallest)

# # 40.Write a Python program to print numbers from 1 to 20 that are divisible by 4.
# for i in range (1,21) :
#    if i %4 == 0 :
#       print(i)

# # Set Task
# # 1.Write a program to create a set with numbers {10, 20, 30, 40} and print it.
# mySet = {10,20,30,40}
# print(mySet)

# # 2.Write a program to create a set {1, 2, 3} and add 4 to it. Print the result.
# mySet = {1,2,3}
# mySet.add(4)
# print(mySet)

# # 3.Write a program to create a set {5, 10, 15, 20} and remove 10.
# mySet = {5,10,15,20}
# mySet.remove(10)
# print(mySet)

# # 4.write a program to create a set {100, 200, 300} and check if 200 is present.
# mySet = {100,200,300}
# if 200 in mySet :
#     print('200 is present')
# else:
#     print('200 is not present')

# # 5.Write a program to create a set {2, 4, 6, 8, 10} and print how many elements are there.
# mySet = {2,4,6,8,10}
# print(len(mySet))

# # 6.Write a program to create union of Two Sets A = {1, 2, 3} B = {3, 4, 5}.
# A = {1, 2, 3}
# B = {3, 4, 5}
# print(A.union(B))

# # 7.Write a program to intersection of two sets A = {1, 2, 3} B = {3, 4, 5}.
# A = {1, 2, 3}
# B = {3, 4, 5}
# print(A.intersection(B))

# # 8.Wrtie a program to find difference of sets A = {1, 2, 3} and B = {3, 4, 5}.
# A = {1, 2, 3}
# B = {3, 4, 5}
# print(A.difference(B))

# # 9.Write a program to remove duplicates from list, convert list [1, 2, 2, 3, 4, 4, 5] into a set.
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = set(numbers)
# print(unique_numbers)

# # 10.write a program to loop through a set pint all elements from {10, 20, 30} using loop.
# mySet = {10,20,30,}
# for i in mySet:
#     print(i)

# # 11.write a program to find largest number in {10, 50, 20, 70, 30} using loop.
# numbers = {10,50,20,70,30}
# largest = 0
# for i in numbers :
#     if i > largest :
#         largest = i
# print(largest)

# 12.Write a program to create a set {1, 2, 3} and add elements 4, 5 using update().
myset = {1, 2, 3}
numbers = {4,5}
myset.update(numbers)
print(myset)

# 13.Write a program to create a set {10, 20, 30} and remove 40 without getting error.
myset = {10,20,30}
myset.discard(40)
print(myset)

# 14.Write a program to create a set {5, 10, 15} and remove all elements.
myset = {5,10,15}
myset.clear()
print(myset)

# 15.write a program to create a set {1, 2, 3} and copy it into another set.
set1 = {1, 2, 3}
set2 = set1.copy()
print("Original Set:",set1)
print("Copied Set:",set2)

# 16.Write a program to find the smallest number in {25, 10, 45, 5, 30} using loop.
numbers = {25, 10, 45, 5, 30}
numbers_list = list(numbers)
smallest = numbers_list[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("Smallest number:", smallest)

# 17.Write a program to count how many even numbers are in {1, 2, 3, 4, 5, 6}.
numbers = {1,2,3,4,5,6}
count = 0
for i in numbers :
    if i % 2 == 0 :
        count += 1
print("no. of even numbers:",count)

# 18.Write a program to convert "hello" into a set and print it.
name = 'hello'
name2 = set(name)
print(name2)

# 19.Write a program check if {1, 2} is a subset of {1, 2, 3, 4}.
myset = {1,2,3,4}
print({1,2}.issubset(myset))

# 20.Write a program find elements that are in either set but not bothA = {1, 2, 3} B = {3, 4, 5}.
A = {1, 2, 3}
B = {3, 4, 5}
print(A.symmetric_difference(B))

# 21.Write a program to find sum of all elements in {10, 20, 30, 40} using loop.
myset = {10,20,30,40}
total = 0
for i in myset :
    total = total + i
print("sum:",total)

# 22.Write a program to find common elements between 3 sets A = {1, 2, 3} B = {2, 3, 4} C = {3, 4, 5}.
A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}
print(A.intersection(B, C))
