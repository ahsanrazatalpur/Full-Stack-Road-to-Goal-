# Practice question of Breakandcontinue

# Qno 1
for i in range(1,21):
    if i%3 == 0:
        continue
    if i == 16:
        break
    print(i)

print("-----------------------------------")

#Qno 2
for i in range (1,51):
    if i == 23:
        break
    print(i)

print("-----------------------------------")
#Qno 3

for i in range(1,16):
    if i%2  == 0:
        continue
    print(i)
print("-----------------------------------")

#Qno 4
for i in range (1,30):
    if i%4 == 0:
     continue
    if i == 21:
     break
    print(i)
