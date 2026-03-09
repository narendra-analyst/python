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

# Union() - Returns all element from both sets and also removes the duplicates.
Set1 = {10,20,30}
Set2 = {20,40,50,60}
print(Set1.union(Set2))

# Intersection - It returns the common data from both the set.
print(Set1.intersection(Set2))

# Difference() - It returns the different elements in the first set but not in the second set.
print(Set1.difference(Set2))

# Symetric_difference() - It returns the different elements in the both set.
print(Set1.symmetric_difference(Set2))

# Relationship test methods:
# issubset() - It checks the same element in the both set and returns the boolean value as True or False.
print({1,2}.issubset({1,2,3}))

# issuperset() - It check the same element in the both set and also check 
print({10,20,30,40}.issuperset({20,10,40,70}))

# isdisjoint() - It returns True if no elements are common in both the set.
print({'a','b','c'}.isdisjoint({'d','e','f'}))




