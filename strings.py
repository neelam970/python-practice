#Take a string input and print its length.
name=(input("name is:"))
print("len is:",len(name))

# Take a string input and print the first and last character.
name=input("enter a string;")
print(name[0],name[-1])

# Write a Python program to print each character of a string on a new line.
name=input("enter a string:")
print('\n'.join(name))

# Take a string and print it in uppercase and lowercase.
word=input("enter string:")
print(word.upper())
print(word.lower())

# Take a string input from the user and convert it to title case (first letter of each word capitalized).
name=input("enter string:")
print(name.title())

# Take a string input and check whether it starts with a particular letter.
name=input("enter a string:")
if(name.startswith('a')):
    print("yes")
else:
    print("no")

# Take two strings and concatenate (join) them together.
str1="neelam"
str2="kumari"
str_concat=str1+""+str2
print(str_concat)

# 2nd method
str1="pihu"
str2="kumari"
concat=str1+str2
print('-'.join(concat))

# Write a program to reverse a string using slicing.
word="python"
print(word[::-1])
# Take a string and find how many times a particular character occurs.
word="commerece" 
print(word.count('e'))

# Check whether the given string contains only alphabets, digits, or special characters.
name=input("enter a string:")
if(name.isalpha()):
    print("it is an alphabet")
elif(name.isdigit()):
    print("it is a digit")
else:
    print("special character")

# Take a string and check whether it is a palindrome (same forwards and backwards).
name=input("enter a string:")
reverse=name[::-1]
if(name==reverse):
    print("it is a palidrome")
else:
    print("it is not a palindrome")

# Take a string and replace all occurrences of a specific character with another character.
word="pythom"
print(word.replace('m','n'))

# Take a string and remove all spaces from it.
word=" python "
print(word.strip())

# if u want to remove spaces between the strings then u hve to do
word="python kumari"
print(word.replace(" ",""))

# if u want to remove spaces between the text then u hve to do
word="py thon"
print(word.replace(" ",""))

# Take a string and split it into a list of words.
word="python is a good prog langhg"
print(word.split())

# Take a string and count the number of words in it.
word="python is good,python is free,python is open source"
print(word.count('python'))

# Take a string and check whether it contains a specific index of substring.
word="hello"
print(word.find("l"))

# Take a string and check whether it contains a specific  substring.
word="python"
if 'ii' in word:
    print("contain substring")
else:
    print("not contain substring")

# Take a string and capitalize the first letter of the string.
word="python"
print(word.capitalize())

