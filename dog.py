# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Woof!")
my_dog = dog.Dog("Rex", "SuperDog")
my_dog.breed = "SuperDog"
my_dog.bark()
print(my_dog.breed)
print(my_dog.name)
