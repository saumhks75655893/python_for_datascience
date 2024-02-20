import re
a = "harry potter"

match = re.findall(r"\Ahar",a)
print(match)

match = re.search(r"ter\b",a)
print(match)

match = re.search(r"\bhar",a)
print(match)

match = re.search(r"har\B",a)
print(match)

match = re.search(r"\Bter",a)
print(match)

a = 'harry1 potter2'
match = re.search(r"\d",a)
print(match)
match = re.findall(r"\d",a)
print(match)

a = 'harry1 potter234@^&5'
match = re.findall(f"\D",a)
print(match)

a = "harry potter 4@5"
match = re.findall(r'\s',a)
print(match)
match = re.findall(r'\S',a)
print(match)

a = 'harry1 4#@%'
match = re.findall(r"\w",a)
print(match)
match = re.findall(r"\W",a)
print(match)

match = re.findall(r"\Z",a)
print(match)
