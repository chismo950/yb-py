class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hi, I'm {self.name}, {self.age} years old."


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        # Initialize name and age using the parent (Person) constructor
        # super() calls the parent class Person's __init__ method
        # to initialize inherited attributes name and age
        # Purpose: Let the parent class handle its own attribute initialization.
        # If the parent class adds new initialization logic in the future,
        # child classes using super() will automatically inherit these changes.
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self) -> str:
        # Override introduce() to include student_id
        return f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}."

# Demonstration:
if __name__ == "__main__":
    student = Student(name="John", age=20, student_id="1234")
    print(student.introduce())
    # Expected output:
    # Hi, I'm John, 20 years old, and my student ID is 1234.



