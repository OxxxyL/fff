numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] #Создали список для хранения простых и не простых чисел
not_primes = []

a = 2 #первое простое число
b = len(numbers) #Переменная b получает длину списка numbers, которая равна 15

for num in range (a, b + 1): #Перебираем каждое число из списка и проверяем на простоту от 2 до 15

    if num == 1: #Число 1 и меньше не являются простыми если num = 1, будет пропуск итерации, так как 1 не простое число
        not_primes.append(num)
        continue

    is_prime = True #Проверка на простоту

    for j in range(a, num): #Проверяем делители от 2 до -1 (всех возможных делителей)
        if num % j  == 0: #Если num делится на j без остатка, значит num не простое
            is_prime = False #Если нашли делитель,оно идёт в список число не простое и False выходит из цикла
            break #Остановка

    if is_prime: #(True - в prime, False - в not_prime).
        primes.append(num) #Добавляем простое число в список primes
    else:
        not_primes.append(num) #Добавляем не простое число в список not_primes

print("Primes:", primes)
print("Not Primes:", not_primes)