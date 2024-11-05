class Vehicle: # Создаём класс транспорт
    __COLOR_VARIANTS = ['RED', 'GREEN', 'MAGENTA', 'BLUE', 'BLACK', 'WHITE'] # атрибут класса - цветовая гамма
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power
        self.owner = owner
    def get_model(self): # модель
        return self.__model
    def get_horsepower(self): # мощность двигателя
        return self.__engine_power
    def get_color(self): # цвет транспорта
        return self.__color
    def set_color(self, new_color: str): #принимает аргумент new_color(str),меняет цвет color на new_color
        if new_color.lower() in self.__COLOR_VARIANTS: #если он есть в списке COLOR_VARIANTS
            self.__color = new_color #Если в списке нету, выводит print
        else:
            print(f'Нельзя сменить цвет на {new_color}')
#Константные(постоянные) значения в Python писать капсом, как в случае списка цветов или количеством пассажиров.

    def print_info(self): # Метод print_info - распечатывает результаты методов
        print("Модель:", self.get_model())
        print("Мощность:", self.get_horsepower())
        print("Цвет:", self.get_color())
        print("Владелец:", self.owner)


class Sedan(Vehicle): # Класс Sedan - наследник класса Vehicle.
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Vladimir', 'Toyota Mark IV 2099', 'BLUE', 2099) #Текущие цвета

vehicle1.print_info() # Изначальные свойства

vehicle1.set_color('PINK') # Меняем свойства, но такого цвета нет в списке
vehicle1.set_color('BLACK') # Меняем свойства из списка
vehicle1.owner = 'Veronika' # Меняем владельца

vehicle1.print_info() #Итоговые свойства