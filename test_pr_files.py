from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r')  # открыли файл
        read_file = file.read()  # считали содержимое файла
        file.close()
        return read_file

# Вот что происходит в коде:
# 1. **Открытие файла**: Сначала методом `open` открывается файл с именем, хранящимся в `self.__file_name`, для чтения
# 2. **Чтение содержимого файла**: Содержимое файла читается, а результат записывается в переменную `read_file`.
# Однако в данном случае вы используете функцию `pprint`, которая предназначена для удобного вывода данных на экран
# (но при этом не возвращает ничего), поэтому `read_file` будет равно `None`.
# 3. **Закрытие файла**: Файл закрывается с помощью `file.close()`, что является хорошей практикой, чтобы не оставлять
# открытые файловые дескрипторы.
# 4. **Возврат результата**: Оператор `return read_file` возвращает значение переменной `read_file`.
# Так как `pprint` ничего не возвращает, `read_file` будет равно `None`. В результате функция `get_products`
# будет возвращать `None`.
# Если вы хотите вернуть содержимое файла (например, в виде строки), вы должны заменить `pprint(file.read())` на
# просто `file.read()`. В итоге код может выглядеть так:

    def add(self, *products):
        file = open(self.__file_name, 'a')
        scanned_file = self.get_products()
        for item in products:
            if item.name not in scanned_file:
                file.write(f'\n{item}')
            else:
                print(f'Продукт {item.name} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#
print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

s1.get_products()