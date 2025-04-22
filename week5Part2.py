class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        return "Running"

class Bird(Animal):
    def move(self):
        return "Flying"

class Fish(Animal):
    def move(self):
        return "Swimming"

# Demonstrate polymorphism
def show_movement(objects):
    for obj in objects:
        print(obj.move())

# Create instances
animals = [Dog(), Bird(), Fish()]

print("ANIMALS MOVING:")
show_movement(animals)
