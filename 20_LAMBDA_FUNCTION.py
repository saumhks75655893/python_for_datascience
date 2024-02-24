# import pandas as pd
import math

#  Lambda function is also a user - defined function but ananymous.


def add(x): return x * 200
print(add(4))

print((lambda a, b: a * b)(5, 7))


def product(x, y, z): return x * y * z


print(product(z=4, x=10, y=4))


def add(x, y=15, z=24): return x + y + z


print(add(20))

addition = lambda *args: sum(args)
print(addition(20, 30, 5, 28, 4, 50, 67, 89))

def higher_ord_fun(x, fun): return x + fun(x)


print(higher_ord_fun(20, lambda x: x * x))

print((lambda x: x % 2 and 'odd' or 'even')(13))

print((lambda string : string in "Welcome to Python Functions tutorial")('To'))

# filter function :-----------

''' filter(function, iterable) '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, list1)))

list1 = [10,20,30,40, 45, 60, 35, 67]
divide = list(filter(lambda x : (x % 4 == 0) , list1))
print(divide)




# map function : --------

list2 = [1, 2, 3, 4]
print(list(map(lambda x: x**2, list2)))

list1 = [10,20,4, 345, 53, 12]
doudle_the_num = list(map(lambda x : x // 2, list1))
print(doudle_the_num)


#  reduce funtion : ------

from functools import reduce

list4 = [10,20,30,40,50]
sum = reduce((lambda x, y : x+y), list4)
print(sum)
product = reduce((lambda x, y : x * y ), list4)
print(product)

# other examples : ----

def quadratic(a,b,c):
    return lambda x : a*x**2 + b*x + c
f = quadratic(4,5,6)
print(f(1))

# df = pd.DataFrame(
#     {"name": ["IBRAHIM", "SEGUN", "YUSUF", "DARE", "BOLA", "SOKUNBI"],
#      "score": [50, 32, 45, 45, 23, 45]
#      }
# )
# df["  lower_name  "] = df["name"].apply(lambda x: x.lower())
# print(df)

# print(pd.__version__)
