print('Задача "Учёт товаров"')
# Вы почти справились с заданием, однако ваш код требует доработки:
# - класс Shop не должен наследоваться от класса Product.
# - ваш метод get_products не возвращает никакого значения, что по умолчанию означает None. По заданию он должен
# возвращать (return) единую строку со всеми товарами из файла __file_name.
# - при проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
# - также у вас в файле записывается первая строка пустая.
# Прошу доработать и направить решение повторно.

from pprint import pprint
class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую
# строку со всеми товарами из файла __file_name.

    def get_products(self):
        file = open(self.__file_name, 'r')    # открыли файл
        read_file = file.read()               # считали содержимое файла
        file.close()
        return read_file

# Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'
    def add(self, *products):
        file = open(self.__file_name, 'a')
        scanned_file = self.get_products()
        for item in products:
            if item.name not in scanned_file:
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