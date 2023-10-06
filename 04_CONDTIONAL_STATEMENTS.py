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

# NESTED - IF : ---------------------

x = int(input("Enter a number  : "))
if x > 10:
    print("Your Number is above ten, ")
    x = int(input("Enter a number  : "))
    if x > 20:
        print("and also above 20 !.")
    else:
        print("but not above than 20 !. ")
