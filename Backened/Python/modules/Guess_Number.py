import random
print("***    WELCOME TO NUMBER GUESS GAME    ***")
number = int(input("Im thinking of number from 1 to 100 ,can you guess ? "))
randomNumber = random.randint(1,10)
if number ==  randomNumber:
    print("Congratulation, you Guess the write number ,The number is: ",randomNumber)
elif number < randomNumber:
    print("Too low  ! guess again")
else:
    print("Too high ! guess again")

