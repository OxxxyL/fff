data_structure = [
  [1, 2, 3], #1+2+3=6 Список
  {'a': 4, 'b': 5}, #4+5=9 Словарь
  (6, {'cube': 7, 'drum': 8}), #6+7+8=21 Кортеж
  "Hello", #Длина=5 Строка
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure): #Рекурсивно вычисляем сумму элементов
    sum_ = 0 #Инициализируем переменную для накопления суммы
    if isinstance(structure, int):
        sum_ = sum_ + structure #Если str явл целым число, мы добавим его к sum_
    if isinstance(structure, str):
        sum_ = sum_ + len(structure) #Если str явл строкой, мы добавляем длину строки к sum_
    if isinstance(structure, list):
        for i in range(len(structure)): #Если str явл списком, перебираем и вызываем cal_srt для каждого элемента
            sum_ = sum_ + calculate_structure_sum(structure[i])
    if isinstance(structure, tuple): #Если str явл кортежем, мы перебираем элементы и рекурсивно обрабатываем
        for i in range(len(structure)):
            sum_ = sum_ + calculate_structure_sum(structure[i])
    if isinstance(structure, set): #Если str является множеством, мы сначала преобразуем его в список, обрабатываем
        structure = list(structure)
        for i in range(len(structure)):
            sum_ = sum_ + calculate_structure_sum(structure[i])
    if isinstance(structure, dict): #Если str является словарем, мы преобразуем в список пар (ключ/знач)+обрабатываем
        structure = list(structure.items())
        for i in range(len(structure)):
            sum_ = sum_ + calculate_structure_sum(structure[i])
    return sum_ #Возвращаем сумму

result = calculate_structure_sum(data_structure)
print(result)