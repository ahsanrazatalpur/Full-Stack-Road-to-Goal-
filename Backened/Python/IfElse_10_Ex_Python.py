"""
#Qno 1 
number = int(input("Enter an inetger :"))
if(number %2 == 0):
    print("Number is Even ")
else:
    print("Number is Odd")

#QNo 2
number = int(input("enter an number: "))
if(number > 0):
    print("Number is positive")
elif(number < 0):
    print("Number is Negative ")
else:
    print("Number is zero")

#QNo 3
year = int(input("Enter a year: "))
if(year %4 == 0) and (year % 400 == 0 or year % 100 != 0):
    print(year,"is a Leap year")
else:
    print(year,"It is not a leap year")

#QNo 4
marks = int(input("Please enter your marks :"))
if (marks >= 90):
    print("YOOOHOOOOO   ! You Got , A+ Grade")
elif(marks >= 80) and (marks <=89):
    print("congratulation ,You Got A Garde ")
elif(marks >=70) and (marks <= 79):
    print("Good, You Got B Grade")
else:
    print("Fail, Try Again")

#QNo 5
num1 = 5
num2 = 8
num3 = 10

if(num1 >num2 and num3):
    print("Num1 Is greater")
elif(num2 > num3 and num1):
    print("Num2 Is greater ")
else:
    print("Num3 is Greater")
#QNo 6
username = input("Enter your username: ")
password = input("Enter your password: ")

if(username == "ahsanraza"):
    if(password == "ahsan123"):
        print("Acces Granted  permision") # if both condition true
    else:
        print("Password is incorect ") # if only 1st conditon true
else:
    print("username is invalid ") # if only 2nd condition true
"""
#Qno 7
age = int(input("Enter your age: "))
if(age < 13):
    print("You Kid ")
elif(age > 13 and age <19):
    print("You are  Teen ")
else:
    print("You are a Adut")

