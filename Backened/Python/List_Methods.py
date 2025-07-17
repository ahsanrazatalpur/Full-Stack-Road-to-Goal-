# Methods To manipulate the List

# li = [2, 4, 6, 8]
# print(li)

# # .append(add data in the last of the list)
# li.append(10)
# print(li)

# sort() method to sort the list but return nothing
# li = [5, 3, 8, 2]
# print(li)
# print(li.sort())  #None
# print(li.sort(reverse = True))  #List sort in Descending order
# print(li) #[2, 8, 3, 5]

#reverse  (reverse the list but return nothing)
# li = [5, 3, 8, 2]
# print(li.reverse()) #None
# print(li)  #[2, 8, 3, 5]

# index (return the index of that value first occurence only)
# li = [1, 2, 3, 4, 5]
# print(li.index(1)) #0
# print(li.index(4)) #3

# #count (count the value)
# li = [1, 2, 1, 4, 5]
# print(li.count(1)) # 2

# #
# l = [12, 34, 56, 56]
# m = l
# m[0] = 0
# print(m)



# insert(index,value) (insrt item at certain index)  return nothing
# li = [1, 2, 3, 4, 5]
# print(li.insert(1, 20))
# print(li)



# extend()  to merge two attribute at the last and return nothing
# l = [1, 2, 3, 4, 5]
# m = [22, 33, 44, 55]

# # simple way to merge list just by combing two lst with new variable
# n = l + m
# print(n)

# # merge two list with pre-built function 
# print(l.extend(m))
# print(l)



# Quick Look on Methods of List
# 1. append(value) add value in the last and return nothing
# 2. insert(index,value) add value in the given index and return nothing
# 3. sort() add sort the list in ascending order and return nothing
#  sort(reverse = True)  add sort the list in descending order and return nothing
# 4. reverse() reverse the list and return nothing
# 5. index() return  the  index of that value in list first occurence only and return value
# 6. count() count the  occurence of  that value  and return the counting value
# 7. extend() merge the  two list value  and return nothing 
# or merge two list by combing them in new variable

