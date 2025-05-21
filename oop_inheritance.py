# Parent class
class Dog:
    # class attribute
    age = 20
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        print(f"{self.name} is {self.age} years old")
    
    def speak(self, sound="from parent class"):
        print(f"{self.name} says {sound}")

    def greet(self):
        print("hello from parent")

# Child class
class bulldog(Dog):
    def speak(self, sound="bulldo says"):
        print(f"{self.name} say {sound}")

# Child class
class chizou(Dog):
    def sen(self):
        # Inherit from parent 
        super().greet()
        

# instance object
ally = chizou("ally", 5)


# output: <class '__main__.bulldog'>
print(type(ally))

# output: True
print(isinstance(ally, bulldog))

# output: True
print(isinstance(ally, Dog))

# output: ally say grrrr
print(ally.speak("grrrr"))

# output: ally say ohhhhhhhh
print(ally.speak())

# output: hello from parent
print(ally.sen())

# output: 20
print(Dog.age)

