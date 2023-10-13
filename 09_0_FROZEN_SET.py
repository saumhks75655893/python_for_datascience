# # -------------------------------- :  FROZEN SET  : --------------------------------------- #

# ''' Frozen set is just an immutable version of a Python set object. While elements of a set cna be modified at any time, elements of the frozen set remian the same after creation. 

# - Unordered
# -Unindexed
# -No duplicate
# '''

# t = (1, 2, 3, 4)
# f = frozenset(t)
# print(f)
# print(type(f))

# t = [5, 5, 6, 5, 3]
# f = frozenset(t)
# print(f)
# print(type(f))

# t = "Himanshu kumar"
# f = frozenset(t)
# print(f)
# print(type(f))

# t = {1, 2, 3, 4, 56, 7}
# f = frozenset(t)
# print(f)
# print(type(f))

s = {1,2,3,4}
f = frozenset([5,6,7])
s.add(f)
print(s)
