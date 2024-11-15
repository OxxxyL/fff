class Shop:
    __file_name = 'products.txt' # Инкапсулированный атрибут с файлом продуктов.


    def get_products(self):
        file1 = open(self.__file_name, 'r') # Открывает файл в режиме чтения
        product = file1.read() # Считывает содержимое файла и возвращает
        file1.close()
        return product # После чтения файл закрывается

    def add(self, *products): # Метод что-бы добавлять продукты в файл
        file = open(self.__file_name, 'r+') # Открываем в режиме чтения и записи
        for el in products:
            if str(el) in self.get_products(): # Проверяет, есть ли он уже в списке продуктов
                print(f"Продукт {str(el)} уже есть в магазине") # Если в файле есть продукты - вывод сообщения
            else:
                file.write(str(el) + '\n') # Если продукта нет, добавляет в файл, в новую строку
        file.close() # После завершения записи файл закрывает


class Product(Shop):
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self): # Для удобного формата
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# 1 запуск
#Spaghetti, 3.4, Groceries
#Potato, 50.5, Vegetables
#Spaghetti, 3.4, Groceries
#Potato, 5.5, Vegetables

# 2 запуск
#Spaghetti, 3.4, Groceries
#Продукт Potato, 50.5, Vegetables уже есть в магазине
#Продукт Spaghetti, 3.4, Groceries уже есть в магазине
#Продукт Potato, 5.5, Vegetables уже есть в магазине
#Potato, 50.5, Vegetables
#Spaghetti, 3.4, Groceries
#Potato, 5.5, Vegetables

# Файл после запуска
#Potato, 50.5, Vegetables
#Spaghetti, 3.4, Groceries
#Potato, 5.5, Vegetables
