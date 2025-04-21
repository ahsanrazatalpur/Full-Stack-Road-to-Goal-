# conditional statment (decision making   3 types)
# print one statement if or else at a time
"""
>
1. <
2. >=
3. <=
4. ==
5. !=
6. if else
7. elif
8. else
age  = int(input("Enter your age : "))
print("Your Age is :",age) 

print(age >  18) # Boolean type retrurn
print(age <  18) # Boolean type retrurn
print(age >=  18) # Boolean type retrurn
print(age <=  18) # Boolean type retrurn
print(age ==  18) # Boolean type retrurn
print(age !=  18) # Boolean type retrurn


if (age >= 18): # Take conditional operator
    print("You can drive :)")  # we give indentation (space) due to python syntax 
else:
    print("You can't drive :(")
print("This line is out of loop ok :)") # this line is out of loop

#elif

apple = 210
budget = 250

if(budget - apple > 200):
     print("Aelxa, Add apple to the cart")
elif(budget - apple <50):
     print("budget is   good")
else:
    print("Budget is not good ")
    print("Alexa, Don't add apple to the cart")

number  =int(input('Please enter the integer number : '))
if (number > 0):
    print('Number is Positive')
elif(number < 0):
    print("Number is Negative ")
else:
    print("Number is Zero ")
print("Im Happy now :) ")
"""
# Nested  if else
number = int(input("Enter any number : "))
if(number > 0):
    print("Number is non-zero")
    if(number <=10):
        print("Number is between  0 to 10")

    else:
        print("Number is greater than 10")

else:
    print("Number is zero")
