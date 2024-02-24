from functools import reduce

a = [12,4,4,4,4,65,456]
sum = reduce((lambda x,y: x+y),a)
print(sum)