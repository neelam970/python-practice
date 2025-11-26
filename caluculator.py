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



    
     