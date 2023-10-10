# # ----------------------------- : SETS : -------------------------------------- #

# '''
# it is collection which is both unordered and unindexed and written with curly brackets unchangeable, don't allow duplicate values.
# '''

# men = {'ram', 'shyam', 'sita','radhe'}
# men.add('Himanshu kumar')
# men.remove("Himanshu kumar")
# print(len(men))
# print(men)

# s = {1,1.0, -1, 45, 9.4}
# print(s)

# SET CONSTRUCTOR : -------

l = [11, 12, 13, 14, 15]
print(l)
print(l[0])
s = set(l)
print(s)
# print(s[0])

S = 'apple'
s = set(S)
print(s)

# Set constructor is used to create a empty set.

s = set()
print(s)
print(type(s))

s.add(10)
print(s)

s = {10,20,33,13,15,19}
for i in s: 
    print(i)

m = set()
for i in range(1,10): 
    n = int(input("Enter the value : "))
    m.add(n)
a = 0
for i in m: 
    print(f"{a} element is -> {i}")
    a += 1
    

#  We can compare a list which values is equal but position is not equal than we can convert it in to set then compare that then we will find  True if the values are equal. 
 
l1 = [1,2,3]
l2 = [2,3,1]                             

s1 = set(l1)
s2 = set(l2)

print(s1 == s2)

#  DATABASE QUERY : --------

DeptSale = {'Ram', 'Shyam', 'Tiara'}
DeptProduction = {'Ram', 'Radha', 'Tiara'}

print(DeptSale & DeptProduction)
