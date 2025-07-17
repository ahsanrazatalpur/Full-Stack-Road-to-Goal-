# Break and continue
# break to return
# continue for skip
# loops work iteration by iteration to skip perticular iteration we use continue and when we want to stop or rturn 
# from that iteration we use break
# break mean loop ko chorke nikal jao
# continue mean iteration ko chorke nikal jao

for i in range(1, 12):
   if i == 8:
     break
   print(5 ,"X", i ,"=" ,i*5)
    
print("Loop ko chorke nikal gya")
# continue mean iteration ko chorke nikal jao

print("------------------------------------------------")

for i in range(1, 12):
   if i == 8:
     print("Skip the iteration")
     continue
   print(5 ,"X", i ,"=" ,i*5)
    
print("iteration ko chorke nikal gya")

print("------------------------------------------------")

# printing only even number using continue statemenet

for i in (1,2,3,4,5):
   if i%2 != 0:
      continue
   print(i)
print("------------------------------------------------")

# printing only odd number using continue statemenet
for i in (1,2,3,4,5,6,7,8,9,10):
   if(i%2 == 0):
      continue
   print(i)
   
print("------------------------------------------------")

i = 0
while True:
   print(i)
   i+=1
   if(i%100 == 0):
      break