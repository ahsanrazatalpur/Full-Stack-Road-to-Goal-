# List in Python
# list mean collection of same entity

l = [1, 2, 3, 4, 5]
print(l)
print(type(l))

marks = [90, 88, 78, 76, 55]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

# List are order collection of entity
# List are seprated by commas and enclosed in square bracket
# List are changable

# List can also store different type of Datatypes
items = [1, 5, "red", False , None]
print(items)
print(type(items))
print(len(items))


# Negative Indexing

print(marks[-3]) # negative Index
print((marks[len(marks) - 3])) # Positive Index


# To chek any element present in list
# For number
if 90 in marks:
    print("Yes")
else:
    print("No")

# For String
if "Ahs" in "Ahsan":
    print("Yes")
else:
    print("No")

print(marks) # to print All marks

# Slicing
print(marks[:]) # to print All marks
print(marks[::2]) # to print All marks but skip one number
print(marks[-1:]) # to print last marks
print(marks[:-1]) # to print All marks exxept last one


