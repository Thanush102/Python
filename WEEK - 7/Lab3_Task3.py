def sum_of_digits(n):
    if n==0:
        return 0
    return n%10+sum_of_digits(n//10)
def reverse_number(n, reversed_n=0):
    if n == 0:
        return reversed_n
    return reverse_number(n // 10, reversed_n * 10 + n % 10)

print("Sum of digits in number 458 is",sum_of_digits(458))
print("Reverse of digits in number 93672 is",reverse_number(93672))    

"""
Output:
Sum of digits in number 458 is 17
Reverse of digits in number 93672 is 27639
"""
