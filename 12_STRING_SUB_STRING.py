# -------------------------------------- : SUB STRING FUNCTION : -------------------------------- #

# 1. COUTN :------

s = "Python is a best langauge and Python can be use anywhere."
s1 = "Python"
r = s.count(s1,0,-1)
print(r)

# 2. FIND : ------

s = "Python is a best langauge and Python can be use anywhere."
r = s.find("Python",1)
print(r)

# 3. RFIND : ------

s = "Python is a best langauge and Python can be use anywhere."
r = s.rfind("Python")
print(r)

# 4. index : ------

s = "Python is a best langauge and Python can be use anywhere."
r = s.find("Python")
print(r)

# 5. rindex : ------

s = "Python is a best langauge and Python can be use anywhere."
r = s.rindex("neon")
print(r)

# 6. STARTSWITH : -------

s = "Python is the best language"
s1 = 'Python'
r = s.startswith(s1)
print(r)

# 7. ENDSWITH : ------

s = "Python is the best language"
s1 = 'Python'
s2 = ('age', 'ge', 'la')
r = s.endswith(s1)
r1 = s.endswith(s2)
print(r)
print(r1)

#  8. REPLACE : --------


s = "Python is the best language"
# r = s.replace('Py', 'Ly')
r = s.replace('Py', 'Ly',1)
print(r)


