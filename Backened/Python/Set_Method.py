# # Methods in Set

# # Union(combine to set but no repeat no sequence)
# s1 = {1, 3, 5, 7, 9}
# s2 = {2, 4, 6, 8, 10}
# print(s1.union(s2))

# # Intersection( the value which are repeating or same in both sets)
# s1 = {1, 3, 5, 7, 9}
# s2 = {2, 4, 6, 8, 10}
# print(s1.intersection(s2))

# # update( update the value or gain the value from other set)
# s1 = {1, 3, 5, 7, 9}
# s2 = {2, 4, 6, 8, 10}
# print(s1.update(s2))
# print(s1) # here s1 gain all the value from s2

# # intersection update(update the value which are same in both)
# s1 = {1, 3, 5, 7, 8 ,4 , 9}
# s2 = {2, 4, 6, 8, 10}
# print(s1.intersection_update(s2))
# print(s1) # 

# symetric difference (update the value which are not same in both)
# s3 = {1, 3, 5, 7, 8 ,4 , 9}
# s4 = {2, 4, 6, 8, 10}
# print(s3.symmetric_difference(s4))

#  difference (update the value which are not same in both man A-B same value cut )
# s3 = {1, 3, 5, 7, 8 ,4 , 9}
# s4 = {2, 4, 6, 8, 10}
# print(s3.difference(s4)) 


# #  IsdisJoint (Value are not common in both if yes than false)
# s3 = {1, 3, 5, 7, 8 ,4 , 9}
# s4 = {2,  6, 10}
# print(s3.isdisjoint(s4)) #True

# #  Superset (all values of one set value are avaliable to other one)
# bara set jiske sare element dusre chote set mn avaliable hu to bare wala super set hai
# s3 = {1, 2, 3, 5, 6,7, 8 ,4 , 9}
# s4 = {2,  6, 10}
# print(s3.issuperset(s4)) #True

# #  Subset (all values of one set value are avaliable to other one and other one set called subset)
# # chota set jiske sare element dusre bare set mn avaliable hu to chote wala subset hai bare ka
# s3 = {1, 2, 3, 5, 6,7, 8 ,4 , 9, 10}
# s4 = {2,  6, 10}
# print(s4.issubset(s3)) #True

# .add()  to add element to set
# sett = {1, 2, 4, 5}
# sett.add(3)
# print(sett)

# .update()  to add one set element to  other set
# sett1 = {1, 2, 4, 5}
# sett2 = {2, 2, 6, 19}
# sett1.update(sett2)
# print(sett1)


# Remove and discard are almost same but remove rays error if remove item is not present but dicard dont show error

# .remove()  to remove item from the set( show error if removing item not present mean lower line doesn't execute program stop)
# sett1 = {1, 2, 4, 5}
# sett1.remove(5)
# print(sett1)

# .discard()  to remove item from the set(does not show error if removing item not present)
# sett1 = {1, 2, 4, 5}
# sett1.remove(5)
# print(sett1)

# .pop()  to remove randomn value from set
# sett1 = {1, 2, 4, 5}
# print(sett1.pop())
# print(sett1)

# .del()  to delete set
# sett1 = {1, 2, 4, 5}
# del sett1
# print(sett1)

# .clear()  to clear set
# sett1 = {1, 2, 4, 5}
# sett1.clear()
# print(sett1)


