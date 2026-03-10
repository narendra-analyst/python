# Set {}:
# It is an unordered we cannot access using index[] and it does not allow duplicate, and it is mutable (changeable).
mySet = {10,20,30}
print(mySet)

# Add() - It is used to add the element in the set.
mySet.add(40)
print(mySet)

# Update() - It is used to merge more squences in the set.
myTuple = ('a','b','c','d')
mySet.update(myTuple)
print(mySet)

# Remove() - It removes element is not found,show keyerror.
mySet.remove(40)
print(mySet)

# Discard() - It removes element, don't show any error. If the element is not present.
mySet.discard(50)
print(mySet)

# Pop - It is used to remove an element randomly
mySet.pop()
print(mySet)

# # Clear() - It clear the element in the set, but not the set.
# mySet.clear()
# print(mySet)

# Union() - Returns all element from both sets and also removes the duplicates (OR symbol '|').
Set1 = {10,20,30}
Set2 = {20,40,50,60}
print(Set1.union(Set2))

# Intersection - It returns the common data from both the set (AND symbol '&').
print(Set1.intersection(Set2))

# Difference() - It returns the different elements in the first set but not in the second set (NOT symbol '-').
print(Set1.difference(Set2))

# Symetric_difference() - It returns the different elements in the both set (XOR symbol '^').
print(Set1.symmetric_difference(Set2))

# Relationship test methods:
# issubset() - It checks the same element in the both set and returns the boolean value as True or False.
print({1,2}.issubset({1,2,3}))

# issuperset() - It check the same element in the both set and also check 
print({10,20,30,40}.issuperset({20,10,40,70}))

# isdisjoint() - It returns True if no elements are common in both the set.
print({'a','b','c'}.isdisjoint({'d','e','f'}))

# 1.Given two lists, return the set of common elements that appear more than once in both lists.
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = [2, 2, 4, 4, 4, 6]
result = set()
for i in list1:
    if list1.count(i) > 1 and list2.count(i) > 1:
        result.add(i)
print(result)

# 2.Create a set of unique words from a sentence, where words are separated by spaces and punctuation marks should be ignored.
sentence = "Hello, world! Hello Python. Python is great!"
for p in ",.!?:;":
    sentence = sentence.replace(p, "")
words = sentence.split()
unique_words = set(words)
print(unique_words)

# 3.Write a function that takes a list of numbers and returns the largest subset such that the sum of the subset is even.
numbers = [3, 5, 7]
def largest_even_subset(numbers):
    total = 0
# find total sum
    for i in numbers:
        total = total + i
# if sum is even return the whole list
    if total % 2 == 0:
        return numbers
# if sum is odd, remove one odd number
    for i in numbers:
        if i % 2 != 0:
            numbers.remove(i)
            break
    return numbers
result = largest_even_subset(numbers)
print(result)

# 4.Given a set of integers, write a function that returns a new set containing all subsets of the original set.
numbers = {1, 2, 3}
def get_subsets(s):
    subsets = [set()]   # start with empty subset
    for num in s:
        new_subsets = []
        for subset in subsets:
            new_subset = subset.copy()
            new_subset.add(num)
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
    return subsets
result = get_subsets(numbers)
for subset in result:
 print(subset)


