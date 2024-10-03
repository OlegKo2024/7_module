print('Задача "Записать и запомнить"')


def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    for i in strings:
        file.write(f'{i}\n')  # Записываем строки в файл
    print(file.tell())  # 117
    file.seek(0)  # Переходим в начало файла
    read_to_dict = {}
    for i in range(len(strings)):
        byte_position = file.tell()  # Получаем текущее положение курсора (начало строки)
        line = file.readline()  # Считаем строку
        key = (i + 1, byte_position)  # Сохраняем номер строки, положение курсора и строку в словаре
        read_to_dict[key] = line.rstrip('\n')  # Убираем символ новой строки
    file.close()
    return read_to_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!!!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
