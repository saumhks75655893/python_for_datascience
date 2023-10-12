# ------------------------------------  SET METHOD  --------------------------------------------- #

# '''difference() -  The difference() method returns the set difference of two sets.
# difference() methods returns the difference between two sets which is also a set. It doesn't modify original sets'''

# s1 = {1,2,3,4}
# s2 = {2,4,5,6}
# t = (6,7,3,4,8)
# s3 = s1.difference(s2)
# print(s3)

# s4 = s2.difference(t)
# print(s4)
# s5 = [1,3,4,6]
# s6 = s1.difference(s5)
# print(s6)
# print(s1)

# ''' difference_update() -  The method returns the set difference of two sets. The method returns the difference between two sets which is also a set. It does modify original sets.'''


# s1 = {1,2,3,4,5}
# s2 = {1,2,3}
# s1.difference_update(s2)
# print(s1)
# print(s2)

# ''' symmetric_difference  -  The symmetric difference of two sets A and B is the set of elements that are in either A or B, but not in thier intersection. But not make any changes in oiginal set. '''

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# s3 = s1.symmetric_difference(s2)
# print(s3)
# print(s1)
# print(s2)

# ''' symmetric_difference_update() - The symmetric difference update of two set A and B is the set of elements that are in either A or B, but not in their intersection. And make any changes in original set.  '''

# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# s1.symmetric_difference_update(s2)

# print(s1)
# print(s2)

# s2.symmetric_difference_update(s1)
# print(s1)
# print(s2)

# ''' union()  -  The union of two or more sets is the set of all distincts present. '''

# a = {1,2,3,4}
# b = {3,4,5,6}
# r = a.union(b)
# print(r)
# print(a)
# print(b)

# ''' 
# intersection() - The intersection() method returns a new set with elements that are common to all sets. It doesn't modify original sets. 
# '''

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# r = s1.intersection(s2)
# print(r)
# print(s1)
# print(s2)

# ''' 
# intersection_update()  -  The intersection_update() method find common elements in all set. It does modify original sets. 
# '''

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# # s1.intersection_update(s2)
# # print(s1)
# # print(s2)
# s2.intersection_update(s1)
# print(s1)
# print(s2)

'''pop() - the pop() method removes element from anywhere in a set. '''
s1 = {1,2,3,4}
r = s1.pop()
print(r)
