def custom_write(file_name, strings): # Функция принимает имя файла, в который будет записан текст и список строк
    strings_positions = {} # Пустой словарь для хранения позиций строк в файле
    file = open(file_name, 'w', encoding = 'utf-8') # Открывает для записи, если сущ. то перезаписывается
    for num_str, str_ in enumerate(strings, 1): # Получение номер строки и саму строку, с 1.
        byte_ = file.tell()
        file.write(str_ + '\n') # строка записывается в файл с добавлением символа новой строки
        strings_positions[(num_str, byte_)] = str_ #Показывает где строка была записана и на какой позиции
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)