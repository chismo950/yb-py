input_n = int(input("Enter a positive integer: "))
if input_n < 0:
    print("Factorial is not defined for negative numbers")
    exit(1)
def factorial(n: int) -> int:
    print(n)
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(f"factorial of {input_n} is", factorial(input_n))