''' Q-2 -> .  You have been given 3 integers - l,r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print  these numbers, You just have to find their count.

Input ->  The first and only line of input contains 3 space separated integers l, r and k . 

Output ->  Print the required answer on a single line.
'''
print("Enter the value l , r and k : ")
l, r, k = input().split()
l = int(l)
r = int(r)
k = int(k)

count = 0
for i in range(l,r+1): 
    if(i%k == 0):
        count += 1
        
else:
    print(count)


