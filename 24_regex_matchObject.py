import re 

a = "John has scored 89 marks"

match = re.search(f"\d+",a)
print(match)
print(match.re)
print(match.string)
print(match.start())
print(match.end())
print(match.span())
print(match.group())

match = re.search(r"\w{2} s",a)
print(match.group())
