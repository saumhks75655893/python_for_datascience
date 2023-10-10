#  You are given an integer N. You need to print the series of all prime number till N.

n = int(input("Enter the number : "))

i = 2
while i<=n: 
    flag = 0
    for var in range(1, i+1):
        if (i % var == 0):
            flag += 1

    if (flag == 2):
        print(i, end=' ')
    i = i+1

