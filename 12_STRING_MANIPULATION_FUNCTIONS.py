# ------------------ : STRING MANIPULATION FUNCTION : ---------------------------- #
# 1.
S = 'a@python'
print(S.isidentifier())

#  2.
a = '\n'
print(a.isprintable())

# 3.
a = 'ram is a good boy'
a = ''
r = a.isspace()
print(r)
a = '\r'
r = a.isspace()
print(r)
a = '\b'
r = a.isspace()
print(r)
a = '\n'
r = a.isspace()
print(r)
a = '\a'
r = a.isspace()
print(r)
a = '\t'
r = a.isspace()
print(r)

# 4.

a = "Ram Is A Good Boy"
r = a.istitle()
print(r)

5.
s = '   This is Python   '
print(s)
r = s.strip(' Tn ')

s = '   This is Python   '
print(r)
r = s.rstrip(' Tn ')

s = '   This is Python   '
print(r)
r = s.lstrip(' Tn ')
print(r)

# 6. 
s = "This is Python is Programming"
r = s.partition("is")
print(s)
print(r)
r = s.rpartition("is")
print(s)
print(r)

# 7. 
s = "This is Python is Programming"
r = s.split()
r = s.split(' ',2)
print(r)
s = "This ,is ,Python ,is, Programming"
r = s.rsplit(" ," , 2)
print(r)

# 8. 
s = "HAPPY \n NEW \n YEAR"
r = s.splitlines()
r = s.splitlines(True)
print(r)