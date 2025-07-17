# Method in Dictinory

# update (update or add one dict item to another)

EID = {
    2334 : 20,
    3974 : 90,
    2847 : 88
}
EID2 = {
    9239: 87,
    393 : 77,
    872 : 67
}

EID.update(EID2)
print(EID)

# clear(to clear all the Dictinory)
EID = {
    2334 : 20,
    3974 : 90,
    2847 : 88
}
EID.clear()
print(EID)

# Empty Dict

Empt = {}
print(Empt)

# pop( to remove any item from Dic)
EID = {
    2334 : 20,
    3974 : 90,
    2847 : 88
}
EID.pop(2334) # remove target key value
EID.popitem() # remove last key value
print(EID)


# Del( to delte dict)
# del EID
# del EID[2847] to delete specific key just
# print(EID)

