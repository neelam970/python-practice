# Python Basics

# Write a Python program to print your name, course, and hobby.
name="Neelam"
course="MCA"
Hobby="Painting"
print(name)
print(course)
print(Hobby)

# Create variables of all data types (int, float, str, bool, complex) and print their types using type().
a=3
b=3.4
c="Neelam"
d= 2+3J
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Show an example of dynamic typing — assign an integer to a variable, then assign a string to the same variable and print both.
x=3
x="hello"
print(x)
# Demonstrate variable naming rules with valid and invalid examples (comment the invalid ones).
# valid one
# name1="neelam"
# invalid one
# 1name="neelam"
# Write a program that displays the memory address (id) of a variable.
s=203
print(id(s))

# Use the keyword module to display all Python keywords.
import keyword
print(keyword.kwlist)

# Show an example of token types — identifier, keyword, literal, operator, and punctuation — in one line of code.
a=3
# a is identifier and 3 is a literal
b=2+3
# b is identifier and + is a operator
# e="{}" it is punctuator
# if is a keyword
# Create a simple statement and explain which parts are identifiers, literals, or operators.
a=2+3
# a is an identifier 2 and 3 are literals and + is an operator
# Convert integer to float and float to integer using type casting.
a=3
b=3.5
print(float(a))
print(int(b))
# Demonstrate multiple assignment in a single line (e.g., a = b = c = 5 and x, y, z = 1, 2, 3).
a=b=3
x,y,z=1,2,3
# Explain importance and limitations of Python in short (comment lines in your code file).
# importance
# python is open source, easy to read and write,huge standard library,used to make websites ,used in datascience ,data automation,al an ml,python is portable
# limitations
# slow execution speed,takes large memory space,not ideal for mobile/android app development, weak in multithrea
# Write a small comment block describing what Python tokens are and give 2 examples of each category.
# tokens in python are a small building block or we can say that basic element of python program and each word or symbol is a token in a python program
# in simple language tokens are alphabets of python code eveything we write is made up of tokens
# there are 5 types of tokens identifers keywords punctuators operators literals
# example 2+2,name123="neelam",eilf,{}

#Topic 2 – Operators & Expressions

# Create variables a = 10, b = 3 and display results for:
a=10
b=3
# Addition
print(a+b)
# Subtraction
print(a-b)
# Multiplication
print(a*b)
# Division
print(a/b)
# Floor Division
print(a//b)
# Modulus
print(a%b)
# Exponentiation
print(a**b)

# Demonstrate the difference between / and // division.
# / is a normal division and it gives decimals result also but // floor division does not gives decimal number it only gives whole number as a result

# Write an expression that mixes operators: 10 + 3 * 2 ** 2 — print and explain the output (operator precedence).
a=10+3*2**2
print(a)
# Show how to use assignment operators like +=, -=, *=, /=, etc.
a=5
a+=3
a-=2
a*=7
a/=2
a//=2
a%=2
a**=2
print(a)


# Demonstrate relational operators (==, !=, >, <, >=, <=) on two numbers and print results.
a=3
b=9
print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
# Show how logical operators (and, or, not) work using True/False variables.
a=3
b=5
print((a>b)and(a<b))
print((b>a)or(b<a))
print(not(a<b) )
# Demonstrate identity operators (is, is not) with two lists having same elements but different IDs.
x=[20,10,30]
z=[20,10,30]
x=y
print(x is y)
print(x is z)
print(x is not z)
# Demonstrate membership operators (in, not in) with a list of numbers.
a=(10,20,30)
print(40 in a)
print(10 not in a)
print(20 in a)

# Create a mathematical expression using multiple operators and parentheses, then explain which executes first.
a=2+3*(8-4)**2/2
print(a)
# Write an expression to calculate the area of a circle using only arithmetic operators and constants (π = 3.14).
radius=2
print(3.14*radius*radius)
# Demonstrate the concept of operator precedence with at least three examples and their outputs.
a=2+3*5
b=3-4/2
c=3//2**2
print(a)
print(b)
print(c)
# Create an expression that uses both arithmetic and logical operators together (for example: (a + b) > (c * 2) and a != b).
a=2
b=4
x=3
y=6
print("result is",(a+b)>(x*y)and(a-b)>(x/y))
# Write a single line expression that assigns value to a variable based on another variable using = and +=.
a=5
b=a
b+=3
print(a,b)
# Combine arithmetic and assignment operators together — for example:
# Explain what happens step-by-step.
# x = 5
# x += 3 * 2
# print(x)
# varible x assgn a value 5 and in the second line x+3*2 will get answer 11 because precedence of multiplication is high then addition then print the resulut using print fuction
