# SET PRACTICE QUESTIONS
# 🟢 Basic Level (Beginner)

# Create a set with 5 different numbers and print it.
s={1,2,3,4,5}
print(s)

# Create an empty set and check its type.
s=set()
print(type(s))

# Add one new element to a set using .add().
s={1,2,3,4,5}
s.add(6)
print(s)

# Add multiple elements at once using .update().
s={1,2,3,4,5}
s.update([7,8,9])
print(s)

# Remove an element using .remove().
s={1,2,3,4,5}
s.remove(5)
print(s)

# Try removing an element that doesn’t exist using .discard() and observe the difference.
s={1,2,3,4,5}
s.discard(7)
print(s)

# Remove and print a random element using .pop().
s={1,2,3,4,5}
print(s.pop())

# Clear all elements from a set using .clear().
s={1,2,3,4,5}
(s.clear())
print(s)

# Check if a specific element (like 5) exists in a set using the in keyword.
s={1,2,3,4,5}
if 5 in s:
    print("exists")
else:
    print("not exits")
# Find the length of a set using len().
s={1,2,3,4,5}
print(len(s))

# Intermediate Level (Set Operations)

# Create two sets and find their union using .union() and |.
s1={1,2,3,4}
s2={5,6,7,8}
print(s1.union(s2))

# Create two sets and find their intersection using .intersection() and &.
s1={1,2,3,4}
s2={5,2,7,8}
print(s1.intersection(s2))


# Find the difference between two sets using .difference() and -.
s1={1,2,3,4}
s2={5,2,7,8}
print(s1.difference(s2))

# Find the symmetric difference between two sets using .symmetric_difference() and ^.
s1={1,2,3,4}
s2={5,2,7,8}
print(s1.symmetric_difference(s2))

# Check if one set is a subset of another using .issubset().
s1={1,2,3,4}
s2={5,2,7,8,1,3,4}
print(s1.issubset(s2))

# Check if one set is a superset of another using .issuperset().
s1={1,2,3,4,5,7,8}
s2={5,2,7,8}
print(s1.issuperset(s2))

# Check if two sets are disjoint using .isdisjoint().
s1={1,2,3,4}
s2={5,6,7,8}
print(s1.isdisjoint(s2))

# Advanced Level (Functions and Mixed Concepts)

# Create a set of numbers {1,2,3,4,5} and find the max, min, and sum.
numbers={1,2,3,4,5}
print(max(numbers))

numbers={1,2,3,4,5}
print(min(numbers))

numbers={1,2,3,4,5}
print(sum(numbers))
# Use the sorted() function to print the set {5,1,3,2} in ascending order.
numbers={5,1,3,2,6}
print(sorted(numbers))
# Write a program to count how many unique elements are in a list using set().
numbers=[5,1,5,3,2,6]
print(len(set(numbers)))
# Convert a list [1,2,2,3,3,4,5] into a set to remove duplicates.
list= [1,2,2,3,3,4,5]
new_list=set([1,2,2,3,3,4,5])
print(new_list)
# Create a set from a string "banana" and print it. (What happens to duplicate letters?)
print(set("banana"))
# Combine two sets using .update() and print the final set.
s1={1,2,3}
s2={4,5,6}
s1.update(s2)
print(s1)


# Create two sets — print elements common to both using intersection.
s1={1,2,3}
s2={4,3,6}
print(s1.intersection(s2))
# Create two sets — print elements that are only in the first but not in the second.
s1={1,2,3,4,5}
s2={4,3,5}
print(s1.difference(s2))
# Create two sets — print elements that are either in one or the other, but not both.
s1={1,2,3,4,5}
s2={4,3,5}
print(s1.symmetric_difference(s2))
# Create a set with numeric values and use any() and all() functions on it.
numbers={1,2,3,4,5}
print(any(numbers))
print(all(numbers))
# Convert a tuple into a set and print it.
tuple_1=("apple","banana","cherry")
new_tuple=set(("apple","banana","cherry"))
print(new_tuple)
# Create a frozen set and try to modify it — what happens?
frozen_set=frozenset({1,2,3,2})
print(frozen_set)
# frozen_set.add(4)u can add if set become frozen ,frozen set doesnot allow mofificationa in the setafter frozen
# print(frozen_set)

# Write a program to check if two lists contain any common elements using sets.
list1=[1,2,3]
s1=set([1,2,3])
list2=[4,5,6,2]
s2=set([4,5,6,2])
print(s1.intersection(s2))

# Bonus Challenges (For extra practice 🌟)

# Create a set {10,20,30} and remove elements one by one using .pop() until it’s empty.
number={10,20,30}
print(number.pop())
print(number.pop())
print(number.pop())

# Write a Python program to find the intersection of three sets.
s1={1,2,6}
s2={4,5,6}
s3={7,8,6}
print(s1.intersection(s2,s3))

# Given a sentence, print all unique words using a set.
sentence=['my','name','is','neelam','my','hobby','is','cooking']
print(set(sentence))
# Write a Python program to find common letters between two input words.
name1=input("type any word :")
new_name1=set(name1)
name2=input("type nd word:")
new_name2=set(name2)
print(new_name1.intersection(new_name2))
# Write a Python program to find letters that appear only once in a given word using a set.
word="neelam"
unique_letters = {ch for ch in word if word.count(ch) == 1}
print(unique_letters)
