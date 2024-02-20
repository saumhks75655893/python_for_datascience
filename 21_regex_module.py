# REGEX MODULE : ------
''' Regular Expression '''

import re

a = "charlie chaplin and the c0a cNa chocolate factory "
b = "ayushi.jain@gmail.com"
c = "hello"
d = "xyz, yz, xyzz, xxxyyz, xxzzy, zyz, xxy"

match = re.search(r"\.",b)
print(match)

match = re.search(r"[@]", b)
print(match)

match = re.findall(r"[l]",c)
print(match)

match = re.search(r'^y',b)
print(match)

match = re.search(r'com$',b)
print(match)

match = re.findall(r'c.a', a)
print(match)
 
match = re.findall(r"cha|fac",a)
print(match)

match = re.findall(r"ch?a",a)
print(match)

match = re.findall(r"ch*a",a)
print(match)

match = re.findall(r"xy+z",d)
print(match)

match = re.findall(r"x{2,4}",d)
print(match)

match = re.findall(r"(x|z)yz",d)
print(match)


