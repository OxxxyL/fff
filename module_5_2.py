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


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#__str__
print(str(h1))
print(str(h2), '\n')
#__len__
print(len(h1))
print(len(h2))