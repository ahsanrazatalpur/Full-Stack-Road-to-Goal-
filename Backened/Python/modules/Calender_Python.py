import calendar
print("***   WELCOME TO CALENDAR    ***")
year = int(input("Please Enter Number Of Year: "))
month = int(input("Please Enter Number Of Month: "))
calendar = calendar.month(month,year)
print(calendar)