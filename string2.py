# Take a string from the user and print its length.
name=input("enter your name:")
print("length of your string is:",len(name))

# Take a string and print the first and last character.
name=input("enter a string:")
print(name[0],name[-1])

# Take a string and print all characters using slicing.
name=input("enter a string:")
print(name[:])

# Reverse a string using slicing.
name=input("enter a string:")
print("reverse os a string is:",name[::-1])


# Check whether the given string is palindrome or not.
name=input("enter a string:")
reverse=name[::-1]
if(name==reverse):
    print("it is a palindrome")
else:
    print("it is not a palindrome")

# Convert a string into uppercase and lowercase.
name=input("enter a string:")
print("string in upper case:",name.upper())
print("string in lower case:",name.lower())
# Count how many vowels are in the string.
name=input("enter a string:")
vowels="aeiouAEIOU"
count=0
for char in name:
    if char in vowels:
        count+=1

print("no of vowels:",count)
# Count how many consonants are in the string.
name=input("enter a string:")
vowels="aeiouAEIOU"
count=0
for char in name:
    if char.isalpha()and char not in vowels:
        count+=1
        
print("no of consonants are:",count)

# Count how many alphabets, digits, and special characters are in a string.
name=input("enter a string:")
alpha = digit = special = 0

for char in name:
    if char.isalpha():
        alpha += 1
    elif char.isdigit():
        digit += 1
    else:
        special += 1

print("alphabets:", alpha)
print("digits:", digit)
print("special characters:", special)


# Replace spaces with underscores.  
name=input("enter a string:")
print(name.replace(" ","_"))

# Remove leading and trailing spaces using strip().
name=input("enter a string:")
print(name.strip())


# Take a sentence and print the number of words.
name="python is a high-level,and python is interpreted language"
words=name.split()
print(len(words))

# Check whether a given character exists in a string using in.
name="neelam"
print("e"in name)

# Concatenate two strings without using +
str1="neelam"
str2="kumari"
str_concat="{}{}".format(str1,str2)
print(str_concat)