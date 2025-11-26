# Recursion Practice Questions
# Level 1: Basics

# Write a recursive function to print numbers from 1 to N.

def count(n):
    if(n==10):
        print("end")
    else:
        print(n)
        count(n+1)
count(1)        

# Write a recursive function to print numbers from N to 1.
def count(n):
    if(n==0):
        print("end")
    else:
        print(n)
        count(n-1)
count(9) 

# Write a recursive function to print “Hello” N times.
def greet():
    print("hello")
    greet()    


# Write a recursive function to find the sum of first N natural numbers.
def add(n):
    if(n==0):
        return 1
    else:
        return n+(n-1)
add(8)
# Write a recursive function to find the factorial of a number.

# Write a recursive function to find the sum of digits of a number.