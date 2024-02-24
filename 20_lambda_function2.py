# 1. Print the adults which is greater than 18 
age = [8,10,24,18,20,22,37]

adults = list(filter(lambda a: a>18, age))

print(adults)

# 2. check the given list's how much element is even and how is odd

a = [2,4,1,3,4,15,23,16,20,21, 25]

evenOdd = list(filter(lambda  a ,b : a%2==0, a))
print(evenOdd)