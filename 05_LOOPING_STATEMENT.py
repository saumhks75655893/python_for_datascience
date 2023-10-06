#  ---------------: LOOPING STATEMEN : ------------------- #

# 1. while loop : ------------

n = int(input("Max iterations : "))
i = 1
while (i <= n):
    print(f"This is iteration number,  {i}  and the answer is  =  {i**2}")
    i += 1

# print even from n numbers

n = int(input("Enter the number : "))
i = 1
j = 1
while i <= n:
    if i % 2 == 0:
        print(f"Evan number {j}  is => {i}")
        j += 1
    else:
        pass
    i += 1

#  BREAK AND CONTINUE STATEMENT : --------------

i = 1
while True:
    if i % 17 == 0:
        print("Inside if.")
        break
    else:
        print("Inside else")
    i += 1


print("done")

n = 10
i = 1
while i <= n:
    if i % 9 != 0:
        print("Inside if.")
        i += 1
        continue
    print("Something")
    print("Somethingelse")
    i += 1


print("done")
