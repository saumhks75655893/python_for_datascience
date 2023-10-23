#  ----------------------------------- : METHODS OF LIST : --------------------------------------------- #

# 1. APPEND ---------

L = [11,12,13]
L.append(14)
print(L)

# by using slicing ------------------

#  add a element at last
L[4:] = [50]
print(L)
# add a element in between the last
L[2:2] = [153]
print(L)
# add a element at the first position 
L[:0] = [123]
print(L)

# 2. EXTEND :-------------------------------

l = [11,12,13,14,15]
l.extend([14,15,16])
print(l)
#  using slicing : ---

l = [16,17,18]
l[:0] = [1,2,3]
l[2:2] = [4,5,6]
l[len(l):] = [7,8,9]
print(l)

# 3. INSERT : --------------------------------

l = [5,7,9,11,13]
l.insert(2,180)
print(l)

# 4. INDEX : -----------------------

l = [5,8,9,11,13,1,11,1110,145,345]
r = l.index(11,6)
print(r)
r = l.index(11,7,9)
print(r)

#  5. COUNT : ------------

l = [5,4,3,2,1]
l.sort()
print(l)
l = [5,4,12,345,1,0]
l.sort(reverse=True)
print(l)

l = ['abc','aBc','ABC']
l.sort()
print(l)
l.sort(key=str.lower,)
print(l)

# 6. REVERSE : ---------

L = [5,4,3,6,10,11]
L.reverse()
print(L)

# 7. COPY : -----------------------------

l = [5,4,3,2,6,8,9]
s = l.copy()
print(s)
s.append(1000)
print(s)
print(l)

s1 = l[:]     # copy using slicing
print(s1)
s1.append(13000)
print(l)
print(s1)

#  8.  CLEAR : ------------------------

l = [1,2,3,4,5]
l.clear()
print(l)
del l[:]
print(l)

# 9. POP()  : ---------------------------

l = [1,2,3,4,5,6]
s = l.pop()
s1 = l.pop(3)
print(s)
print(s1)
print(l)

#  10. REMOVE : ----------

l = [1,2,3,5,3,4,5,6]
l.remove(3)
print(l)