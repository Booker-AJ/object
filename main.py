from enums.Sex import Sex
from models.Animal import Animal

tree = Animal(age=4, name='Tree', sex=Sex.OTHER)

print(f"Tree is age {tree.age}")
tree.speak()
