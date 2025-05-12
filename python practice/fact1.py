def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 and 1 is 1
        return 1
    return n * factorial(n - 1)  # Recursive case

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
