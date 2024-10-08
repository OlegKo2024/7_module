
print('Файлы в операционной системе')

import os
import time

print('Текущая директория:', os.getcwd())
current_file_path = os.path.abspath(__file__)
print(current_file_path)

for root, dirs, files in os.walk('.'):  # Обход каталога с os.walk() - возвращает кортеж для каждой директории, где
    # root - текущая директория, dirs - подкаталоги, а files - файлы в текущем каталоге
    for file in files:
        filepath = os.path.join(root, file)     # Формирование полного пути к файлу
        print(f'Обнаружен файл: {file}, Путь: {filepath}')
    for dir in dirs:
        dirpath = os.path.join(root, dir)
        print(f'Обнаружена директория: {dir}, Путь: {dirpath}')
file_stat = os.stat(r'.\pr_files_in_os.py')
print(file_stat)
file_time_stat = file_stat.st_mtime
print(file_time_stat)
file_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time_stat))
print(file_time)

filetime = os.path.getmtime(current_file_path) # Получение времени последнего изменения файла
print(filetime)
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # Форматирование времени
print(formatted_time)
filesize = os.path.getsize(current_file_path)

parent_dir = os.path.dirname(current_file_path)    # Получение родительской директории файла

print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
      f'Родительская директория: {parent_dir}')