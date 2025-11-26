# Q1. Single Inheritance

# Task:
# Create a class Vehicle with a method show_vehicle() that prints “This is a vehicle.”
# Then create a child class Car that inherits from Vehicle and has its own method show_car() that prints “This is a car.”
# Create an object of Car and call both methods.
class Vehicle:
    def show_vehicle(self):
        print("this is a vehicle")
class car(Vehicle):
    def show_car(self):
        print("this is a car")      
obj=car()
obj.show_car()
obj.show_vehicle()

# Q2. Multilevel Inheritance

# Task:
# Create three classes — Grandparent, Parent, and Child.
# Each should have one method that prints its class name.
# Create an object of Child and call all three methods.
class grandparent:
    def show_grandparent(self):
        print("this is grandparent class")
class parent(grandparent):
    def show_parent(self):
        print("this is a parent class")   
class child(parent):
    def show_child(self):
        print("this is a child class")    
obj=child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()    

# Q3. Multiple Inheritance

# Task:
# Create two parent classes:

# Teacher with method teach(),

# Student with method study().

# Then create a class Tutor that inherits from both Teacher and Student and adds method guide().
# Create an object of Tutor and call all methods.

class Teacher:
    def teaches(self):
        print("teaching students")
class Student:
    def study(self):
        print("studying lessons")
class Tutor(Teacher,Student):
    def guide(self):
        print("guiding students")   
obj=Tutor()
obj.teaches()
obj.study()
obj.guide()    

# Q4. Hierarchical Inheritance

# Task:
# Create a base class Animal with a method sound().
# Then create two derived classes — Dog and Cat.
# Each should have its own method (bark() and meow() respectively).
# Create objects for both classes and call their methods.
class Animal:
    def sound(self):
        print("animals are making different sounds")
class dog(Animal):
    def bark(self):
        print("dog barks")      
class cat(Animal):
    def meow(self):
        print("cat meow")
A1=dog()
A2=cat()
A3=Animal()
A3.sound()
A1.bark()
A3.sound()
A2.meow()   

# Q5. Hybrid Inheritance

# Task:
# Create these classes:

# Class A → method showA()

# Class B(A) → method showB()

# Class C(A) → method showC()

# Class D(B, C) → method showD()

# Create an object of D and call all methods.
class A:
    def showA(self):
        print("this is class A")
class B(A):
    def showB(self):
        print("this is class B")
class C(A):
    def showC(self):
        print("this is class C")      
class D(B, C):
    def showD(self):
        print("this is class D")    
ob=D()
ob.showA()  
ob.showB()  
ob.showC()  
ob.showD()              
