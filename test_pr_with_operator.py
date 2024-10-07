class WordsFinder:
    all_file_names = []

    def __init__(self, *file_names):
        self.file_names = list(file_names)
        WordsFinder.all_file_names.extend(self.file_names)

# Уроки:
# не создал all_words[file_name] = [], в который будут добавляться слова
# не знал, что сам перебор for line in file: - это уже прочтение и не надо file.read()
# все, что связано с punctuation = [',', '.', '=', '!', '?', ';', ':', '-'] - новое
# не знал как добавлять к списку в словарь с помощью .extend и .append
# .split - разбиваем по пробелам, а так разобьет по буквам

    def get_all_words(self):
        all_words = {}      # Словарь для хранения списка слов, из каждого файла
        for file_name in self.file_names: # Перебираем отдельно по каждому имени файла в списке
            all_words[file_name] = []     # Для каждого файла создаем пустой список, где имя файла - ключ
            with open(file_name, encoding='utf-8') as file: # Открыли файл
                for line in file:                           # Читаем файл построчно на каждом цикле
                    low_font_file = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', '-'] # '-' - без пробелов, иначе слова слипаются
                    translation_table = str.maketrans('', '', ''.join(punctuation))
                    cleaned_file = low_font_file.translate(translation_table)
                    words = cleaned_file.split() # Разбиваем строку по пробелам, если не сделать каждый символ - строка
                    # all_words[file_name].extend(words) # Добавляем слова к списку / append даст списки внутри списков
                    for word in words:
                        all_words[file_name].append(word)
        return all_words

# Задание: find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
# позиция первого такого слова в списке слов этого файла.
# Уроки:
    # не запустил функцию, чтобы вытащить словарь all_words как переменная
    # все время хотелось поставить self, но: `self` — это специальное имя в Python, которое используется в методах
    # классов для обозначения текущего экземпляра класса. Концептуально, `self` можно понимать как ссылку на объект,
    # который был создан из класса, и он используется для доступа к переменным и методам, принадлежащим этому объекту
    # Например:
        # При создании экземпляра `WordsFinder`, метод `__init__` вызывается автоматически. Здесь `self.file_names`
        # будет хранить список имен файлов, переданных при создании объекта. Если, например, вы создали экземпляр
        # finder = WordsFinder("file1.txt", "file2.txt")` - `self.file_names` станет равным `["file1.txt", "file2.txt"]`

    def find(self, word):
        find_word = {}
        all_words = self.get_all_words()
        for file_name, word_list in all_words.items():
            key = file_name
            if word.lower() in word_list:
                value_number = 0
                for i in range(len(word_list)):
                    if word.lower() != word_list[i]:
                        value_number += 1
                    else:
                        break
            else:
                print(f'{word} not found in {all_words}')
                return
            find_word[key] = value_number
        return find_word

    def find_00(self, word):
        locate_word = {}  # Словарь для хранения результатов поиска
        # Проверяем наличие файлов и возвращаем пустой результат, если файл отсутствует
        if not any(file_name in WordsFinder.all_file_names for file_name in self.file_names):
            return locate_word  # Возвращаем пустой словарь, если ни один файл не найден

        # Получаем все слова из файлов
        all_words = self.get_all_words()  # Вызываем метод для получения всех слов

        # Перебираем все файлы и их слова
        for file_name, words_list in all_words.items():  # Итерация по каждому файлу и его словам
            found_index = None  # Переменная для хранения индекса найденного слова
            # Ищем слово в списке слов, если оно есть, запоминаем его индекс
            for index, current_word in enumerate(words_list):  # Перебираем слова с их индексами
                if current_word == word.lower():  # Сравниваем слово без учета регистра
                    found_index = index  # Запоминаем индекс
                    break  # Выходим из цикла, так как нашли слово

            if found_index is not None:  # Проверяем, было ли слово найдено
                locate_word[file_name] = found_index  # Записываем файл и индекс слова

        return locate_word  # Возвращаем словарь с результатами поиска

# Задание: count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
# значение - количество слова word в списке слов этого файла.
    def count(self, word):
        count_word = {}
        all_words = self.get_all_words()
        for file_name, word_list in all_words.items():
            key = file_name
            if any(word.lower() == file_word for file_word in word_list):
                for file_word in word_list:
                    count = word_list.count(word.lower())
            else:
                print(f'{word} not found in {all_words}')
            count_word[key] = count
        return count_word



finder0 = WordsFinder('test.txt', 'test_file.txt')
finder1 = WordsFinder('test.txt')
finder2 = WordsFinder('test_file.txt')
print(finder0.file_names)
print(finder1.file_names)
print(finder2.file_names)
print(WordsFinder.all_file_names)

print(finder1.get_all_words())
print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего