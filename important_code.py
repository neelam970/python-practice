# write a program for fibonacci series
# num=int(input("enetr num:"))
# n1,n2=0,1
# sum=0
# if num<0:
#     print("enter no greater than zero")
# else:
#     for i in range(0,num):
#         print(sum,end=" ")
#         n1=n2
#         n2=sum
#         sum=n1+n2

# # using functions
# def fibonacci(num):
#     n1=0
#     n2=1
#     if num<0:
#         return("enter no greater than zero")
#     else:
#         series=[]
#         for i in range(num):
#             series.append(n1)
#             sum=n1+n2
#             n1=n2
#             n2=sum
#         return series
#take user input
# num=int(input("enter num:")) 
# functiona call 
# result=fibonacci(num)
# print(result)

# write a program to find a prime no or not
# num=int(input("enter no."))
# if num<=1:
#     print("it is not a prime number")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("it is not a prime no")   
#             break   
#     else:
#             print("it is a prime no") 

# #using functions
# def prime(num):
#      if num<=1:
#           return("not prime") 
#      else:
#           for i in range(2,num):
#                if num%i==0:
#                     return "not prime no"
#                     break
#           else:
#                return("it is prime no")           
# # taking input
# num=int(input("enter num:"))
# # fuctiona call
# result=prime()
# print (result)

# find the factorial of a given no.
num=int(input("enter number:"))
fact=1
if num<0:
     print("print factorial of a number doesnot exist")
elif num==0:
     print("factorial of 0 is 1")
else:     
     for i in range(1,num+1):
           fact=fact*i
     print(fact)

# using functions
def factorial(num):
     fact=1
     if num<0:
          return "factorial of negative no doesnot exist"
     elif num==0:
          return 1
     else: 
          for i in range(1,num+1):
               fact=fact*i
          return fact     
# take input     
num=int(input("enter num:"))
# function call
result=factorial(num)
print(result)