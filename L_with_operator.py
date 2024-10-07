
def with_(file_name):
    # file = file_name                                       # не нужно, сразу можно без переменной
    with open(file_name, 'r', encoding='utf-8') as file:     # но можно и без 'r' - по умолчанию чтение
        for line in file:
            print(line)

result = with_('test.txt')
print(result)

# строки с пробелом, чтобы его убрать - end=''

print('Lecture_00')

file_name = 'test.txt'
with open(file_name, encoding='utf-8') as file:
    for line in file:
        print(line, end='')

print('Lecture_01')

file_name = 'test.txt'
with open(file_name, encoding='utf-8') as file:
    for line in file:
        for char in line:
            print(char, end='')     # c end='' получим тоже самое, но если убрать но во вертикали получим каждый символ

# print(file.read())      ValueError: I/O operation on closed file. - действие на закрытом файле





