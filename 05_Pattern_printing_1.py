'''
**********
'''
print("First pattern : --------- \n")
for i in range(1):
    print("*" * 10)
'''
 ******
 ******
 ******
 ******
'''
print("\nSecond Pattern : ---------- \n")
for i in range(5):
    print("* " * 5)

'''
12345
12345
12345
12345
12345
'''

print("\n Third pattern : ----------\n")

n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end='')
    print("\t")

'''
1
1 2
1 2 3
1 2 3 4
'''
print("\n Fourth pattern : ----------\n")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()

'''
1
2 2
3 3 3
4 4 4 4
'''

print("\n Fifth pattern : ----------\n")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

#SOME BASIC PROBLEM : ------------

print("\n SOME BASIC PROBLEM : ----------\n")
for i in ['red', 'blue']:
    for j in ['apple', 'banana']:
        print(f"{i} -->  {j}")

'''
1
2 3
4 5 6
7 8 9 10
'''
print("\n Sixth pattern : ----------\n")
r = int(input("Enter the number of rows : "))
# c = int(input("Enter the number of columns : "))
m = 1
for i in range(1,r+1):
    for i in range(1,i+1):
        print(m, end=" ")
        m += 1
    print()

'''
1 1 1 1 1
2 2 2 2 
3 3 3 
4 4 
5
'''
print("\n Seven'th pattern : ----------\n")
r = int(input("Enter the number of rows : "))
for i in range(1, r+1):
    for j in range(r+1, i, -1):
        print(i, end=" ")
    print()

'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
'''

print("\n Eight'th pattern : ----------\n")
r = int(input("Enter the number of rows : "))
for i in range(1, r+1):
    for j in range(r, i-1, -1):
        print(r-i+1, end=" ")
    print()

'''
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2
10 9 8 7 6 5 4 3
10 9 8 7 6 5 4
10 9 8 7 6 5 
10 9 8 7 6 
10 9 8 7
10 9 8 
10 9 
10
'''
print("\n Nine'th pattern : ----------\n")
r = int(input("Enter the number of rows : "))
for i in range(1, r+1):
    for j in range(r, i-1, -1):
        print(j, end=" ")
    print()

'''
1 2 3 4 5 
6 7 8 9 
10 11 12
13 14
15 
'''
print("\n Ten'th pattern : ----------\n")
r = int(input("Enter the number of rows : "))
m = 1
for i in range(1, r+1):
    for j in range(r+1, i, -1):
        print(m, end=" ")
        m += 1
    print()
