print('Задача "Записать и запомнить"')

print('Вариант 1')

def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    for i in strings:
        file.write(f'{i}\n')  # Записываем строки в файл
    print(file.tell())  # 117
    file.seek(0)  # Переходим в начало файла
    read_to_dict = {}
    for i in range(len(strings)):
        byte_position = file.tell()  # Получаем текущее положение курсора (начало строки)
        line = file.readline()  # Считываем строку
        key = (i + 1, byte_position)  # Сохраняем номер строки, положение курсора в переменной key
        read_to_dict[key] = line.rstrip('\n')  # Записываем ключ и значение в словарь, убираем символ новой строки
    file.close()
    return read_to_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!!!'
]


result = custom_write('test.txt', info)
print(result)
for elem in result.items():
    print(elem)

print('Вариант 2')

def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    for i in strings:
        file.write(f'{i}\n')                    # Записываем строки в файл
    print(file.tell())                          # 117
    file.seek(0)
    read_file = file.readlines()                # Считываем файл построчно в список
    file.seek(0)                                # Переходим в начало файла после чтения
    read_to_dict = {}
    for i in range(len(read_file)):             # Используем считанный в список файл для задания кол-ва итераций
        byte_position = file.tell()
        line = file.readline()
        key = (i + 1, byte_position)
        read_to_dict[key] = line.rstrip('\n')
    file.close()
    return read_to_dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!!!'
]

result = custom_write('test.txt', info)
print(result)
for elem in result.items():
    print(elem)
