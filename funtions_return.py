# square of a numbers
# def square(a):
#      return a*a
    
# # fuction call
# num=square(2)
# print(num)
# print(type(num))

# perimeter of a rectangle
# def peri_of_rec(l,b):
#      return (l*b)
# # func call
# l=int(input("enter length:"))
# b=int(input("enter breadth:"))
# result=peri_of_rec(l,b)
# print(result)

# # area of a square
# def area_of_squ(side):
#      return side*side
# # func call
# side=int(input("enter side:"))
# result=area_of_squ(side)
# print(result)

# # area of circle
# def area_of_circle(r):
#      area = 3.14*r*r
#      return area
# # func call
# r=int(input("enter radius:"))
# result=area_of_circle(r)
# print(result)
     
# sum of two numbers
# def sumof2nums(a,b):
#      return a+b
# # fun call
# a=int(input("enter a:"))
# b=int(input("enetr b:"))
# result=sumof2nums(a,b)
# print(result)

# even or odd
# def even_odd(a):
#      if(a%2==0):
#           return('even')
#      else:
#           return('odd')
# #fun call
# a=int(input("enter a:"))
# result=even_odd(a)
# print(result)


# make a calculator in which u are doing addition , multiplication, division,subtraction,average
def addition(a,b,op):
     if op=="+":
         return a+b
def substraction(a,b,op):
     if op=="-":
         return a-b
def multiplication(a,b,op):
     if op=="*":
         return a*b
def division(a,b,op):
     if op=="/":
          if b==0:
               return "zero division error"
          else:
               return a/b
def average(a,b,op):
     if op == "avg":
          return a+b/2
     
def power(a,op):
     if op=="pow":
          return a*a  

def modulus(a,b,op):
     if op =="mod":
          return a%b   

def percentage(a,b,op):
     if op =="%":
          return (a*b)/100      


#take input from user
a=int(input("enetr a:")) 
op=input("enter operator :") 
b=int(input("enetr b:"))

#function call
result=None
result=addition(a,b,op)or substraction(a,b,op)or multiplication(a,b,op)or division(a,b,op)or average(a,b,op)or power(a,op)or modulus(a,b,op) or percentage(a,b,op)

#print 
print(result)



    
     