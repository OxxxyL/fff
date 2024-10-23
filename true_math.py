from math import inf

def divide(first, second): #Числа которые хотим разделить
    if second == 0: #Когда в second записан 0 - возвращать бесконечность
        return inf #Функция возвращает результат деления first на second
    else: #Если делитель не равен нулю, функция выполняет деление first/ second и возвращает результат
        return first / second