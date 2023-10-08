# # String Conversion types : ---------

# print(f"a = %s"%"Hello") # this will print hello without single inverted comma
# print(f"b = %r"%"Hello") # this will print hello with single inverted comma.
# print(f"c = %a"%'Hello') # this will also print hello with single inverted comma.

# # Widht specifier : -----------

# print(f"a = %17s"%'Himanshu kumar')

# #  The .<precision> Specifier : --------------

# print(f"a = %.5f" % 6.5)
# print(f"c = %.2c"% 'A')
# print(f"d = %.5s"%'Hello')

# Conversion The flags ( # , +, -, 0, ' ') : ---------

''' # -> It works with only octal and hexadecimal numbers. '''

print(f'%o'%65)
print(f'%#o'%65)
print(f'%x'%65)
print(f'%#x'%65)

''' 0 - causes padding with '0' in numbers'''
print(f"%05d"%221)
print(f"%05d"%21)
print(f"%05d"%1)

''' The - tag - When a formatted value is shorter than the speicfied field width, it is usually right-justified.'''

print(f"%-5d"%221)
print(f"%-5d"%21)
print(f"%-5d"%1)

''' The + flag and ' '  -  By default numeric value do not have a leading sign character. The + flag add '+' character to the left of numeric output. '''

print(f"%+d"%221)
print(f"%+d"%21)
print(f"%+d"%-1)
print("\n")
print(f"% d"%221)
print(f"% g"%21)


