print('Задача "Найдёт везде"')


class WordsFinder:
    all_file_names = []

    def __init__(self, *file_names):
        self.file_names = list(file_names)
        WordsFinder.all_file_names.extend(self.file_names)

    def get_all_words(self):
        all_words = {}  # Словарь для хранения списка слов, из каждого файла
        for file_name in self.file_names:  # Перебираем отдельно по каждому имени файла в списке
            all_words[file_name] = []  # Для каждого файла создаем пустой список, где имя файла - ключ
            with open(file_name, encoding='utf-8') as file:  # Открыли файл
                for line in file:  # Читаем файл построчно на каждом цикле
                    low_font_file = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', '-']  # '-' - без пробелов, иначе слова слипаются
                    translation_table = str.maketrans('', '', ''.join(punctuation))
                    cleaned_file = low_font_file.translate(translation_table)
                    words = cleaned_file.split()  # Разбиваем строку по пробелам, если не сделать каждый символ - строка
                    all_words[file_name].extend(words)  # Добавляем слова к списку / append даст списки внутри списков
        return all_words

    def find(self, word):
        locate_word = {}    # словарь
        all_words = self.get_all_words() # получаем все слова используя метод выше
        for file_name, word_list in all_words.items(): # итерация по каждому файлу и словам
            key = file_name
            if word.lower() in word_list: # проверяем, был ли вообще мальчик
                value_number = 0
                for i in range(len(word_list)):
                    if word.lower() != word_list[i]:
                        value_number += 1 # если был, считаем пока не нарываемся на него
                    else:
                        break
            else:
                print(f'{word} not found in {all_words}') # не был, значит пишем как есть
                return
            locate_word[key] = value_number # записываем в словарь
        return locate_word

    def count(self, word):
        count_word = {}
        all_words = self.get_all_words()
        for file_name, word_list in all_words.items():
            key = file_name
            if any(word.lower() == file_word for file_word in word_list): # немного иначе проверяем был ли мальчик
                for file_word in word_list:
                    count = word_list.count(word.lower()) # считаем сколько их
            else:
                print(f'{word} not found in {all_words}')
            count_word[key] = count # записываем в словарь
        return count_word


finder1 = WordsFinder('test.txt')
finder2 = WordsFinder('test_file.txt')
print(WordsFinder.all_file_names)
print(finder1.get_all_words())
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
