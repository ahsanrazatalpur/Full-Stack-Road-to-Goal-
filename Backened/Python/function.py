# Function in Python 
# piece of code that can be reused
# help to repeat our code rather than typing multiple line or changing easy bs have to change only in one line 

# a  = 10
# b = 20
# gmean = (a*b)/(a+b)
# print(gmean)

def CalculateGmean(a , b):
    mean = (a*b)/(a+b)
    print(mean)
CalculateGmean(10,20)
CalculateGmean(5,10)

a = 10
b = 20

def isGreater(a,b):
    if(a > b):
        print("First number is greater")
    else:
        print("Second number is greater")

isGreater(10,20)
isGreater(9,7)
isGreater(7,80)
isGreater(1,2)
