my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list): #Цикл продолжается, пока индекс меньше длины списка
    if my_list[index] < 0: #Если число будет отрицательное, мы используем break чтобы выйти из цикла
        break #Останавливаем цикл, если встречаем отрицательное число
    print(my_list[index]) #Выводим положительные
    index += 1 #увеличиваем индекс на 1 чтобы перейти к следующему элементу списка