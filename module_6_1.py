class Animal: #Родительский класс
    alive = True    # (живой)
    fed = False     # (накормленный)
    def __init__(self, name): # (Индивидуальное название каждого животного)
        self.name = name

class Plant: #Родительский класс
    edible = False  # (съедобность)
    def __init__(self, name): # (индивидуальное название каждого растения)
        self.name = name

# Создаём унаследованный класс животных - Травоядные
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

# Создаём унаследованный класс животных - Хищники
class Predator(Animal):

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

# Унаследованный класс растений - Цветы
class Flower(Plant):
    pass
 # edible = True

# Унаследованный класс растений - Фрукты
class Fruit(Plant):
    edible = True


# Ввод названий животных и растений
animal1 = Predator('Волк с Уолл-Стрит')
animal2 = Mammal('Хатико')
plant1 = Plant('Цветик семицветик')
plant2 = Fruit('Заводной апельсин')

# Вывод результата
print(animal1.name)
print(plant1.name)

print(animal1.alive, f'- {animal1.name} живой')
print(animal2.fed, f'- {animal2.name} голоден')

animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive, f'- {animal1.name} помер')
print(animal2.fed, f'- {animal2.name} сыт')