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

# Task:
# 1.Write a Python program to print all elements of a list using a loop.
myList = [10, 20, 30, 40, 50]
for i in myList:
    print(i)

# 2.Write a Python program to print only the even numbers from a list.
numbers = [12,4,63,1,0,56]
for i in numbers :
    if i %2 == 0:
        print(i)

# 3.Write a Python program to print only the odd numbers from a list.
numbers = [12,4,63,1,0,56]
for i in numbers :
    if i %2 !=0:
        print(i)

# 4.Write a Python program to find the sum of all numbers in a list.
numbers = [5,6,40]
total = 0
for i in numbers :
    total += int(i)
print('sum=',total)

# 5.Write a Python program to find the largest number in a list using a loop.
numbers = [20, 51, 48, 39, 64, 29]
largest = numbers[0]   # Assume first number is largest
for i in numbers:
    if i > largest:
        largest = i
print(largest)

# 6.Write a Python program to find the smallest number in a list using a loop.
numbers = [20, 51, 48, 39, 64, 29]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)

#7.Write a Python program to count how many positive numbers are in a list.
numbers = [20,-51,12,-11,25,48]
count = 0
for i in numbers:
    if i > 0:
        count += 1
print(count)

# 8.Write a Python program to count how many negative numbers are in a list.
numbers = [20,-51,12,-11,25,48]
count = 0
for i in numbers:
    if i < 0 :
        count += 1
print(count)

# 9.Write a Python program to reverse a list without using the .reverse() method.
myList = [10,20,30,40,50]
print(myList[::-1])

# 10.Write a Python program to count how many even and odd numbers are present in a list.
numbers = [12,4,63,1,0,56]
even_count = 0
odd_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers =", even_count)
print("Odd numbers =", odd_count)

# 11. Write a Python program to find and print the index of a specific value in a list.
myList= [10,30,50,88,35,95,100]
print(myList.index(88))

# 12.Write a Python program to replace all negative numbers in a list with 0.
myList = [20,-10,54,30,-12,-22,45]
for i in range(len(myList)):
    if myList[i] < 0:
        myList[i] = 0
print(myList)

# 13.Write a Python program to print all numbers greater than 50 from a list.
myList = [48,24,55,60,38,74,65,10,90]
for i in myList :
    if i > 50 :
        print(i)

# 14. Write a Python program to create a new list containing the squares of each element.
myList = [10,20,30,40,50]
newList = []
for i in myList:
    newList.append(i ** 2)
print(newList)

# 15.Write a Python program to print all duplicate values in a list.
myList = [10,20,30,40,20,60,30,80,60]
duplicates = []
for i in myList:
    if myList.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)

# 16.Write a Python program to print list elements until the number 50 appears (stop when found).
myList = [10, 25, 40, 60, 50, 70, 80]
for i in myList:
    if i == 50:   
        break   # stop when 50 found
    print(i)

# 17.Write a Python program to count how many numbers in a list are divisible by 5.
myList=[10,15,30,42,32,50]
count = 0
for i in myList :
    if i %5 == 0 :
        count += 1
print(count)

# 18.Write a Python program to find the second largest number in a list using loops.
numbers = [10, 45, 32, 67, 89, 54]
largest = numbers[0]
second_largest = numbers[0]
# First find largest
for i in numbers:
    if i > largest:
        largest = i
# Now find second largest
for i in numbers:
    if i > second_largest and i != largest:
        second_largest = i
print("Second largest number is:", second_largest)

# 19.Write a Python program to check whether a list is sorted in ascending order.
numbers = [10, 45, 32, 67, 89, 54]
is_sorted = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break
if is_sorted:
    print("List is sorted in ascending order")
else:
    print("List is NOT sorted in ascending order")

# 20.Write a Python program to find the sum of only the even numbers in a list.
numbers = [5,6,40,3,7,80]
total = 0
for i in numbers :
    if i %2==0:
        total += int(i)
print('sum=',total)

