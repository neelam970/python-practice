# Write a program to print numbers from 1 to 20, but stop printing when you reach a number greater than 12. (Use break)
for i in range(1,21):
    if(i>12):
     break
    print(i)

# Print numbers from 1 to 15, but skip numbers divisible by 3.
for i in range(1,16):
   if(i%3==0):  
      continue
   print(i) 

# Take numbers as input from the user until they enter a negative number. Print all entered numbers. (Use break)
while True:
   num=int(input("enter a number:"))
   if(num<0):
    break
   print(num)

#Print the first 5 even numbers starting from 1. Stop after printing the fifth even number. (Use break)
count=0
for i in range(2,100,2):
   if(i%2==0):
    print(i)
    count+=1
    if count==5:
       break
# Take a list of numbers and print all numbers until you encounter the first number greater than 50. (Use break)
num=[1,23,4,12,31,55,6,23] 
for i in num:
   if(i>51):
    print("greater than 50 no is found",i)
    break
   print(i)

#  From a list of numbers, print all numbers except those that are multiples of 4. (Use continue
num=[1,2,3,4,5,6,7,8,9,10]   
for i in num:
  if(i%4==0):
    continue
  print(i) 

# Take a string input from the user and print each character until you encounter the letter 'x'. (Use break)
word=input("enter a string:")
for i in word:
  if(i=='x'):
   print("x is found",i)
   break
  print(i)

# Print numbers from 1 to 50, skip all numbers divisible by 7, and print the rest. (Use continue)
for i in range(1,51):
  if(i%7==0):
    continue
  print(i)  



