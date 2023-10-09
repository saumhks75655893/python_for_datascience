#  ----------------  :  LOOPING STATEMENT  :  --------------------#

# 2. FOR LOOP :---------------

print("\n","*"*40)
print("    -------  Simple for Loop for list ------- ")
print("*"*40,"\n")
l = []
print("[", end='')
for i in range(11):
    print(i, end=', ')

    l.append(i**2)
print("]")

print(l)

#  FOR LOOP WITH ELSE : -------------

print("\n", "*"*40)
print("    -------   for Loop with else and set ------- ")
print("*"*40, "\n")
s = {"apple", 4.9, "cherry"}


i = 0
for x in s:
    print(x)
    i += 1
    if i == 3:
        break
    else:
        pass
else:
    print("Loop completes its iterations.")
print("Outside the loop.")

# FEW EXPLORAION ON DICTIONARY : -----------
print("\n","*"*40)
print("    -------   for Loop with dictionary  ------- ")
print("*"*40, "\n")
d = {"apple": 44, "cherry": 30}
for i in d:
    print(f"The number of '{i}' is '{d[i]}' ")
    
    
# A PROGRAM :-------------

x = 4
y = 0
while x>=0: 
    x -= 1
    y += 1
    if x == y:
        continue
    else:
        print(x, y)

#  Prime Number program : ---------
print("*"*70)
print("Prime Number Program ")
print("*"*70)

n = int(input("Enter a number : "))
flag = 0
for i in range(2,n):
    if n%i == 0:
        flag = 1
        break

if flag == 1: 
    print(f"{n} Not a prime number.")
else:
    print(f"{n} is a prime number.")

#  ELSE and BREAK WITH FOR LOOP :------------------
print("*"*70)
print("ELSE and BREAK WITH FOR LOOP")
print("*"*70)


n = int(input("Enter the value of n : "))

for i in range(2,n):
    print(f"Position is : {i}")
    if i == 7: 
        break
else:
    print("out the loop statement.")

#  ELSE and CONTINUE WITH FOR LOOP :------------------

print("*"*70)
print("ELSE and CONTINUE WITH FOR LOOP")
print("*"*70)


n = int(input("Enter the value of n : "))

for i in range(2,n):
    print(f"Position is : {i}")
    if i == 7: 
        continue
else:
    print("Out of the for loop body.")
