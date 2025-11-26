# BASIC CLASS & OBJECT PRACTICE QUESTIONS (Without __init__())
#  Q1. Create a class named Car

# Task:

# Create a class called Car

# Add two attributes: brand and color

# Create one object and print both attributes
class Car:
    brand="Tata"
    color="red"

car1=Car()   
print(car1.brand)
print(car1.color)

# Create a class named Student

# Task:

# Add attributes: name and age

# Create two objects and print their data
class student:
    name="Neelam"
    age="23"

stdent1=student()   
print(stdent1.name)
print(stdent1.age)

# Q3. Create a class named Dog

# Task:

# Add an attribute breed

# Add a method bark() that prints “Dog is barking”

# Create an object and call the method
class Dog:
    breed="golden retrever"

    def bark(self):
        print("dog is barking")

dog1=Dog()
print(dog1.breed)        
dog1.bark()

# Q4. Create a class named Laptop

# Task:

# Add three attributes: brand, ram, price

# Add a method display() to show details

# Create one object and call the method
class Laptop:
    brand="hp"
    ram="260gb"
    price="120000"

    def display(self):
        print(self.brand)
        print(self.ram)
        print(self.price)       

laptop1=Laptop()
laptop1.display()    

# Q5. Create a class named Fruit

# Task:

# Add two attributes: name and color

# Add a method show() that prints both values

# Create two objects with different data
class Fruits:
    name=" "
    color=" "
    def show(self):
        print(self.name)
        print(self.color)

fruits1=Fruits()
fruits1.name="mango"       
fruits1.color="orange"  

fruits2=Fruits()
fruits2.name="apple"       
fruits2.color="red"  

fruits1.show()
fruits2.show()

# Q6. Create a class Pen

# Task:

# Add attributes brand and color

# Add a method write() that prints “Writing smoothly”

# Create an object and display both attributes and call method
class Pen:
    brand="cello"
    color="red"
    def write(self):
        print("writing smoothly")
p1=Pen()
print(p1.brand)
print(p1.color)
p1.write()     

# Q7. Create a class Mobile

# Task:

# Add attributes: brand, model

# Add method call() that prints “Calling…”

# Create object and call the method
class Mobile:
    brand="samsung"
    model="s21"
    def call(self):
        print("calling")
m1=Mobile()
print(m1.brand)
print(m1.model)
m1.call()   

# Create a class Laptop with brand, ram, and price using __init__().
class Laptop:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price

L1=Laptop("dell","16gb","300000")    
L2=Laptop("hp","24gb","400000") 

print(L1.brand,L1.ram,L1.price)
print(L2.brand,L2.ram,L2.price)

# Create a class Dog that takes name and breed as parameters and prints them.
class Dog:
    name="sizuu"
    breed="golden retriever"

d1=Dog()
print(d1.name)   
print(d1.breed) 

# Create a class Book that takes title and author, and has a method display() to print both.
class Book:
    title="fly high"
    author="chetan bhagat"
    def display(self,title,author):
        self.title=title
        self.author=author

b1=Book()    
b2=Book()
b3=Book()

b2.display("dream big","kaushal singh")
b3.display("think positive","narayanan")

print(b1.title,b1.author)
print(b2.title,b2.author)
print(b3.title,b3.author)

# Q1. Create a class Student

# Add a method set_details() to store name and marks.

# Add another method show_details() to print them.

# Create two objects and display their details.
class Student:
    def set_details(self,name,marks):
        self.name=name
        self.marks=marks

    def show_details(self):
        print("name:",self.name)    
        print("marks:",self.marks) 

# object creation        
s1=Student()  
s2=Student() 
# call method to set details
s1.set_details("neelam",99)     
s2.set_details("komal",94)     

# call method to display details
s1.show_details()
s2.show_details()

# Q2. Create a class Calculator

# Add a method add() that takes two numbers and prints their sum.

# Add another method multiply() that takes two numbers and prints their product.

# Create an object and call both methods.
class Calculator:
    def add(self,num1,num2):
          print("sum of number is:",num1+num2)   
    def mul(self,num1,num2):
          print("multiplication  of number is:",num1*num2)   
    
    # oblect creation
c1=Calculator()    


    #call a method to set data
c1.mul(6,2)
c1.add(2,3)

#    Create a class Pen

# Add attributes: brand and color.

# Add a method show() to print both attributes.

# Create two different objects with different data and display them.
class Pen:
    def show(self,brand,colour):
        print("brand of a pen is:",brand)
        print("colour of a pen is:",colour)

        #creating two objects
p1=Pen()
p2=Pen()


# call a method to diplay
p1.show("cello","blue")
p2.show("butterflow","red")

# Create a class BankAccount

# Add a method set_balance() to store account holder name and balance.

# Add another method deposit() to add money and show updated balance.

# Create one object and perform both actions.
class BankAccount:
    def set_balance(self,name,balance):
        print("account holder name is:",name)
        print("account balance is:",balance)
    def deposit(self,updated_balance):
        print("updated balance is:",updated_balance)    

        #creation of two objects
b1=BankAccount()        

#set data
b1.set_balance("neelam",45000)
b1.deposit(50000)


#  Q5. Create a class Rectangle

# Add a method set_dimensions() to store length and width.

# Add a method area() to calculate and print the area.

# Create an object and find the area.   
class Rectangle:
         def set_dimensions(self,length,width):
             self.length=length
             self.width=width
             
         def area_(self):
             print("area is:",self.length*self.width)    

r1=Rectangle()  

r1.set_dimensions(2,4)
r1.area_()

# create a student class that takes name and marks of three subjects as arguments in constructor then create a method to print the average
class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def get_avg(self):
        print("name is:",self.name)
        print("avg of three subjects are",(self.mark1+self.mark2+self.mark3)/3)

s1=Student("komal",99,44,76)
s1.get_avg()        
        