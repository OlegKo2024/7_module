print('Форматирование строк')
print('Меня зовут ' + 'Oleg')
print('Меня зовут %s' % 'Oleg')
print('Меня зовут %s, мне %s' % ('Oleg', 14))
print('Меня зовут %(name)s, мне %(age)s' % {'name': 'Oleg', 'age': 14})
print('I study at {}'.format('Urban'))
print('I study at {} {} my major is {}'.format('Urban', 'Uni', 'Python'))
print('I study at {0} {1} and by the way my major is {0}'.format('Urban', 'Uni', 'Python'))
print('I study at {title} {org} and my major is {title}'.format(title='Urban', org='Uni'))

print(f'This is the newest method, we can put any Python code in 3 times - {'HERE' * 3}')
print(f'This is the newest method, we can put any Python code in 3 times with spaces {" ".join(["HERE"] * 3)}')

'''
Когда стоит использовать метод «format» в отличие от урбан?
Например, в отдельном файле хранится текст. Там есть обозначения с фигурной F-строкой и фигурные скобки на месте 
которых будет браться значение из переменных. Но! Мы ее импортируем в основной файл и хотим использовать, но на тот 
момент в другом файле этой переменной не было. Возникнет ошибка. Использование метода «format». 
Вставляем импортированную строку и с помощью метода «format» подставляем значение переменных.
'''

print('Файлы в операционной системе')

import os

print('Текущая директория:', os.getcwd())       # где мы находимся
if os.path.exists('Newer'):                     # создание вложенной папки
    os.chdir('Newer')
else:
    os.mkdir('Newer')
    os.chdir('Newer')

print('Текущая директория:', os.getcwd())       # сейчас мы в: D:\PythonProjectUni\Module_07\Files_in_os\Newer

# os.makedirs(r'Newest\Last')                     # создали нескольких вложенных папок
print('Текущая директория:', os.getcwd())       # Текущая директория: : D:\PythonProjectUni\Module_07\Files_in_os\Newer

print(os.listdir())                             # одноуровневый список директорий ['Newer']

print('Текущая директория:', os.getcwd())

print('Обход 1')
directory = r'D:\PythonProjectUni\Module_07\Files_in_os'
for i in os.walk(directory):
    print(i)                                  # чтобы посмотреть всю вложенность

print('Обход 2')
# Обход каталога с os.walk - возвращает кортеж для каждой директории, где root - текущая директория,
# dirs - подкаталоги, а files - файлы в текущем каталоге
for root, dirs, files in os.walk(directory):
    print(f'{root} {dirs} {files}')

# D:\PythonProjectUni\Module_07\Files_in_os ['Newer'] ['L_the_rest.py', 'pr_files_in_os.py']
# D:\PythonProjectUni\Module_07\Files_in_os\Newer ['Newest'] []
# D:\PythonProjectUni\Module_07\Files_in_os\Newer\Newest ['Last'] []
# D:\PythonProjectUni\Module_07\Files_in_os\Newer\Newest\Last [] []

print('По заданию, вывод файлов и директорий')

for root, dirs, files in os.walk(directory):
    for file in files:                          # Внутренний цикл проходит по каждому файлу
        filepath = os.path.join(root, file)     # Формирует полный путь к файлу, объединяет путь и файл
        print(f'Обнаружен файл: {file}, Путь: {filepath}')
for dir in dirs:                                # Цикл проходит по каждой директории
        dirpath = os.path.join(root, dir)       # Формирует полный путь к директории, объединяет путь и директорию
        print(f'Обнаружена директория: {dir}, Путь: {dirpath}')

# Аргументы join(): Она принимает один или несколько аргументов:
# Первый аргумент — это базовый путь (например, путь к директории).
# Последующие аргументы — это имена файлов или папок, которые вы хотите добавить к этому пути.

# Обнаружен файл: L_the_rest.py, Путь: D:\PythonProjectUni\Module_07\Files_in_os\L_the_rest.py
# Обнаружен файл: pr_files_in_os.py, Путь: D:\PythonProjectUni\Module_07\Files_in_os\pr_files_in_os.py
# Обнаружена директория: Newer, Путь: D:\PythonProjectUni\Module_07\Files_in_os\Newer
# Обнаружена директория: Newest, Путь: D:\PythonProjectUni\Module_07\Files_in_os\Newer\Newest
# Обнаружена директория: Last, Путь: D:\PythonProjectUni\Module_07\Files_in_os\Newer\Newest\Last

print('Вывод списков')
print('Текущая директория:', os.getcwd())
print('Меняем директорию')
os.chdir(r'D:\PythonProjectUni\Module_07\Files_in_os')
print('Текущая директория:', os.getcwd())           # директория изменена
print(os.listdir())                                 # выводит все # ['L_the_rest.py', 'Newer', 'pr_files_in_os.py']

file = [f for f in os.listdir() if os.path.isfile(f)]  # хотим отфильтровать только файлы (генератор списка файлов)
dirs = [d for d in os.listdir() if os.path.isdir(d)]   # хотим отфильтровать только файлы (генератор списка директорий)
# пробегаем по списку файлов или директорий и если они удовлетворяют условию isfile или isdir, то выводим
print(file)
print(dirs)

# print('os позволяет запускать файлы')
# os.startfile(file[0])                           # из списка файлов и должен появиться текстовый документ
# print('os если хочу получить информацию из файла')

print('Атрибуты')
print(os.stat(file[0]).st_size) # # без st_size когда создали, использовали ..., с st_size - один из атрибутов
file_stat = os.stat('L_the_rest.py')
print(file_stat)
print(file_stat.st_size)
print(file_stat.st_mtime)
'''
Атрибуты, которые вы видите в `os.stat_result`, представляют собой информацию о файле или каталоге в файловой системе. 
Каждый из этих атрибутов содержит специфические данные. Вот объяснение каждого из них:
1. **st_mode**: хранит информацию о типе файла и правах доступа (permissions). Например, значение `33206` указывает, 
что это обычный файл, содержит права доступа, такие как чтение и запись для владельца, группы и других пользователей
2. **st_ino**: номер inode файла (в UNIX-системах), уник. ID, используется файловой системой для управления файлами.
3. **st_dev**: ID устройства, где хранится файл, полезно, если работать с файловыми системами на различных устройствах.
4. **st_nlink: Кол-во жестких ссылок на файл. Если у файла несколько имен (жестких ссылок), значение будет > одного.
5. **st_uid**: ID пользователя (user ID), кому принадлежит файл. Значение соответствует UID пользователя в оп. системе.
6. **st_gid**: ID группы (group ID), к которой принадлежит файл. Значение соответствует GID группы в операционной системе.
7. **st_size**: Размер файла в байтах. В вашем случае этот файл имеет размер 1868 байт.
8. **st_atime**: Время последнего доступа к файлу (last access time) в формате временной метки (Unix timestamp). 
В вашем случае это `1728406553` секунд с начала эпохи Unix (1 января 1970 года).
9. **st_mtime**: Время последнего изменения содержимого файла (last modification time), также в формате временной метки.
Значение `1728406553` указывает на время, когда содержимое файла было последний раз изменено.
10. **st_ctime**: Время изменения метаданных файла (last status change time), например, когда файл был создан или когда
 к нему были изменены права доступа. Это также в формате временной метки.
Эти атрибуты обычно получаются с помощью функции `os.stat()`, которая возвращает объект `os.stat_result`, 
содержащий всю указанную информацию о файле.
'''

