class House: #"Класс" Дом с этажами

    houses_history = [] #Атрибут хранит список имен всех созданных объектов класса House

    def __new__(cls, *args, **kwargs): #Создание нового экземпляра класса.
        instance = object.__new__(cls)
        args = args[0]
        cls.houses_history.append(args) #Добавляет имя дома в houses перед вызовом конструктора _init_
        return instance

    def __init__(self, name, number_of_floors): #конструктор класса, принимает имя дома и кол-во этажей
        self.name = name
        self.number_of_floors =  number_of_floors


    def go_to(self, new_floor): #Метод, который указывает, на какой этаж надо перейти
        if 1 <= new_floor <= self.number_of_floors: #Находится ли new_floor в диапазоне от 1 до кол-во этажей
           for floor in range(1, new_floor + 1): #Если да то идет от 1 до new_floor + 1
                print(floor)

        else: #Если new_floor превышает кол-во этажей дома, выводит сообщение
            print('Такого этажа не существует')

    def __del__(self): #Деструктор, вызывается при удалении объекта
        return print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)