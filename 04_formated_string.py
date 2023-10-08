#  ----------- : FORMATING : ---------- #

a = 10
b = 19
print(f" a = %d and b = %d"%(a,b))


print(f"a = {a} and b  = {b}.")
print(f"a = {a} and b  = {b}.")

# Widht specifier : -----------

print(f"a = %15s"%'Himanshu kumar')
print(f"a = %10d"%50)
print(f"c = %10g" % 120.32)

#  The .<precision> Specifier : --------------

print(f"a = %.5f" % 6.5)
print(f"c = %.2c"% 'A')
print(f"d = %.5s"%'Hello')

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

