calls = 0 #Глобальная переменная для подсчета вызовов функции

def count_calls():
    global calls #Позволяет функции изменять глобальную переменную, а не создавать новую локальную с тем же именем
    calls += 1 #Увеличивает значение переменной calls на 1 каждый раз когда она вызывается

def string_info(string): #Принимает строку в качестве аргумента, возвращает кортеж, содержащий....
    count_calls() #Увеличиваем счетчик вызовов
    length = len(string) #Длину строки
    upper = string.upper() #строку в Верхнем регистре
    lower = string.lower() #строку в Нижнем регистре
    return (length, upper, lower)

def is_contains(string, list_to_search): #принимает строку и список, проверяет есть ли строка в списке
    count_calls() #Увеличиваем счетчик вызовов
    return string.lower() in (item.lower() for item in list_to_search) #Проверка есть ли в списке

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
count_calls()


