#Creating hotel website where user ask for choice food

# we take dictinory to store item and price

menu = {
    "Pizza" : 450,
    "Burger" : 320,
    "Coffe" : 120,
    "Salad" : 80,
    "Raita" : 50,
    "Chapati" : 35,
    "Chiken Biryani" : 350,

}

# Greeting user  
print(" ***        WELCOME TO OUR NASHEELA DHABA        ***   ")
print()
print("01. Pizza  : 450 Rs\n02. Burger  : 320 Rs\n03. Coffe   : 120 Rs\n04. Salad   : 80 Rs\n05. Raita   : 50 Rs\n06. Chapati : 35 Rs\n07. Chiken Biryani  : 350 Rs")
order_total = 0

item_1 = input("Please enter item to Order : ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"{item_1} added succesfuly")
else:
    print(f"{item_1} is not availiable")

another_order = input("You want to Order anything else? yes/no")
if another_order == "yes":
    item_2 = input("Enter second item ")
    if item_2 in menu:
        order_total += menu[item_2]
    else:
        print(f"{item_2} is not avaliable")
print("Total Bill =",order_total,"RS")
print()

print("          *** Bill ***")
print("-----------------------------------")
print("Items                     Price")
print("-----------------------------------")
print(item_1,"                  ",menu[item_1],"Rs")
print()
print(item_2,"                  ",menu[item_1],"Rs")





