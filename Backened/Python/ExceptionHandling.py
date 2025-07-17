# Error Handling or Exception Handling

# we got error by our mistake or by error through server data fatch so py prohgram show error

a = input("Please enter table number")
print(f"The table of {a} is")

try:
 for i in range (1,11):
    print(f"{a} X {i} = {int(a)*i}")
except Exception as error:
  print(error)
print("End of the Program")


a = input("Please enter table number")
print(f"The table of {a} is")

try:
 for i in range (1,11):
    print(f"{a} X {i} = {int(a)*i}")
except:
  print("error")
print("End of the Program")


# specific error handling 
try:
  num = input(int("ENter integer"))
except ValueError:
  print("Value Error")