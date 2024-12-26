# Modulo operators will return the remainder of a division operation
# The modulo operator is represented by the percentage sign (%)

# Examples
example1 = 10 % 2  # THis equals 0 because 10 is divisible by 2 with no remainder
example2 = 10 % 3  # This equals 1 because 10 divided by 3 equals 3 with a remainder of 1
example3 = 10 % 4  # This equals 2 because 10 divided by 4 equals 2 with a remainder of 2
example4 = 10 % 5  # This equals 0 because 10 is divisible by 5 with no remainder

# Odd or even
number = int(input("Which number do you want to check? "))
is_even = number % 2 == 0  # All even numbers are divisible by 2
if is_even:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
