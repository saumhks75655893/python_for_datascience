import re
a = "harry potter"

match = re.findall(r"\Ahar",a)
print(match)

match = re.search(r"ter\b",a)
print(match)

match = re.search(r"har\B",a)
print(match)