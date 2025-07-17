# For Loop in Python

# Else can use with For Loop and While loop too

# if for loop code doesnot execute then else part execute
for i in []: #range(6):  # range = n - 1
    print(i)
else:
    print("Invalid I")



for i in range(6):
    print(i)
    if i == 4:# The condition of else execute is its might complete all program 
        break  # here loop doesnot end here loop break so else part does not execute
else:
    print("invalid")

# in continue case loop end so the else part execute
for i in range(6):
    print(i)
    if i == 4:# The condition of else execute is its might complete all program 
        continue  # here loop doesnot end here loop break so else part does not execute
else:
    print("invalid")

# here also loop does not end so else part will not execute
i = 0
while i <= 5:
    print(i)
    i+=1
    if i == 3:
        break
else:
    print("invalid i")


# here also loop end so else part will execute
i = 0
while i <= 5:
    print(i)
    i+=1
    if i == 3:
        continue
else:
    print("invalid i")