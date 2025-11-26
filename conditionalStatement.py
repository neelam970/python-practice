# conditional statement
# if statement
age=int(input("age is:"))
if(age>=18):
    print("you can vote")

    # if else statement
    age=int(input("age is:"))
    if(age>=18):
        print("you can vote")
    else:
        print("you can not vote")

    # check if a no is positive or negative or zero
    num=int(input("num is:"))
    if(num>0):
       print("num is positive")
    elif(num<0):
       print ( "num is negative ")
    else:
       print("zero")

    #check no is od and even
    num=int(input("num is:"))
    if(num%2==0):
       print("even")
    else:
       print("odd")

    #    check a no is greater then 100 or not
    num=int(input("num is:"))
    if(num>=100):
       print("greater than 100")
    else:
       print("not greatrer then 100")
    
    #input two no and tell which one is greater
    num1=int(input("num1 is:"))
    num2=int(input("num2 is:"))
    if(num1>num2):
       print("num1 is greater")
    else:
       print("num2 is greater")

     # Take marks as input and print “Pass” if marks ≥ 33, otherwise “Fail”.
    marks=int(input("marks is:"))
    if(marks>=33):
       print("pass")
    else:
       print("fail")

    #Take 3 numbers and print the largest among them.
    a=int(input("a is:"))
    b=int(input("b is:"))
    c=int(input("c is:"))
    if(a>b and a>c):
       print("a is greater")
    elif(b>a and b>c):
       print("b is greater")
    else:
       print("c is greater")

    #Input a year and check if it is a leap year or not.
    year=int(input("year is:"))
    if(year%4==0 and year%400==0 or year%100!=0):
       print("leap year")
    else:
       print("not a leap year")
      
    #    '''Take temperature as input and print messages like:

    #    Above 30 → "It's hot!"

    #    Below 10 → "It's cold!"

    #    Otherwise → "Weather is normal.'''
    temp=int(input("temp is:"))
    if(temp>30):
       print("it is hot")
    elif(temp<10):
       print("it is cold")
    else:
       print("weather is normal")

    #Take a number and check if it is divisible by 5 and 11 both.
    num=int(input("num is:"))
    if(num%5==0 and num%11==0):
       print("yes it is divisible by 5 and 11 both")
    else:
       print("not divisible by 5 and 11 both")

    #Take a character input and check if it is a vowel or consonant.
    char=chr(input("char is:"))
    if(char=='a'or char=='e'or char=='i'or char=='o'or char=='u'or char=='A'or char=='E'or char=='I'or char=='O'or char=='U'):
       print("vowel")
    else:
       print("consonant")

    #second way
    char=input("char is:")
    if char in ('a','e','i','o','u','A','E','I','O','U'):
       print("vowel")
    else:
       print("consonant")

    #Take an integer and check if it is a three-digit number.
    num=int(input("num is:"))
    if(num>99 and num<1000):
        print("num is three digit no")
    else:
        print("num is not three digit no")

    # Take a password as input and print “Access Granted” if it matches your set password.
    password=input("password is:")
    if(password==1234):
        print("access granted")
    else:
        print("access denied")

    #Take your age and print:# < 13: “Child”# 13–19: “Teenager”# 20–59: “Adult”# 60+: “Senior Citizen”
    age=int(input("age is:"))
    if(age<13):
        print("child")
    elif(gae>=13 and age<=19):
        print("teenager")
    elif(age>=20 and age>=59):
        print("adult")
    else:
        print("senior citizen")

