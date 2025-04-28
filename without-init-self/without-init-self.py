class Factorial:
    @staticmethod
    def factorial(n):  # Factorial method now works with self.num1
        result = 1  # Initialized before the loop to store the product.
        for i in range(1, n + 1):
            result *= i
        return result
    @staticmethod
    def check_Prime(n):  # Prime check method added
        if n < 2:  # 0 and 1 are not prime numbers
            return False
        for i in range(2, int(n ** 0.5) + 1): # Check up to the square root of num1 and int to make it not show decimal values
            # Check if num1 is divisible by i 
            if n % i == 0:
                return False
        return True
    @staticmethod
    def display(n):  # Display method corrected
        print("Factorial of", n, "is", Factorial.factorial(n))
        if Factorial.check_Prime(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")
 
# Instantiate the class
number1 = Factorial()
 
# Call the display method to show the result
number1.display(10)

Factorial.display(5) # plus: this also working for staticmethod

# about static method: https://docs.python.org/3/library/functions.html#staticmethod