# Operation in Tuples

# # we cannot make directley changes on tuples(add, delete etc) we covert it into list than perform operation

# # .append(value) ad value at the last of list(temporory convert to list and make change and again change to tupple)
# tupp = ("Pakistan", "India", "China", "Iran")
# tupp2 = list(tupp)
# tupp2.append("Nepal")
# tupp = tuple(tupp2)
# print(tupp)
# print(type(tupp))


# # pop(index) to remove the value on that index(temporory convert to list and make change and again change to tupple)
# tupp = ("Pakistan", "India", "China", "Iran")
# tupp2 = list(tupp)
# tupp2.pop(1)
# tupp = tuple(tupp2)
# print(tupp)
# print(type(tupp))


# # change value by indexing(temporory convert to list and make change and again change to tupple)
# tupp = ("Pakistan", "India", "China", "Iran")
# tupp2 = list(tupp)
# tupp2[0] =("Islami Jamohoria Pakistan")
# tupp = tuple(tupp2)
# print(tupp)
# print(type(tupp))



###   Some method that can Directly used on tuple  ###

# we can merge two tuple without changing it to list
# asia = ("Pakistan", "India", "Bangladesh", "Iran", "China")
# europe = ("America", "Russia", "Ukraine", "Finland", "Poland")
# world = asia + europe
# print(world)
# print(type(world))

# count (count the occurence of valur in tuple)
# marks = (10, 15, 10, 20, 10)
# con = marks.count(10)
# print(con)


# index(value) tell the index of that value
# marks = (10, 15, 10, 20, 10)
# con = marks.index(10)
# con = marks.index(1 , 3 , 10) (start, end , target) find the index of that value in particular index
# print(con)


# len() to find the length of tupple
# tup = (1, 2, 3, 4, 5)
# print(len(tup))

# All the methods of list can be used but firstly change tupple into list then do what to do again convert to tupple


