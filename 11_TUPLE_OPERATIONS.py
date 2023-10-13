# ----------------------------------- : TUPLE OPERATIONS : -------------------------------------- #

#  index() -  to find the index of the element of the tuple .

t = (11,12,13,14,15)
r = t.index(14)
print(r)

# Duplicate value (index ): -----

t = (1,2,3,4,4,5,6,6,4)
r = t.index(4,5)
print(r)

#  count()  - It's used to count the number of element is present in the tuple.

t = (1,2,3,4,4,5,6,6,7,4,3,4,3,4,4,3,4)
r = t.count(4)
print(r)

r = t.count(110)
print(r)

# sorted() - It's used to sort the tuple in ascending or descending order.

t = (45,565,2,34,2,5,6,3453,6,2,34,56,2,57,43343,54,456)
m = sorted(t)
print(m)

m = sorted(t, reverse=True)
print(m)

t = ('aaaa','bbbbbb','ccc', 'ddddd')
i = sorted(t, key=len)
print(i)

# by using function we can aslo sort the tuple but thier should be at least nested tuple.

def sec(el):
    return el[1]

t = ((1,1452), (19,234), (34, 534))
i = sorted(t, reverse=False, key=sec)
print(i)


#  min() - to find minimum value of the tuple
# max() - to find maximum value of the tuple.
# sum() - to find the sum of all the element of the tuple.

t = (1,2,3,4,3345,453,2345,735,21)
minV = min(t)
print(minV)
maxV = max(t)
print(maxV)
sumofelement = sum(t)
print(sumofelement)

# NESTED TUPLE OPERATIONS : ----------

t = ((1, 20), (20, 100), (20, 111))
i = min(t)
print(i)
i = max(t)
print(i)

I = min(t[2])
print(I)
I = max(t[2])
print(I)
I = sum(t[2])
print(I)
