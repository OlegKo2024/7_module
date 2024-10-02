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

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def add(self, *products):
        existing_products = [line.split(',')[0] for line in self.get_products()]  # Получаем имена существующих продуктов
        with open(self.__file_name, 'a') as file:
            for item in products:
                if item.name not in existing_products:
                    file.write(f'{item}\n')
                else:
                    print(f'Продукт {item.name} уже есть в магазине')

# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

# Выводим все продукты
for product in s1.get_products():
    print(product.strip())  # Используем strip() для удаления лишних пробелов и переносов