"""
#Qno 1
name = input("Please Enter your name : ")
print("Hello,",name,"Nice to meet you.")
# Qno 2 
name  = "Ahsan Raza"
print(len(name))
# Qno 3
name  = "Ahsan Raza Talpur"
print(name[::-1])
#qno 4
name  = "Ahsan Raza Talpur"
a = name.find('a')
print("a =",a)
e = name.find('e')
print("e =",e)
i = name.find('i')
print("i =",i)
o = name.find('o')
print("o =",o)
u = name.find('u')
print("u =",u)
#Qno 5
word = 'tibit'
if word[::-1] == word:
    print("Is Palindrome")
else:
    print("Not palindrome")
# qno 6
name = "Ahsan Raza Talpur"
print(name.lower())

# Qno 7
name = 'Ahsan Raza Talpur'
print('Raza' in name)
# Qno 8
name = "Ahsan Raza Jutt"
name2 = name.replace("jutt","Talpur")# -----------------------------------------------
print(name2)

#Qno 9
greet = "Hello"
greet1 =greet.count('H')
print("H -->",greet1)
greet2 =greet.count('e')
print("E -->",greet2)
greet3 =greet.count('l')
print("L -->",greet3)
greet4 =greet.count('o')
print("O -->",greet4)
greet  = 'Hello'
greet2 =greet.index('H')
print("H -->",greet2)
greet2 =greet.index('e')
print("E -->",greet2)
greet2 =greet.index('l')
print("l -->",greet2)
greet2 =greet.index('l')
print("L -->",greet2)
greet2 =greet.index('o')
print("O -->",greet2)
"""