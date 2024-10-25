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


h1 = House('ЖК Эльбрус', 30)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)