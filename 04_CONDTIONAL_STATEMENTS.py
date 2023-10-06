#  CONDITIONAL STATEMENT : ----------

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

# IF STATEMENT : --------

if a > b:
    print(a)
    print("I am still inside the if condition.")

if (a > b):
    print(f"a is greater. {a}")
if (b > a): 
    print(f"b is greater. {b}")

# IF ELSE STATEMENT : ----------

if (a > b):
    print(a)
    print("I am still inside the if block.")
else:
    print("I am out of if condition.")

# IF - ELIF - ELSE STATEMENT : --------------

if (b > a):
    print(f"b={b} is greater than a={a}.")
elif (a == b):
    print(f"a={a} and b={b} is equal.")
else:
    print(f"a={a} is greater than b={b}.")

# i. short hand if : ---------

print("A") if a > b else print("=") if a == b else print("B")

# NESTED - If - else : ---------------------

x = int(input("Enter a number  : "))
if x > 10:
    print(f"Your Number is above ten = {x}")
    if x > 20:
        print(f"and also above 20 !. = {x}")
        if x > 30:
            print(f" and really , it's also greater than 30. = {x} ")
        else:
            print(f"But not greater than 30. = {x}")
    else:
        print(f"but not above than 20 !. = {x} ")

else:
    print("Small than 10. ")
    if x < 5:
        print(f"And also smaller than 5. = {x}")
        if x < 0:
            print(f"This is a negative number. {x}.")
        else:
            print(f"It's not a negative number  =  {x}")
    else:
        print(f"But not smaller than 5. {x}")


print("Outside all if else statement.")
