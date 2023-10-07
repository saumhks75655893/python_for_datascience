#  Type casting 
# 1. Implicit type casting   ( It is done by computer/python interpretor)
# 2. Explicit type casting  (It's done by user/programmer)

# 1. Implicit type casting : -----------

a = 6
b = 2.0
c = a + b
print("c = ",c)
print("type of c : ",type(c))

# 2. Explicit type casting : ---------

a = True 
b = int(a)
print("b = ",b)
print("type of b : ",type(b))

c = "123"
b = int(c)
print("b : ",b)
print(type(b))


b = "123"
c = complex(b)
print(c)