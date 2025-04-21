import time
timesstamp = time.strftime('%H')
print(timesstamp== time.strftime('%H'))
if(int(timesstamp== time.strftime('%H')) >= 6 and int(timesstamp== time.strftime('%H')) <12):
    print("Good Morning Sir :) ")
elif(int(timesstamp== time.strftime('%H')) == 12 and int(timesstamp== time.strftime('%H')) <2 ):
    print("Good After Noon Sir :)")
elif(int(timesstamp== time.strftime('%H')) >= 2 and int(timesstamp== time.strftime('%H'))< 4 ):
    print("Good Evening Sir :)")
else:
    print("Good Night sir , Have a sweat dream :)")

