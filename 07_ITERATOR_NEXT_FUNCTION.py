s = "Hello"
I = iter(s)

# String iterator cann't run directly by using print.

s1 = str(I)
print(s)
print(type(s))
print(type(I))
print(type(s1))

l = len(s)
while True:
    try:
        print(next(I))
    except StopIteration:
        print("Finish.....")
        break


print(s.lower())
print(s.upper())
