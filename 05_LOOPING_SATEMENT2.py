#  ----------------  :  LOOPING STATEMENT  :  --------------------#

# 2. FOR LOOP :---------------

l = []
print("[",end='')
for i in range(10):
    print(i, end=', ')
   
    l.append(i**2)
print("]")

print(l)