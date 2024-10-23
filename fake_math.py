def divide(first, second): #Числа которые хотим разделить
    if second == 0: #Когда в second записан 0 - возвращать строку 'Ошибка'.
        return 'Ошибка'
    else: #Если делитель не равен нулю, функция выполняет деление first / second и возвращает результат.
        return first / second