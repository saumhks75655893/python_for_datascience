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

# 4. descard() - It's like remove method. It never gives error either element is exist or not. 

s = {1,2,3}
s.discard(55)
print(s)