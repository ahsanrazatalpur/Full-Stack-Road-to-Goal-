# Qno 1 
def greet(name):
    print('Hello,',name)
greet("Mehdi")

print("----------------------------------------------------------------")
# Qno 2

def sumOftwo(a,b):
    print(a + b)

sumOftwo(20,30)

print("----------------------------------------------------------------")
print("----------------------------------------------------------------")

#qno 3 
def EvenOdd(num):
    if num % 2== 0:
        print("number is Even")
    else:
        print("number is Odd")

EvenOdd(19)

print("----------------------------------------------------------------")
#qno 4
def primeChecker(num):
    for i in range (2,num):
     if num % i == 0:
        print("Not Prime number")
        break
    else:
        print("Prime number")

primeChecker(19)