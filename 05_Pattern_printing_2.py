# PATTERN PRINTING PART -2 : -----------

'''
        1
      1 2 3
    1 2 3 4 5 
  1 2 3 4 5 6 7
      
'''
print("\n Sixth pattern : ----------\n")

n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    print(" " * (n-i), end="")
    for j in range(1,(2*i - 1) + 1): 
        print(j, end="")
    print()