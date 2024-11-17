from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        self.file = open(self.__file_name, 'r')
        products = self.file.read()
        self.file.close()
        return products

    def add(self, *products):
        new_products = self.get_products()
        self.file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in new_products:
                self.file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине')
        self.file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

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
