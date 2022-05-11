from enums.Sex import Sex


class Animal:
    age: int
    name: str
    sex: Sex

    def __init__(self, age, name, sex):
        self.age = age
        self.name = name
        self.sex = sex

    def speak(self):
        print('skwaa')
