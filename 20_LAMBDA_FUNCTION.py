#  Lambda function is also a user - defined function but ananymous.

import pandas as pd
x = 4
print(lambda x: x*2)

# filter function :-----------

''' filter(function, iterable) '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# find the even number using lambda function

print(list(filter(lambda x: x % 2 == 0, list1)))


# map function : --------

list2 = [1, 2, 3, 4]
print(list(map(lambda x: x**2, list2)))


df = pd.DataFrame(
    {"name": ["IBRAHIM", "SEGUN", "YUSUF", "DARE", "BOLA", "SOKUNBI"],
     "score": [50, 32, 45, 45, 23, 45]
     }
)
df["  lower_name  "] = df["name"].apply(lambda x: x.lower())
print(df)

print(pd.__version__)
