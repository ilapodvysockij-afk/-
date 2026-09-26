class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Якийсь звук"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Гав!"


# Підклас Кіт
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        return "Мяу!"



my_dog = Dog("Рекс", "Вівчарка")
my_cat = Cat("Мурчик", "Рудий")

print(f"Собака {my_dog.name} ({my_dog.breed}) каже: {my_dog.make_sound()}")
print(f"Кіт {my_cat.name} ({my_cat.color}) каже: {my_cat.make_sound()}")
