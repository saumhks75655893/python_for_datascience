#  ------------------------------------ : TUPLE : ----------------------------------------#

t = (1,2,3,4,5,6,7)
print(t)

#  creating single element tuple : ----------
t = (1,)
print(t)
print(type(t))

# creating single element tupe by using tuple method 
t = tuple()
print(t)
print(type(t))

# From string to tuple 
s = "Hello python"
t = tuple(s)
print(t)

# TUPLE INDEXING : ---------

t = (11,12,13,14,15)

print(t[0])
print(t[-4])

#  TUPLE SLICING :--------

print(t[0::2])
print(t[-1::-1])

# NESTED TUPLE INDEXING AND EXTRACTING VALUES : ------

t = (1,2,3, (4,56),9,10)
print(t[3][0])

t = (1,2, [4,5,6], 7,8)
t[2][1] = 10
print(t)

t1 = (1,2,3,4)
t2 = (3,4,5,6,7)
t = t1 + t2
print(t)
print(t1)
print(t2)


