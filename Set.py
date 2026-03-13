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

# 3.Write a program that takes a list of numbers and returns the largest subset such that the sum of the subset is even.
numbers = [3, 5, 7]
total = 0
# find total sum
for i in numbers:
    total = total + i
# if sum is even return the whole list
if total % 2 == 0:
    result = numbers
# if sum is odd, remove one odd number
else:
    for i in numbers:
        if i % 2 != 0:
            numbers.remove(i)
            break
    result = numbers
print(result)

# 4.Given a set of integers, write a function that returns a new set containing all subsets of the original set.
s = {1, 2, 3}
nums = list(s)
n = len(nums)
subsets = []
for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(nums[j])
    subsets.append(subset)
print(subsets)

# 5.Check if two sets are equal, considering their elements but ignoring the order (i.e., set equality).
a = {1, 2, 3}
b = {3, 2, 1}
def check_sets_equal(set1, set2):
    if len(set1) != len(set2):
        return False
    for i in set1:
        if i not in set2:
            return False
    return True
print(check_sets_equal(a, b))
# or
def check_sets_equal(set1, set2):
    if len(set1) == len(set2):
        return True
    else:
     return False
print(check_sets_equal(a, b))

# 6.Write a program that finds the intersection of multiple sets.
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}
sets = [set1, set2]
result = sets[0]
for s in sets[1:]:
    result = result.intersection(s)
print(result)

# 7.Find the set difference of multiple sets.
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}
sets = [set1, set2]
result = sets[0]
for s in sets[1:]:
   result = result.difference(s)
print(result)

# 8.Given a list of sets, write a program to return the set containing elements that are present in every set in the list.
sets = [{1, 2, 3, 4}, {2, 3, 5}, {2, 3, 6}]
result = sets[0]
for s in sets:
    result = result.intersection(s)
print(result)

# 9.Write a program that checks if a set of strings forms a palindrome when concatenated together.
s = {"ma", "dam"}
text = ""
for word in s:
    text = text + word
reverse = text[::-1]
if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# 10.Given a set, find the number of distinct subsets where the sum of the elements in each subset is divisible by a given integer.
numbers = {1, 2, 3}
k = 3   # given integer
nums = list(numbers)
n = len(nums)
count = 0
# generate all subsets
for i in range(1 << n):
    subset_sum = 0    
    for j in range(n):
        if (i & (1 << j)) != 0:
            subset_sum = subset_sum + nums[j]   
    if subset_sum % k == 0:
        count = count + 1
print("Number of subsets:", count)

# 11.Write a program that finds the longest consecutive sequence in an unsorted list of numbers using sets.
numbers = [100, 4, 200, 1, 3, 2]
numbers.sort()
longest = 1
count = 1
for i in range(len(numbers) - 1):
    if numbers[i] + 1 == numbers[i + 1]:
        count = count + 1
    else:
        if count > longest:
            longest = count
        count = 1
if count > longest:
    longest = count
print(longest)

# 12.Given two sets, find the symmetric difference, but only include elements that appear more than once across both sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
def symmetric(a, b):
    sym_diff = a.symmetric_difference(b)
    combined = list(a) + list(b)
    result = set()
    for i in sym_diff:
        if combined.count(i) > 1:
            result.add(i)
    return result
print(symmetric(set1, set2))

# 13.Write a function that checks if there exists a pair of numbers in a set that sum to a specific target
numbers = {2, 4, 7, 11}
target = 9
def pair_sum(s, target):
    for num in s:
        needed = target - num
        if needed in s and needed != num:
            return True
    return False
print(pair_sum(numbers, target))

# 14.Write a function to determine whether a set is a proper subset of another set.
set1 = {1,2}
set2 = {1,2,3}
def subset(a, b):
    if len(a) >= len(b):
        return False
    for i in a:
        if i not in b:
            return False
    return True
print(subset(set1, set2))

# 15.Write a function that returns the elements in a set which are not present in any of the other sets from a list of sets.
A = {1,2,3,4,5}
sets = [{2,3}, {4,6}, {7,8}]
def unique_elements(main_set, set_list):
    result = set()
    for item in main_set:
        found = False
        for s in set_list:
            if item in s:
                found = True
                break
        if not found:
            result.add(item)
    return result
print(unique_elements(A, sets))

# 16.Find all possible subsets of a set and return the ones where the sum of elements is prime.
s = {1, 2, 3}
nums = list(s)
n = len(nums)
result = []
for i in range(1 << n):
    subset = []
    subset_sum = 0
    for j in range(n):
        if i & (1 << j):
            subset.append(nums[j])
            subset_sum = subset_sum + nums[j]
    # check if subset_sum is prime
    if subset_sum > 1:
        count = 0
        for k in range(1, subset_sum + 1):
            if subset_sum % k == 0:
                count = count + 1
        if count == 2:
            result.append(subset)
print(result)

# 17.Create a set of all permutations of a given list of characters.
chars = ['a', 'b', 'c']
permutations = set()
for i in range(len(chars)):
    for j in range(len(chars)):
        for k in range(len(chars)):
            if i != j and j != k and i != k:
                perm = chars[i] + chars[j] + chars[k]
                permutations.add(perm)
print(permutations)

# 18.Check if a set contains a subset of elements that sum up to a specific value
s = {2, 4, 6, 10}
target = 16
nums = list(s)
n = len(nums)
found = False
for i in range(1 << n):
    subset_sum = 0
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset_sum += nums[j]
            subset.append(nums[j])
    if subset_sum == target:
        print("Subset found:", subset)
        found = True
        break
if not found:
    print("No subset found")

# 19.Find the number of elements that appear in exactly one set from a list of sets.
sets = [{1,2,3}, {3,4,5}, {5,6}]
all_elements = set()
for s in sets:
    for i in s:
        all_elements.add(i)
count = 0
for elem in all_elements:
    freq = 0    
    for s in sets:
        if elem in s:
            freq += 1
    if freq == 1:
        count += 1
print(count)

# 20.Write a program that finds the union of all sets, but only includes elements that appear more than once across all sets.
sets = [{1,2,3}, {3,4,5}, {5,6}]
all_elements = set()
for s in sets:
    for i in s:
        all_elements.add(i)
result = set()
for elem in all_elements:
    count = 0
    for s in sets:
        if elem in s:
            count += 1
    if count > 1:
        result.add(elem)
print(result)