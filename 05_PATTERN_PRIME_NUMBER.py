#  You are given an integer N. You need to print the series of all prime number till N.

n = int(input("Enter the number : "))

flag = 0
i = 2
while (i <= n):
    for var in range(2, i):
        if (i % var == 0):
            flag = 1
            break

    if (flag == 0):
        print(i, end=' ')

    i = i + 1