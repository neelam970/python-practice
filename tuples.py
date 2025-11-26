# Create a tuple with 5 different fruits and print it.
my_tuple=('apple','banana','orange','mango','kiwi')
print(my_tuple)

# Create a tuple with one element and check its type.
t=(4,)
print(type(t))

# Access the 3rd element from a tuple (10, 20, 30, 40, 50).
t=(10, 20, 30, 40, 50)
print(t[2])

# Print the last element of a tuple using negative indexing.
t=(10, 20, 30, 40, 50)
print(t[-1])

# Use slicing to print the first three elements of a tuple (1, 2, 3, 4, 5).
t=(1, 2, 3, 4, 5)
print(t[0:3])

# Create a tuple of 5 numbers and find the maximum and minimum values.
t=(1, 2, 3, 4, 5)
print(max(t))
print(min(t))

# Count how many times a particular element (like 2) appears in (1, 2, 3, 2, 4, 2).
t=(1, 2, 3, 2, 4, 2)
print(t.count(2))

# Find the index of an element (like 4) in (2, 4, 6, 8, 10).
a=(2, 4, 6, 8, 10)
print(a.index(4))

# Check if an element exists in a tuple or not (using the in operator).
a=(2, 4, 6, 8, 10)
print(2 in a)
print(50 in a)

# Concatenate two tuples and print the result.
t1=(1,22,33)
t2=(2,22,33)
print(t1+t2)

# Repeat a tuple 3 times using the * operator.
t1=(1,22,33)
print(t1*3)

# Create a nested tuple and access an inner element (e.g., (1, (2, 3), 4) → print 3).
t=(1, (2, 3), 4)
print(t[1][1])

# Convert a tuple into a list, add a new element, and convert it back into a tuple.
t1=(1,22,33)
new_list=list(t1)
print(new_list)
new_list.append(44)
print(new_list)
new_tuple=tuple(new_list)
print(new_tuple)

# Unpack a tuple of 3 elements into three variables and print them.
t=(1,2,3)
a,b,c=t
print(a)
print(b)
print(c)

# Write a program to compare two tuples for equality.
t1=(1,2,3,4)
t2=(1,2,3,5)
print(t1==t2)

# Find the sum of all numeric elements in a tuple.
t=(1,2,3,4)
print(sum(t))

# Create a tuple containing both numbers and strings and print only the string elements.
t1=(1,2,'neelam','komal',65)
print(t1[3])
print(t1[2])

# correct way
for i in t1:
    if type(i) == str:
        print(i)

# write a program to aks the user to enter names of their 3 favourite movies and stores them in a list
movies=[]
movie_1=input("enter your 1st movie:")
movie_2=input("enter your 2st movie:")
movie_3=input("enetr your 3rd movie:")

movies.append(movie_1)
movies.append(movie_2)
movies.append(movie_3)

print(movies)
new_tuple=tuple(movies)
print(new_tuple)

# write a program to check if alist contains a palindrome of elements
t1=input("enter a tuple:")
reversed=t1[::-1]
if(t1==reversed):
    print("it is a pelindrome")
else:
    print("it is not a palindrome")

