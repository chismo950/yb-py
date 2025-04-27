class Factorial:
    def input(self):
        self.n = int(input("Enter a positive integer: "))
        if self.n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return self.n

    def calculate(self):
        if self.n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        elif self.n == 0 or self.n == 1:
            return 1
        else:
            result = 1
            for i in range(2, self.n + 1):
                result *= i
            return result
    
    def isPirmeNumber(self):
        if self.n < 2:
            return False
        for i in range(2, self.n, 1):
            if self.n % i == 0:
                return False
        return True

factorial = Factorial()
factorial.input()
print(f"factorial of {factorial.n} is", factorial.calculate())
print(f"{factorial.n} is prime number?: {factorial.isPirmeNumber()}")