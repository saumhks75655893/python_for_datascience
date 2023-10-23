#  ----------------------------- : MATRIX IN PYTHON : ---------------------------------------   #

a = [[1,2,3],[4,5,6],[7,8,9]]
sum = 0
for i in range(3):
    for j in range(3):
        print(a[i][j], end='  ')
        sum = sum + a[i][j]
    print()
    
print("Sum of the element of the matrix is : " , sum)