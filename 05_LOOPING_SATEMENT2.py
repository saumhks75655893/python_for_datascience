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
