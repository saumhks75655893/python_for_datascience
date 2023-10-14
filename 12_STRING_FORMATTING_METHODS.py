#  ------------------------------------  : STRING FORMATTING METHODS  : -------------------- #

s = 'Hello'
r = s.ljust(10, '*')
print(r)

print("\n\n")
r1 = s.rjust(10)
print(r1)

print("\n\n")
s = "hello"
r = s.center(20, "*")
print(r)

print("\n\n")

s1 = "Shaumya sinha\t1200000000Rs"
s2 = "Himanshu kumar\t8000000Rs"

print(s1.expandtabs(20))
print(s2.expandtabs(20))

print("\n\n")

