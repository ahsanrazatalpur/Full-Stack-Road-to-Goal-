# Arguement in Function

def Average(a , b): #here a , b are required arguement
# Average(a = 5 , b = 7): #here a , b are default arguement
    print("The average of two number is",(a+b)/2)

Average(4 ,6)
print("----------------------------------------------------------------------")

#There are four types of arguements in function in python
 # 1. Default Arguement
 # 2. Keyword Arguement
 # 3. Variaable Arguement
 # 4. Required Arguement
 

 # Here is twist if we pass two arguement default and required args so required will be prefer
def Average1(a = 5 , b = 7): #here a , b are default arguement   # ignored
    print("The average of two number is",(a+b)/2)

Average1(4 ,6)# prefrered
print("----------------------------------------------------------------------")

# another twist if we give requireed areguement one value a and  both value a and b in default arguemenet so the
# a will be taken from required arguement and b is taken from default 
def Average3(a = 5 , b = 7): #here a , b are default arguement
    print("The average of two number is",(a+b)/2)

Average3(4) # only a is defined so b will be taken from top default argurment 

print("----------------------------------------------------------------------")
# another example of giving one value in required argurment

def Bio(name = "Ali Raza",fname = "Amir ALi", cast = "Talpur"):# name will be taken as required argur=ement below
    print("Name :",name )
    print("FName :",fname )
    print("Caste :",cast )

Bio("Ahsan Raza")

print("----------------------------------------------------------------------")

#Keyword argument (if we want we does not want order)

def avg(a = 5, b = 9):
    print("The Average of",a, "and", b ," is :",(a+b)/2)

avg(b = 3, a = 8) # we doesnot follow the order the keyword args is nothing but we just pass args as any randomn order

print("----------------------------------------------------------------------")

# Required Arguement(nothing but just give the value  in the require args below)

def sum(a,b):
    print("The Sum is :",a+b)
sum(3,5) # required args nothing but just give the value of variable here below 

print("----------------------------------------------------------------------")

def avgg(*number):# number as i wish 
     sum = 0
     for i in number:
       sum = sum + i
     print("The avg of is: ",sum/len(number))
avgg(1,2,4,6)
