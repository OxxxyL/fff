class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = [*file_name] # Принимает имена и сохраняет как список
        self.file_name = file_name # Сохраняет кортеж имени файла

    def get_all_words(self):
        all_words = {}
        words = []
        simbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as open_:
                for line in open_: # Открывает файл и читает его построчно
                    line = line.lower() # Нижний регистр
                    for p in simbols: # Замена simbols на пробелы
                        if p in line:
                            line = line.replace(p, ' ') # Разбивает строку на слова и добавляет их в список
                    split_line = line.split(sep=' ')
                    words.append(split_line)
        sorted_words = [x for y in words for x in y] # Объединяет все слова в один список
        all_words[self.file_name] = sorted_words
        return all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items(): # Перебирает слова
            for w in words:
                if word.lower() in w:
                    index = words.index(w)
                    dict_[self.file_name] = index + 1
                    break
        return dict_

    def count(self, word): # Подсчёт вхождения слов
        dict_ = {}
        count = 0
        for name, words in self.get_all_words().items():
            for w in words:
                if word.lower() in w:
                    count += 1
        dict_[self.file_name] = count
        return dict_


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

