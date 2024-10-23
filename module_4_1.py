# Импортируем модули с переименовыванием
import fake_math as fakeM
import true_math as trueM


# присваиваем значения для фу-ции divide из двух импортируемых модулей
fake_divide = fakeM.divide
true_divide = trueM.divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# вывод результата
print(result1)
print(result2)
print(result3)
print(result4)