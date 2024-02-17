num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

operator = input("Enter operator : ")

match operator: 
    case "+":
        print(f"Sum of {num1} and {num2} is {num1 + num2}")
    case "-":
        print(f"substraction of {num1} and {num2} is {num1 - num2}" )
    case "*":
        print(f"Multiplication of {num1} and {num2} is {num1 * num2}" )
    case "/":
        print(f"Devision  of {num1} and {num2} is {num1 / num2}" )
    case _: 
        print("Enter a valid operator...")