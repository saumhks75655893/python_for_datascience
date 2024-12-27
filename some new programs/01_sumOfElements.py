# SUM OF ELEMENTS
# if the total digits of the result is greater than 1 digit then do the process again till the result is in 1 digit.

def sum(n):
    while n >= 10:
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum += digit
            n //= 10
        n = total_sum
    return n


n = int(input("Enter the number : "))
sum_of_digits = sum(n)

print(f"Sum of the digits of {n} : ", sum_of_digits)
