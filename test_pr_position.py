l = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

print(len(l))

print(len('Text for tell.')) # 14
print(len('Используйте кодировку utf-8.'))

# ((1, 15), 'Text for tell.\n')
# ((2, 44), 'Используйте кодировку utf-8.\n')
# ((3, 75), 'Because there are 2 languages!\n')
# ((4, 84), 'Спасибо!\n')

def linesize(line):
    pos = 0
    key = []
    for i in range(len(line)):
        pos += len(line[i])
        key.append(pos)
    return key

result = linesize(l)
print(result)

l = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

print(len(l))

def line_size(lines):
    pos = 0
    key = []
    for line in lines:      # теперь мы перебирать строки в списке lines
        pos += len(line)    # увеличиваем длину на длину текущей строки
        key.append(pos)     # добавляем новую позицию в список
    return key

result = line_size(l)
print(result)

print('Решение chatGPT')

def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл для записи в бинарном режиме
    file = open(file_name, 'wb')  # 'wb' - режим записи в бинарном виде

    # Перебираем строки
    for index, string in enumerate(strings):
        # Получаем байтовую строку
        byte_string = string.encode('utf-8')  # Кодируем строку в байты

        # Получаем текущую позицию (количество байт, уже записанных в файл)
        position = file.tell()  # Считываем текущую позицию в байтах

        # Записываем строку в файл, добавляя перевод строки
        file.write(byte_string + b'\n')  # Записываем байтовую строку, добавляя '\n'

        # Добавляем позицию и строку в словарь
        strings_positions[(index + 1, position)] = string  # Используем (номер строки, байт начала строки)

    file.close()  # Закрываем файл после завершения записи
    return strings_positions

# Пример выполнения кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

print('Вариант 1')
def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    for i in strings:
        file.write(f'{i}\n')
    file.seek(0)                                    # 0 курсор в начало
    print(file.tell())
    read_to_dict = {}
    lines = file.readlines()                        # читаем и сохраняем строки в виде списка под переменной
    print(file.tell())                              # 115 курсор в конце файла
    file.seek(0)
    byte_position = file.tell()
    for line_number, line in enumerate(lines):      # идем по строкам списка и имеем номер строки и строку
        line_number += 1
        byte_position += len(line)                  # положение курсора перед чтением текущей строки - не верно.
        key = (line_number, byte_position)
        read_to_dict[key] = line
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

print('Вариант 2')

def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    for i in strings:
        file.write(f'{i}\n')
    file.seek(0)
    read_file = file.read()
    file.seek(0)
    print(file.tell())
    lines = read_file.split('\n')
    read_to_dict = {}
    byte = file.tell()
    for i in range(len(lines) - 1):
        byte += len(lines[i]) + 1
        key = (i+1, byte)
        line = lines[i]
        read_to_dict[key] = line
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


print('Вариант 3')

def custom_write(file_name, strings):
    with open(file_name, 'w+', encoding='utf-8') as file:
        # Записываем строки в файл
        for i in strings:
            file.write(f'{i}\n')
        # Переходим в начало файла
        file.seek(0)
        read_to_dict = {}
        for i in range(len(strings)):
            # Читаем строку
            line = file.readline()
            # Получаем текущее положение курсора
            byte_position = file.tell()
            # Сохраняем номер строки, положение курсора и строку в словаре
            key = (i + 1, byte_position)  # i + 1 для номеров строк, начинающихся с 1
            read_to_dict[key] = line.rstrip('\n')  # Убираем символ новой строки

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

print('Вариант 4')

def custom_write(file_name, strings):
    with open(file_name, 'w+', encoding='utf-8') as file:
        # Записываем строки в файл
        for i in strings:
            file.write(f'{i}\n')

        # Переходим в начало файла
        file.seek(0)
        read_to_dict = {}
        for i in range(len(strings)):
            # Получаем текущее положение курсора (начало строки)
            byte_position = file.tell()
            # Читаем строку
            line = file.readline()
            # Сохраняем номер строки, положение курсора и строку в словаре
            key = (i + 1, byte_position)  # i + 1 для номеров строк, начинающихся с 1
            read_to_dict[key] = line.rstrip('\n')  # Убираем символ новой строки

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

print('Вариант 5')

def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    for i in strings:
        file.write(f'{i}\n')                    # Записываем строки в файл
    print(file.tell())                          # 117
    file.seek(0)                                # Переходим в начало файла
    read_to_dict = {}
    for i in range(len(strings)):
        byte_position = file.tell()             # Получаем текущее положение курсора (начало строки)
        line = file.readline()                  # Считаем строку
        key = (i + 1, byte_position)            # Сохраняем номер строки, положение курсора и строку в словаре
        read_to_dict[key] = line.rstrip('\n')   # Убираем символ новой строки
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