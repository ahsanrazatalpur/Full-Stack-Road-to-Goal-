# Set in Python
# no repeted entries
# collection of well defined object

st = {2, 4, 2, 6} 
print(st)  # 2 4 8
print(type(st))

# we can do all the operation except repeat the entries
# unorder collection ( no order maintance)
# seprated by commas aand enclosed in qurly bracket
# imutable
# can't contain duplicate item

basket = {"toy", 12, 88 , 12 ,"toy", "Ball"}
print(basket) # unorder

# print(basket[0]) # we cannt do this because there is no order in set
empty = set()  # only the way to craete empty set
print(empty)
print(type(empty))

basket = {"toy", 12, 88 , 12 ,"toy", "Ball"}
for item in basket: # way tom print set
    print(item)

