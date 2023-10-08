# String Conversion types : ---------

# this will print hello without single inverted comma
print(f"a = %s" % "Hello")
print(f"b = %r" % "Hello")  # this will print hello with single inverted comma.
# this will also print hello with single inverted comma.
print(f"c = %a" % 'Hello')

# Widht specifier : -----------

print(f"a = %15s" % 'Himanshu kumar')


a = "Himanshu kumar"
b = " is a student"
c = a + b

print(f'Sum of {a!s:10} and {b!a:10} is : \n{c!r:10}')
