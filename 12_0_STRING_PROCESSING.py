# --------------------------------------: STRING PROCESSING :---------------------------------------------- #

#                         -------------- : STRING LITERAL : ----------
#                     -----------------: single line string :-------------------
a = "hello"
print(a)

#                      ----------------: Multiline string :-------------------

a = '''hello
Himanshu kumar
what are you doing?
Where are you going?
'''
print(a)
a = 5
b = 10
c = a + b
print(f"sum {a} and {b} is {c}")
print(f"sum %d and %d is %d"%(a,b,c))

print("c:\\newfolder\\himanshukumar")


#  --------------------------------- : Memory Representation of String : ------------------------------------- #

# 1. Indexing (slicing): -------
s = "Hello"
print(s[2])
print(s[0:4])
print(s[-1::-1])

#2. String is not mutable.
#3. String is iterable
#4. Nested structure is not allowed.


# STRING OPERATIONS : -------------------

# String concatination : -----

a = 'hello'
b = " himanshu"
print(a+b)

# String repetition : --------

a= 'hellohellohellohello'
print(a)


# Membership operator : -----------

a = 'hello'
print('e' in a)

s = "himanshu kumar"
print("kumar" in s)
print('' in s)              # imp


n = 341234
p = str(n)
print(p)
print(type(p))


# tuple to string : ---------

t = (1, 2, 3, 4)
p = 1
h = str(t)

#  Now calculate the number of element present in this string.
print(f"The length of the string is {h}  is   :   {len(h)}")

# How see this explaination.
for i in h:
    print(f"At {p} position the character is :  {i}")
    p += 1


#  Character code conversions : ----------

# ord() : a single character to its underlying integer code. 
# chr() : taking an integer code and converting it to the corresponding character. 
# bin() : convert into binary

s = 'a'
print(ord(s))
n = 65
print(bin(ord(s)))
