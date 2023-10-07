''' Problem statement : -   
         Given a list of number i.e. [1,2,4,-5,7,9,3,2], make antherlist that contains all the items in sorted order from min to max. i.e. your result will be another like [-5,1,2,2,3,7,9]'''

l = [1, 2, 4, -5, 7, 9, 3, 2]
for j in range(len(l)):
    m = l[j]
    idx = j
    c = j
    for i in range(j, len(l)):
        if l[i] < m:
            m = l[i]
            idx = c
        c += 1
    temp = l[j]
    l[j] = m
    l[idx] = temp

print(l)

# another way : -------

for i in range(len(l)):
    for j in range(i+1,len(l)): 
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print(l)