class House: #"Класс" Дом с этажами
    def __init__(self, name, number_of_floors): #конструктор класса, принимает имя дома и кол-во этажей
        self.name = name
        self.number_of_floors =  number_of_floors

    def go_to(self, new_floor): #Метод, который указывает, на какой этаж надо перейти
        if 1 <= new_floor <= self.number_of_floors: #Находится ли new_floor в диапазоне от 1 до кол-во этажей
           for floor in range(1, new_floor + 1): #Если да то идет от 1 до new_floor + 1
                print(floor)

        else: #Если new_floor превышает кол-во этажей дома, выводит сообщение
            print('Такого этажа не существует')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors
    def __eq__(self, other):    #должен возвращать True, если количество этажей одинаковое у self и у other.
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):    #
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value): #Добавляем целое число к кол-ву этажей
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self #увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.

    def __radd__(self, value): #Поддержка сложений + и +=
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self #работают так же как и __add__ (возвращают результат его вызова).
#функции isinstance:
#isinstance(other, int) - other указывает на объект типа int.
#isinstance(other, House) - other указывает на объект типа House.

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

print(h1.__add__(10))
print(h1 == h2)
print(h1.__add__(10))
print(h2.__add__(10))
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
