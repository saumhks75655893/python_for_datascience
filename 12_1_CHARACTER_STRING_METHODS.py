# ---------------------------------: CHARACTER STRING METHODS : ---------------------------------------- #

#  1. capitalize() -

s = "I AM GOING TO HOME."

n = s.capitalize()
print(n)

n = s.casefold()  # same as lower
print(n)

r = s.lower()
print(r)

s = 'abcd'
print(s.islower())

s = 'himanshu kumar'
r = s.upper()
print(r)

s = 'HIMAN'
print(s.isupper())

s = "Himanshukumar"
print(s.isalpha())

s = "Himanshu34534asdfasdf"
print(s.isalnum())


s = "HIMANshu KUmar"
r = s.swapcase()  # uper to lower and lower to upper
print(r)

s1 = "3"
s2 = "3^6"
s3 = "10^-19"
s4 = "9^1/2"

print(s1.isdecimal())
print(s1.isdecimal())
print(s1.isdecimal())
print(s1.isdecimal())

print("\n\n")
print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())
print(s4.isdigit())

print("\n\n")
print(s1.isnumeric())
print(s2.isnumeric())
print(s3.isnumeric())
print(s4.isnumeric())
print("\n\n")
