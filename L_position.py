import io
from pprint import pprint

name = 'products_00.txt'
file = open(name, 'a')
print(file.tell())      # 0
# Функция `file.tell()` используется для определения текущей позиции курсора (указателя места в файле) в открытом файле.
# Это значит, что метод возвращает позицию в байтах, где в данный момент располагается курсор, начиная отсчёт с нуля.
# pprint(file.read())   # нельзя читать в режиме добавления
print(file.tell())
file.seek(5)            # в режиме 'a' курсор всегда будет находиться в конце текста
file.write('\nmy')

# Проблема, с которой вы столкнулись, связана с тем, что вы открываете файл в режиме `append` (`'a'`). В этом режиме
# указатель всегда перемещается в конец файла, и любые операции записи будут происходить именно там, независимо от
# того, где вы находитесь в файле.
# Для того чтобы установить курсор в нужное место, нужно открыть файл в режиме чтения и записи (`'r+'`).
# В этом режиме вы можете перемещаться по файлу, читать его содержание и писать в любую позицию. П
# Пример:
# name = 'products_00.txt'
# # Открываем файл в режиме чтения и записи
# file = open(name, 'r+')  # Теперь мы можем и читать, и писать
# print(file.tell())  # Позиция курсора в начале файла, будет 0
# print(file.read())  # Чтение содержимого файла
# file.seek(5)  # Перемещаем курсор на 5 байт
# file.write('\nmy')  # Записываем текст в указанную позицию
# file.close()  # Не забываем закрыть файл

name = 'products_01.txt'
file = open(name, 'w')
print(file.tell())
file.write('Это новый файл \nПроверяем работу курсора')
print(file.tell())
file.close()

# не смогли прочитать используя encoding='UTF-8', так как записано по умолчанию в другом формате
# введем текст руками

# name = 'products_01.txt'
# file = open(name, 'r', encoding='utf-8')
# file.seek(0)
# print(file.read())
# print(file.tell())
# print(file.read())

name = 'products_01.txt'
file = open(name, 'r')
print(file.readable())
print(file.writable())
print(file.seekable())
print(file.read())
print(file.tell())
file.seek(0)
print(file.tell())

print(file.name)        # products_01.txt
print(file.buffer)      # <_io.BufferedReader name='products_01.txt'>
print(file.close)       # <built-in method close of _io.TextIOWrapper object at 0x000001CD48B2D700>
file.close()
