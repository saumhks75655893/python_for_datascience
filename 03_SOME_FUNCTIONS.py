# Some functions : ----------

# i.  round() function : ------------------

print("\n SOME IMPORTANT FUNCTION  \n")
print("\n ROUND FUNCTION  \n")

print(round(234.234234))
print(round(534.834))
print(round(4.423535434,3))


# ii. divmod(x,y) function : --------

print("\n DIVMOD FUNCTION  \n")

g = divmod(10,4)
print(g)
print(type(g))
print(divmod(10,5))
print(divmod(27,5))

# iii. isinstance() function : ---------

print("\n ISINSTANCE FUNCTION  \n")
print(isinstance(1, int))
print(isinstance(1.0, int))
print(isinstance(1.0, (int, float)))
print(isinstance(2+3j, (int, float, str, complex)))
   
  
# iv. pow(x,y,z) function : ---------

print("\n POWER FUNCTION  \n")

print(pow(2,3))
print(pow(16,2,3))

# v. input() function : -------

print("\n INPUT FUNCTION  \n")

a = input("Enter something : ")

