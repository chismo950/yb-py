# Parent class (also called base class or superclass)
class Animal:
    def __init__(self, name):
        # Parent constructor - initializes common attributes for all animals
        self.name = name

    def speak(self):
        # Parent method - provides default behavior for all animals
        print(f"{self.name} makes a sound.")


# Child class (also called derived class or subclass)
# The syntax "class Dog(Animal):" means Dog inherits from Animal
class Dog(Animal):
    # Dog inherits ALL attributes and methods from Animal
    # This means Dog automatically gets:
    # - __init__(self, name) method
    # - name attribute
    # - speak() method (though we override it below)
    
    def speak(self):
        # Method Overriding: Child class provides its own implementation
        # This overrides the parent class's speak() method
        print(f"{self.name} barks.")

    def fetch(self, item):
        # Additional method specific to Dog class
        # This extends the functionality beyond what Animal provides
        print(f"{self.name} fetches the {item}.")


# Another child class inheriting from the same parent (Hierarchical Inheritance)
class Cat(Animal):
    # Cat also inherits ALL attributes and methods from Animal
    # This demonstrates hierarchical inheritance - multiple classes inherit from one parent
    
    def speak(self):
        # Method Overriding: Cat provides its own implementation
        # This overrides the parent class's speak() method differently than Dog
        print(f"{self.name} meows.")

    def climb(self):
        # Additional method specific to Cat class
        # This extends the functionality beyond what Animal provides
        print(f"{self.name} climbs the tree.")


if __name__ == "__main__":
    # Demonstrate single inheritance behavior
    
    # Create an Animal instance and call its method
    generic_animal = Animal("GenericAnimal")
    generic_animal.speak()   # Output: GenericAnimal makes a sound.

    # Create a Dog instance (child of Animal)
    # Dog inherits Animal's __init__ method, so we can pass just the name
    my_dog = Dog("Buddy")
    
    # Call overridden method - uses Dog's version, not Animal's
    my_dog.speak()           # Output: Buddy barks.
    
    # Call Dog-specific method (not available in parent Animal class)
    my_dog.fetch("ball")     # Output: Buddy fetches the ball.

    # Create a Cat instance (another child of Animal)
    # Demonstrates hierarchical inheritance - both Dog and Cat inherit from Animal
    my_cat = Cat("Whiskers")
    
    # Call overridden method - uses Cat's version, not Animal's or Dog's
    my_cat.speak()           # Output: Whiskers meows.
    
    # Call Cat-specific method
    my_cat.climb()            # Output: Whiskers climbs the tree.
    
    # Hierarchical inheritance allows multiple child classes to inherit from one parent
    # Each child can have unique behaviors while sharing common parent features




