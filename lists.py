# Create a list of 5 fruits and print it.
fruits=['apple','banana','kiwi','mango','pears']
print(fruits)

# Add one more fruit at the end of the list using append().
fruits=['apple','banana','kiwi','mango','pears']
fruits.append("grapes")
print(fruits)

# Insert a fruit at the 2nd position using insert().
fruits=['apple','banana','kiwi','mango','pears']
fruits.insert(2,"orange")
print(fruits)

# Remove a specific fruit from the list using remove().
fruits=['apple','banana','kiwi','mango','pears']
fruits.remove('banana')
print(fruits)

# Print the length of the list using len().
fruits=['apple','banana','kiwi','mango','pears']
print(len(fruits))

# Create a list of numbers [1, 2, 3, 4, 5] and remove the last element using pop().
numbers=[1, 2, 3, 4, 5]
numbers.pop()
print(numbers)

# Copy one list into another using copy().
numbers=[1,2,3,4,5]
new_list=numbers.copy()
print(new_list)

# Count how many times the value 2 occurs in [1, 2, 3, 2, 4, 2].
numbers=[1, 2, 3, 2, 4, 2]
print(numbers.count(2))

# Sort the list [4, 2, 9, 1, 7] in ascending and then descending order.
numbers=[4, 2, 9, 1, 7]
numbers.sort()
print(numbers)

# for decsecding order
numbers= [4, 2, 9, 1, 7]
numbers.sort(reverse=True)
print(numbers)

# Reverse the list [10, 20, 30, 40, 50] using reverse().
numbers= [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

# Combine two lists [1, 2, 3] and [4, 5, 6] using extend().
list1= [1, 2, 3]
list1.extend([4, 5, 6])
print(list1)

# Find the maximum and minimum value from the list [5, 10, 15, 2, 7].
list1=[5, 10, 15, 2, 7]
print("min is:",min(list1))
print("max is:",max(list1))

# Use slicing to print the first 3 elements of a list [10, 20, 30, 40, 50].
numbers=[10, 20, 30, 40, 50]
print(numbers[0:3])

# Remove all elements from a list using clear().
numbers=[10, 20, 30, 40, 50]
numbers.clear()
print(numbers)

# Create a list of numbers and print the sum of all numbers using sum().
numbers=[10, 20, 30, 40, 50]
print(sum(numbers))

# Delete the element at index 2 from a list using the del keyword.
numbers=[10, 20, 30, 40, 50]
del numbers[2]
print(numbers)

# Create a nested list and print an inner element (for example [1, [2, 3], 4] → print 3).
numbers=[1, [2, 3], 4]
print(numbers[1][1])

# write a program to aks the user to enter names of their 3 favourite movies and stores them in a list
movies=[]
mov1=input("enter 1st movie:")
mov2=input("enter 2nd movie:")
mov3=input("enter 3rd movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# write a program to check if alist contains a palindrome of elements
list=[1,2,3,2,1]
reverse=list[::-1]
if(list==reverse):
    print("it is a palindrom")
else:
    print("it is not a plaindrome")

# take input from user
list=input("enter a list:")
new_list=list.split()
reverse=new_list[::-1]
if(new_list==reverse):
    print("it is a palindrom")
else:
    print("it is not a plaindrome")
