# f=open("neelam.txt","w")
# f.write("hello!,I am Neelam.\n")
# f.write("I am a kind person")
# f.close()

# f=open("neelam.txt","r")
# content= f.read()
# print(content)
# f.close()

# f=open("neelam.txt","r")
# for line in f:
#     print(line.strip())
# f.close()    

# f=open("neelam.txt","r")
# line=f.readline()
# print(line)
# f.close()    

# f=open("neelam.txt","r")
# linee=f.readlines()
# print(linee)
# f.close()    

# f=open("neelam.txt","a")
# f.write("\nI am very respectful person")
# f.close()

# f=open("neelam.txt","r")
# content1=f.read()
# print(content1)
# f.close()

# with  open("neelam.txt","r") as f:
#     line=f.readline()
#     print(line)

# # Create a file and write your name and hobby in it.
# f=open("manish.txt","w")
# f.write("Hello!,I am Neelam," " ")
# f.write("my hobby is painting.")
# f.close()

# # Read and print the content of the same file.
# f=open("manish.txt","r")
# content=f.read()
# print(content)
# f.close()

# # Append “I love Python” to the same file.
# f=open("manish.txt","a")
# f.write("" " I love python")
# f.close()

# # Read and print the content of the same file.
# f=open("manish.txt","r")
# content=f.read()
# print(content)
# f.close()

# # Read and print all lines separately.
# f=open("manish.txt","r")
# for line in f:
#     print(line)
# f.close()

# # Count how many lines are in the file.
# f=open("manish.txt","r")
# lines=f.readlines()
# print(len(lines))
# f.close()

# BASIC LEVEL (Fundamentals)

# These test your understanding of file opening, reading, and closing.

# Create a text file named info.txt containing:

# Hello, my name is Neelam.
# I love painting.
# Python is my favorite language.
f=open("info.txt","w")
f.write("Hello, my name is Neelam.\n")
f.write("I love painting.\n")
f.write("Python is my favorite language.")
f.close()

# Write a Python program to read and display the content of the file.
f=open("info.txt","r")
content=f.read()
print(content)
f.close()
# Write a program to read only the first 10 characters of info.txt.
f=open("info.txt","r")
content=f.read(10)
print(content)
f.close()

# Write a program to read and print the first line of the file using readline().
f=open("info.txt","r")
content=f.readline()
print(content)
f.close()


# Write a program to read all lines using readlines() and display them one by one.
f=open("info.txt","r")
content=f.readlines()
print(content)
f.close()


# Count and print the number of lines present in the file.
f=open("info.txt","r")
content=f.readlines()
print(len(content))
f.close()
# Read and print each line with its line number (like “Line 1: …”).
f=open("info.txt","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)

# intermidiate level
# Write a program to count the total number of words in a file.
f=open("info.txt","r")
content=f.read()
words=content.split()
print(len(words))
f.close()



# Write a program to count how many times the word “Python” appears in the file.
f=open("info.txt","r")
content=f.read()
count=content.count("Python")
print(count)
f.close()

# Write a program to read a file and convert its content to uppercase while displaying.
f=open("info.txt","r")
content=f.read()
print(content.upper())
f.close()

# Read the file and print only those lines that contain the word “love”.
f=open("info.txt","r")
for line in f:
    if "love" in line:
        print(line)
f.close()        
# Write a program that reads a file and prints the longest line.
f=open("info.txt","r")
longest_line=""
for line in f:
    if len(line)>len(longest_line):
      longest_line=line
print(longest_line)
f.close()
# Read all lines of a file and store them into a list (without using readlines()).
list=[]
f=open("info.txt","r")
for line in f:
    list.append(line)
print(list)
f.close()

f=open("info.txt","wb")
f.write(b"hello friends")
f.close()

f=open("info.txt","rb")
data=f.read()
print(data)
f.close()

f=open("info.txt","ab")
f.write(b"i am neelam") 
f.close()

f=open("info.txt","rb")
data=f.read()
print(data)
f.close()

f=open("info.txt","r+b")
data=f.read()
print(data)
f.seek(0)
f.write(b"i am love")
f.close()

f=open("info.txt","rb")
data=f.read()
print(data)
f.close()

f=open("info.txt","w+b")
f.write(b"my name is riya")
f.seek(0)
print(f.read())
f.close()

f=open("info.txt","a+b")
f.write(b"sorry my name is rohilaa")
f.seek(0)
print(f.read())
f.close()