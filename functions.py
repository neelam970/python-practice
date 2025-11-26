# Write a function that prints “Hello World”.
# function definition
def greet():
    print("hello world!")

    # function call
greet()    
greet() 
greet() 

# Write a function that prints your name.
def name():
    print("neelam")

name()  
name()  
name()  

# Write a function that prints any 3 lines (like “Good morning”, “How are you?”, “Have a nice day!”).
def wish():
    print("Good Morning")
    print("how are u")
    print("have a nice day")

wish() 

# Write a function that adds two numbers and prints the sum.
def add():
    a=2
    b=3
    sum=a+b
    print(sum)

add()  

# Write a function that subtracts two numbers and prints the result.
def sub():
    a=4
    b=2
    sub=a-b
    print(sub)

sub() 


# Write a function that prints the square of a given number.
def square():
    num=int(input("enetr a number"))
    print("square of a no.",num*num)

square()    

# Write a function that prints numbers from 1 to 10.
def num():
    for i in range(1,11):
     print(i)

num()     
num()    

# Write a function that prints the table of a given number (like 2, 3, 4…).
def table():
 num=int(input("enter a num"))
 for i in range(1,11):
    print(num ,"*", i ,"=",num*i)

table() 

# Write a function that prints your college name and course name.
def student():
   print("cgc landran,mohali")
   print("MCA")

student()   


# Write a function that prints whether a number is even or odd.
def evod():
    num=int(input("enter a num:"))
    if(num%2==0):
       print("even no")
    else:
       print("odd")

evod()  

# 🌿 LEVEL 2: Functions with Inputs (Parameters)

# (You’ll learn how to send values into a function)

# Write a function that takes a name and prints “Hello, name!”.
def nam(name):
   print("hello",name)

nam("Neelam")   

# Write a function that takes two numbers and prints their sum.
def num(num1,num2):
    # num1=int(input("enter num:"))
    # num2=int(input("enter num:"))
    sum=(num1+num2)
    print("sum is:",sum)

num(2,3) 
num(6,7)
num(9,9)   

# Write a function that takes one number and prints its square.
def squ(num):
   print("square of num is:",num*num)

squ(3)   
squ(4)   
squ(6)   
squ(7)   

# Write a function that takes a number and prints if it is positive, negative, or zero.
def number(num):
   if(num<0):
      print("negative no")
   elif(num>0):
      print("positive no")
   else:
      print("zero")

number(4)
number(-1)      
number(0)      
number(8)

# Write a function that takes two numbers and prints the greater one.
def grt(num1,num2):
   if(num1>num2):
      print("num1 is greater")
   else:
      print("num2 is greater")

grt(3,7)    
grt(9,7)      
grt(1,7)    

# Write a function that takes three numbers and prints the smallest.
def small(num1,num2,num3):
   if((num1<num2)and(num1<num3)):
      print("num1 is smallest")
   elif((num2<num1)and(num2<num3)):
      print("num2 is smallest")
   else:
      print("num3 is smallest")

small(2,1,5)      
small(0,-1,9)      
small(22,9,500)  

# another way to do this is
def smal(num1,num2,num3):
   smallest=min(num1,num2,num3)
   print("smallest no is:",smallest)

smal(2,1,4)   
smal(2,100,44)   


# Write a function that takes marks and prints if the student is Pass or Fail.
def score(marks):
   if(marks>=50):
      print("pass")
   else:
      print("fail")

score(66)      
score(6)      
score(22)      

# Write a function that takes age and prints if the person can vote or not.
def vote(age):
   if(age>=18):
      print("u can vote")
   else:
      print("u cannot vote")

vote(12)
vote(18)
vote(88)

# Write a function that takes a number and prints if it’s divisible by 5.
def div(num):
   if(num%5==0):
      print("it is divisible by 5")
   else:
      print("it is not divisible by 5")

div(44)
div(95)

# Write a function that takes a number n and prints all numbers from 1 to n.
def numb(n):
   for i in range(1,n+1):
      print(i)
numb(9)
numb(11)
numb(23)

# LEVEL 3: Functions that Return a Value

# (You’ll learn return keyword now)

# Write a function that returns the sum of two numbers.
def addd(a,b):
   return a+b
   
result=addd(3,4)
print("result is:",result)

# Write a function that returns the square of a number.
def sqrt(num):
   return num*num
number=int(input("enetr a number"))
square=sqrt(number)
print("square of no is:",square)
print(square*2)


# Write a function that returns the area of a rectangle (length × width).
def rect(l,b):
   return l*b
length=int(input("enter length"))
breadth=int(input("enter breadth"))
area=rect(length,breadth)
print("area of rectangle:",area)
print("double of area",area*2)


# Write a function that returns the average of three numbers.
def avg(num1,num2,num3):
   return num1+num2+num3/3
number1=int(input("enter num1"))
number2=int(input("enter num2"))
number3=int(input("enter num3"))
average=avg(number1,number2,number3)
print("average is:",average)

# Write a function that returns True if a number is even, otherwise False.
def numer(num):
   return num%2==0
number=int(input("enter a number"))
result=numer(number)
print(result)
      

# Write a function that returns the area of a circle (πr²).
import math
def circle(r):
   return math.pi*r*r
radius=int(input("enetr a number"))
area=circle(radius)
print("area of circle:",area)

# Write a function that returns the maximum of two numbers.
def maxi(num1,num2):
   return max(num1,num2)
number1=int(input("enetr num1"))
number2=int(input("enetr num2"))
result=maxi(number1,number2)
print(result)

# Write a function that returns the factorial of a number.
def fact(num):
    factorial=1
    for i in range(1,num+1):
     factorial=factorial*i
    return factorial

number=int(input("enetr a number"))
result=fact(number)
print(result)

# Write a function that returns the sum of first n natural numbers.
def natural(n):
   return n*(n+1)//2
n1=int(input("enter n"))
result=natural(n1)
print(result)


# Write a function that returns the square root of a number.
import math
def square(num):
   return math.sqrt(num)
number=int(input("enetr a number"))
result=square(number)
print(result)