def get_multiplied_digits(number): #Функция которая принимает только целые числа
    str_number = str(number) # Преобразуем число в строку для удобства
    first = int(str_number[0])

    if len(str_number) > 1: #Длина строки больше 1? Проверяем, если 1=1 то это последняя цифра
          #Первую цифру преобразуем в целое число. Значение для умножения
        # Берем число и умножаем на рекурсию
        return first * get_multiplied_digits(int(str_number[1:]))
    #Если длина строки больше 1 = Функция рекурсивно передает цифры все кроме первой(str_num[1:])
    #Умножаем первую цифру на результат рекурсивного вызова функции, постепенно вычисляя произведение всех цифр
    else:
        # Если длина строки 1, возвращаем оставшуюся цифру как целое число, это конец...
        return first

# Обработка нулей
def get_multiplied_digits_without_zeros(number): #Преобразуем число в строку для перебора
    str_number = str(number)
    product = 1
    for digit in str_number:
        if digit != '0':  # Игнорируем нули, если цифра не равна 0 то умножаем на product
            product *= int(digit)
    return product

result = get_multiplied_digits_without_zeros(402030)
print(result)

#Стек вызовов будет выглядеть следующим образом:
#При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
#get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3
#Вызываем get_multiplied_digits_without_zeros(402030), что возвращает 24, так как 4 * 2 * 3 = 24.
