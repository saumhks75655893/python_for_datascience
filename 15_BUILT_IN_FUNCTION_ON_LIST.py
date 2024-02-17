#  ------------------------- :  BUILT - IN FUNCTIONS ON LIST    : --------------------------------------- #
import itertools
import operator
#  1. sum() : ----------

L = [1,2,3,4,5,6]
m = sum(L)
print(m)

#  2. max() : -----------
m = max(L)
print(m)

#  3. min() : ------------

mi = min(L)
print(mi)

# 4. all() : -------------

l = [1,2,3,True, False]
m = all(l)
print(m)

# 5. any() : -----------

n = any(l)
print(n)

#  6. len() : ---------

n =len(l)
print(n)

#  7. type() : -------

print(type(l))

#  8. enumerate() : ----------

l = [1,2,3,4]
s = list(enumerate(l))
print(s)
s2 = list(enumerate(l,100))
print(s2)

#  9. accumulate() : --------------------------------

l = [16,11,1,13,18,5,4,3,2]
r = itertools.accumulate(l,max)

print(l)
for i in r: 
    print(i,end='  ')