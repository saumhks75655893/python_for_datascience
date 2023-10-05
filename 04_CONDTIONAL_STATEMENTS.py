#  CONDITIONAL STATEMENT : ----------

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

# IF STATEMENT : --------

# if a>b: 
#     print(a)
#     print("I am still inside the if condition.")

if a>b:
    print(f"a is greater. {a}")
if b>a:
    print(f"b is greater. {b}")

# IF ELSE STATEMENT : ----------

if a>b: 
    print(a)
    print("I am still inside the if block.")
else:
    print("I am out of if condition.")