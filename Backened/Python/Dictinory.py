# Dictinory (key value pair)
# order collection of data item

dic = {
    "name" : "Ahsan Raza",
    "age" : 20,
    "Dept" : "Computer Science"
}
print(dic)
print(dic["name"])
print(dic["age"])
print(dic["Dept"])

EID = {
    1 : "Ahsan Raza",
    2 : "Alee Raza",
    3 : "Mehdi Raza"
}
print(EID[1])
print(EID[2])
print(EID[3])

# to way to get value from key

ex = {
"name"  : "Ahsan",
"Age" : 20,
"eligible" : True
}
print(ex["name"])  # 1st way (if value not present than throw error)
print(ex.get("name"))  # second way (if not present than throw None)

# to get all keys
Family = {
    1 : "Ahsan Raza",
    2 : "Alee Raza",
    3 : "Mehdi Raza"
}
print(Family.keys)
for key in Family.keys():
    print(key)
    print(Family[key])


    PUBG ={
        232938329 : "Ahsan Raza",
        848287236 : "Ismail",
        364328439 : "ShahBaz"
    }
    for key in PUBG.keys():
        print(key)
        print(PUBG[key])
print(PUBG.keys()) # to get all keys
print(PUBG.values()) # to get all values


PUBG ={
        232938329 : "Ahsan Raza",
        848287236 : "Ismail",
        364328439 : "ShahBaz"
    }
print(PUBG.items())
for key, value in PUBG.items():
    print(f"The {value} has {key}")

        