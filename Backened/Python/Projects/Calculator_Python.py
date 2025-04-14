print("*** CALCULATOR ***")
print("Press 1 for Add")
print("Press 2 for Substract")
print("Press 3 for Multiply")
print("Press 4 for Divide")
print("Press 5 for Floor function")
print("Press 6 for Exponent")
print("Press 7 for Reminder")

option = int(input("Please Choose a option: "))
if option in [1,2,3,4,5,6,7]:
    num1=int(input("Please Enter 1st number : "))
    num2=int(input("Please Enter 2nd number : "))

if option == 1:
    print("Sum of two numbers are :",num1 + num2)
elif option == 2:
    print("Substract of two numbers are :",num1 - num2)
elif option == 3:
    print("Multiply of two numbers are :",num1 * num2)
elif option == 4:
    print("Divide of two numbers are :",num1 / num2)
elif option == 5:
    print("Floor Function of two numbers are :",num1 // num2)
elif option == 6:
    print("Exponent of two numbers are :",num1 ** num2)
elif option == 7:
    print("Reminder of two numbers are :",num1 % num2)
else:
    print("Invalid Operation")