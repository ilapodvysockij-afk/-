class IterableGenerator:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        current = 0
        while current < self.limit:
            yield current
            current += 1

my_iterable = IterableGenerator(5)

generator_object = iter(my_iterable)
print(f"Тип повернутого об'єкта: {type(generator_object)}")

print("Елементи генератора:")
for number in my_iterable:
    print(number)
