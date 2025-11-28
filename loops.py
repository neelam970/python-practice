# Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

# Print all even numbers between 1 and 20.
for i in range(2,21,2):
    print("even no are:",i)

# Print all odd numbers between 1 and 20.
for i in range(1,21,2):
    print("odd no are:",i)

# Print the multiplication table of a given number (take input from the user).
number=int(input("enter a number:"))
for i in range(1,11):
    print(number ,'*',i ,'=', number*i)

# Print all elements of a list using a for loop.
lists=['apple','banana','kiwi']
for list in lists:
    print(list)

# Print each character of a string on a new line.
word="Neelam"
for word1 in word:
    print(word1)  

# Print numbers from 10 to 1 in reverse order.      
number=[1,2,3,4,5,6,7,8,9,10]
for number in range(10,0,-1):
    print(number)

# Print your name 5 times.
for i in range(1,6):
    print("Neelam")

# Print the square of numbers from 1 to 10.
for i in range(1,11):
    print(i,"square is",i*i)

# Print a pattern like this:
# *
# * *
# * * *
# * * * *
for i in range(1,5):
    print("*"*i)

# Print all numbers between 1 and 100 that are divisible by 5.
for i in range(1,101):
    if(i%5==0):
        print(i)

# Count how many even numbers are between 1 and 50.
for i in range(2,51,2):
    print(i)       

# Print the cube of numbers from 1 to 5.
for i in range(1,6):
    print(i,"cube is",i*i*i)

# Print the sum of all even numbers between 1 and 20.
total=0
for i in range(2,21,2):
    total=total+i
print(total)    

# Print all characters of a string except spaces.
word="Neelam"
for word1 in word:
    print(word1)

# Print the numbers from 1 to 10 using a while loop.
count=1
while(count<=10):
    print(count)  
    count+=1

# Print all elements of a list in reverse order using a for loop.
list1=['apple','banana','kiwi']
for i in reversed (list1):
    print(i)

# Take 5 numbers from the user and print their total.
num1=int(input("enter num1:"))
num2=int(input("enter num2 :"))
num3=int(input("enter num3 :"))
print(num1+num2+num3)  

# Take 5 numbers from the user and print their total by using loop
total=0
for i in range(5):
    num=int(input("enter a number:"))
    total=total+num
print(total)    

# Print numbers from 1 to 30, but skip those divisible by 3.
for i in range(1,31):
    if(i%3!=0):
      print(i)

# write a progam to reversed a string
word="Neelam"
for i in reversed(word):
  print(i)


  
# Print numbers from 1 to 20.

# 2️⃣ Print even numbers between 1 and 50.
# 3️⃣ Print odd numbers between 1 and 50.
# 4️⃣ Print the multiplication table of a given number.
# 5️⃣ Print the sum of first n natural numbers.
# 6️⃣ Count the number of digits in a given number.
# 7️⃣ Reverse a given number using loops.
# 8️⃣ Find the factorial of a given number.
# 9️⃣ Find the sum of digits of a given number.
# 🔟 Print Fibonacci series up to n terms (no nested loop needed).