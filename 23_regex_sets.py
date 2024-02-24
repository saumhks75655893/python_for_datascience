import re

a = "charlie and the chocolate factory"
match = re.findall("[ats]",a)
print(match)

a = 'charliez and @'
match = re.findall("[a-t]",a)
print(match)

a = "char yz &"
match = re.findall("[^atx]",a)
print(match)

a = "charlie 1 & 4 factory"
match = re.findall("[0123]",a)
print(match)

match = re.findall("[0-9]",a)
print(match)

a = "charlie 11 21& 49 99 100 factory"
match = re.findall("[0-9][0-9]",a)
print(match)

a = "chaADFADadfasdfrlie 11 21& 49 99 100 faFctory"
match = re.findall("[A-Z][a-z]",a)
print(match)

a = "HiHello12"
match = re.findall("[a-zA-Z]",a)
print(match)

a = "HiHello@#$"
match = re.findall("[$]",a)
print(match)
