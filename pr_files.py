print('Режимы открытия файлов')
from pprint import pprint
class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):

    def __init__(self):
        self.__file_name = 'products.txt'

# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую
# строку со всеми товарами из файла __file_name.

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()

# Метод add(self, *products), который принимает неограниченное количество объектов класса
# Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
    def add(self, *products):
        file = open(self.__file_name, 'a')
        for item in products:
            if item.name not in self.__file_name:
                file.write(f'\n{item}')
            else:
                print(f'Продукт {item.name} уже есть в магазине')
        file.close()


# Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
# При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
# Не забывайте закрывать файл вызывая метод close() у объектов файла.

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())