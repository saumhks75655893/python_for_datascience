#                   -------------------        LIST            -------------------                   #
#  ---------------------------------- :  BASIC LIST OPERATIONS : -------------------------------------------

#  1. CREATING LIST : ------------------

# empty list : -----
S = []
s1 = list()
print(S)
print(s1)

# list with elements :------
r = [1,2,3,4, None]
print(r)

#  mixed typ list : -----

r = [1, 1.2, 'ram', False]
print(r)

#  using list method converting from a type to another type : -----

r = (10, 20 , 40 , 50)
m = list(r) 
print(m)
print(type(m))

# 2. CONCATINATING USING + : ------

s1= [1,2,3,4]
s2 = [5,6,7]
s = s1 + s2
print(s)

# 3. MULTIPLYING USING * : -------

l1 = [1,2,3]
l = l1 * 3
print(l)

# 4. MEMBERSHIP OPERATOR IN LIST : ------

l1 = [1,2,3,4,5,[6,7]]
r = 1 in l1
print(r)
r= 6 not in l1
print(r)
r = [6,7] in l1
print(r)

# 5. ITERATION ON LIST : ---------

l = [1,2,3,4,5,6]
for i in l: 
    print(i)

# 6. DELETING LIST : ------------

l = [1,2,3,4,5]
print(l)
del l
print(l)

# 7. INDEXING : -----------

l = [11, 12, 13, 14, 15]
print(l[3])

l[-1] = 20
print(l)

del l[3]
print(l)

# 8. LIST SLICING : ------

l = [1,2,3,4,5,6]
l[1:4] = [100, 200, 300]    # replace items
print(l)
del l[1:4]      # delete item from selected place
print(l)

l = [1,2,[3,4],5,6]
print(l[2][1])
