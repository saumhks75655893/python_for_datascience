# OPERATORS  OF PYTHON   : ------------

'''
1. ARITHMETIC OPERATOR 
2. COMPARISON OPERATOR 
3. ASSIGNMENT OPERATOR
4. LOGICAL OPERATOR 
5. BITWISE OPERATOR
6. MEMBERSHIP OPERATOR
7. IDENTITY OPERATOR 

'''
# 1. ASSIGNMENT OPERATOR : --------------
print("\n ASSIGNMENT OPERATOS \n")

a = 10
print(a)
d = 10
print(d)
a += 10
print(a)
d -= 10
print(d)
a *= 10
print(a)
d /= 10
print(d)

# 2. COMPARISON OPERATORS : ---------------
print("\n COMPARISON OPERATOS \n")
a = 10 
b = 12

print(a > b)
print(a >= b)
print(a <= b)
print(a < b)
print(a == b)
print(a != b)
print(3 == 3.0)
print(3 <= 4)

x = 4
y = 9
z = 8.3
r = -3

print((x<y) and (z<y) or (r==x))

print(not(2!=3) and True or (False and True))

# 3. ARITHEMETIC OPERATOR : ------

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)


#  4. LOGICAL OPERATOR : -------------

print( (2>1) and (1>2))
print( (2>1) or (1>2))
print(not (1>2))

#  5. Identity Operator : -----------

a = "Ram"
b = "Ram"
print( a is b)
print(a is not b)

#  6. Membership Operator : --------

A = "I am himanshu kumar"
B = "am"
print(B in A)
print(B not in A)

# 7. Bitwise Operator : -----------

a = 10
b = 11

print(a & b)
print(a | b)
print(a ^ b)
print(~ b)    # 1'st compliment
print(b >> 2)   # right shift
print(a << 1)   # left shift
print(-1 >> 11)

# answer will -1 , of all three which is given below : ----------

print(-1 >> 10)
print(-1 >> 4)
print(-1 >> 9)

print(True & False)
print(True | False)
print(True ^ False)
print(~False)
print(~True)
print( True >> 2)
print( True << 2)
print( False >> 2)
print( False << 2)

# ---------------------:  Ternary Operator  : ------------------------ #

# Write a program to check if number is odd or even using ternary operator. 

number = int(input("Enter the number : "))

print("Even" if number%2==0 else "odd")

a = 12
b = 11

print({True: "This is run on True", False : "This is run on False"}[a>b])