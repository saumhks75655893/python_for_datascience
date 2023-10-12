# #  ----------------------------------   SET METHODS ------------------------------------------- #

# ''' A set of statements, together perform a single task. '''

# # 1. add() - add a given element to the set. 

# s = {'Himanshu', 1, 3, 2}
# r = (10,20)
# s.add(r)
# # it never adds a list. 
# print(s)

# # 2.  clear()-> removes all elements from the set. 

# s = {10, 20 , 'himanshu'}
# s.clear()
# print(s)

# 3. remove() - Delete specifiec element , it given element doesn't exist so KeyError exception will be thrown.  

# s = {1,(2,3)}
# s.remove(1)
# print(s)

# # 4. descard() - It's like remove method. It never gives error either element is exist or not. 

# s = {1,2,3}
# s.discard(55)
# print(s)

# # copy() - The copy method returns a shallow copy of the set.

# s1 = {1,2,3}
# s2 = s1
# s3 = s1.copy()
# s3.add((34,39))
# s2.add(4)
# print("Original set : ", s1)
# print("Assignment copy : ",s2)
# print("Copy method  :  ",s3) 

# # update() -  The Python set update() method updates the set, adding items from other iterables.

# s = {1,2,3,4}
# s1 = {5,6}
# t = (7,8)
# l = [9,10,11]
# s.update(s1)
# print(s)
# s.update(t)
# s.update(l)
# print(s)

# s.update(s1,t,l)
# print(s)

