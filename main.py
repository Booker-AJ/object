from enums.Sex import Sex
from models.Animal import Animal

tree = Animal(age=4, name='Tree', sex=Sex.OTHER)
otter = Animal(32, 'Bret', Sex.MALE)

animals = [tree, otter]

for animal in animals:
    print(f"{animal.name} is age {animal.age}")
    animal.speak()
