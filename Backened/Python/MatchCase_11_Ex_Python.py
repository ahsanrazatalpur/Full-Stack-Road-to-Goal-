
#Qno 1 
"""
day = int(input("Enter an integer :"))
match day:
    case 1 :
          if day == 1:
            print("Monday ")
    case 2:
        if day == 2:
            print("Tuesday")
    case 3:
        if day == 3:
            print("Wednesday")
    case 4:
        if day == 4:
            print("Thursday")
    case 5:
        if day == 5:
            print("Friday")
    case 6:
        if day == 6:
            print("Saturday")
    case 7:
        if day == 7:
            print("Sunday yaHOOOO!")
    case _:
        print("Invalid input")
#Qno 2 
print("***    SIMPLE CALCULAATOR   ***")
number1 = int(input("Enter first number :"))
number2 = int(input("Enter second number :"))
operation = input("Choose Operattion between(+,-,*,/,%) :")

match operation:
    case '+':
        print("Sum of two number is :",number1+number2)
    case '-':
        print("Difference of two number is :",number1-number2)
    case '*':
        print("The Multiplication of two numbers is :",number1*number2)
    case '/':
        print("The Division of two number is :",number1/number2)
    case '%':
        print("The Modulto of two number is :",number1%number2)
    case _:
        print("invalid operation")

#Qno 3 
season = int(input("Enter the season number :"))
match season:
    case 1 | 2 | 12:
        print("Winter")
    case 3 | 4 | 5:
        print("Spring")
    case 6 | 7 | 8:
        print("Summer")
    case 9 | 10 | 11:
        print("Fall")
    case _:
        print("Invalid season")
        
# Qno 4
light = input("Enter Light color :")
match light:
    case 'red':
        print("Stop")
    case 'yellow':
        print("Get ready")
    case 'green':
        print("Go ! yohoooooooOO")
    case _:
        print("Invalid color")
grade = input("Enter your grade :")
match grade:
    case 'a':
        print("Exellent")
    case ''b':
        print("Good Job!")
    case 'c':
        print("You passed")
    case 'd':
        print("Need important")
    case 'd':
        print("very poor")
    case 'f':
        print("Failed")
    case _:
        print("invalid grade")
        
#Qnoo 5
print("***   Welcome too translator   ***") 
word = input("Enter a English word to transle in Urdu :\n")

match word:
    case 'hi' | 'HI':
        print("Aslam O alekum ")
    case 'bye':
        print("Allah Hafiz")
    case 'thanks' |'THANKS':
        print("apka shukriya")
    case 'yes' | 'YES':
        print("Ji haan")
    case 'no' |'NO':
        print("Ji nahin")
    case _:
        print("invalid word")
#qno 6
        alpha = input("Enter a Alphabet to check :")
for char in alpha:
 match alpha:
    case 'a' | 'e' | 'i' | 'o' |'u' |'A' |'E' |'I' | 'O' | 'U':
        print(f"{alpha} in Vowel ")
    case _:
        print("Alphabet is constant")
#Qno 7
number = [1, 0, 5, 20]
for num in number:
 match num:
    case 0:
     print("number is zero")
    case 1:
      if num > 0:
        print("number is positive ")
    case _:
     print("number is negative")

#qno 8
alpha = input("Enter any alphabet ")
match alpha:
    case 0:
        if alpha >= 65 | alpha <= 90:
            print("Alphabet is upperase")
    case 1:
        if alpha >= 97 | alpha<= 122:
            print("alphabet is Lower case")
    case _:
        print("Invalid number")
#qno 9
username = input("enter username: ")
password = int(input("enter pass: "))

match username, password:
    case("ahsan" ,  123):
            print("Login succesfull")
    case ("ahsan" ,  _):
            print("invallid  password")
    case (_ ,  123):
         print("username is Invvalid")
    
#         """
# month = int(input("enter birth month : "))-----------------
# day = int(input("enter birth day : "))

# match month,day:
#     case(3  , 5 ):
#         if  month >= 3 | <= 4 , day >1 | <=30:
#          print("Aries")
    


        
    