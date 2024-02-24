# FUNCTIONS IN REGEX : ---------

import re

a = """ 
John has scored 89 marks
Lisa has scored 90 marks
David has scored 70 mars
"""

b = "rohan das 89 to 60"

# 1. re.findall() : -------

print(re.findall(r"\d+", a))
print(re.findall(r"[A-Z][a-z]*",a))

# 2. re.complie() : ------

p = re.compile('[a-d]')
print(re.findall(p,a))

p = re.compile('[0-9][0-9]')
print(re.findall(p,a))

p = re.compile('[0-9]')
print(re.findall(p,a))

p = re.compile('\d+')
print(re.findall(p,a))


# 3. re.split() :---------

a = re.split("\d+", a)
print(a)

# 4. re.sub() : --------

print(re.sub("\s","",a))
print(re.sub("\s","",b))

# 4. re.subn() : --------

print(re.subn("\s","",a))
print(re.subn("\s","",b))

# 4. re.escape() : --------

print(re.escape(a))
print(re.escape(b))

# 4. re.search() : --------

print(re.search(r"\d+",a))
print(re.search(r"\d+",b))





