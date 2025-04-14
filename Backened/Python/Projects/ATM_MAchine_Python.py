print("***   WELCOME TO APNA ATM MACHINE   ***")
print("Press 1 to Deposit money ")
print("Press 2 to Withdram money ")
print("Press 3 to Check Balance ")
print("Press 4 to Exit ")

option = int(input("Please choose a option :"))
money = 0

if option in  [1,2,3,4]:
    deposit =int(input("Enter an amount to Deposit :"))
    money += deposit
elif option == 2:
    withdraw =int(input("Enter an amount to Withdraw :"))
    money -= withdraw
elif option == 3:
    print("Your current Balance is :",money)
else:


