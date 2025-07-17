# Recursion are basically function but calling function from the function known as recursion 
# oe Dividing something itself


# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1
# factorial(n) = n * factorial(n-1)

def factorial(n): # function
    if(n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n - 1) # another call inside the function 
    
print(factorial(2))
print(factorial(3))
print(factorial(4))


# see how its work
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1



    