# WAP to convert a float point number into integer number and check this integer number is even or odd. 

x = float(input("Enter a real number : "))
y = round(x)

if x > 0:
    if y > x:
        inPortion = y - 1

    else:
        inPortion = y

else:
    if y < x:
        inPortion = y + 1

    else:
        inPortion = y

if inPortion > 0:       
    if inPortion%2 == 0: 
        print(f"Even number =  {inPortion}")
    else:
        print(f"Odd number = {inPortion}")
else: 
    if inPortion%2 == 0: 
        print(f"Negative Even number =  {inPortion}")
    else:
        print(f"Negative Odd number = {inPortion}")
