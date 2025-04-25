input_n = int(input("Enter a number: "))
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(f"factorial of {input_n} is", factorial(input_n))