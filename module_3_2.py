def send_email(message, recipient, *, sender = "university.help@gmail.com"): #SMS, получатель и отправитель по умолчанию
    def is_valid_email(email): #Проверяем содержит ли e-mail символ @ и заканчивается ли на окончания
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or
    email.endswith(".net"))
#Именованные аргументы отделяются от остальных символом "*" перед ними.
    #Именованные аргументы всегда идут после позиционных.
 # Проверка корректности адресов, если не проходит проверку, выдаст ошибку
    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Проверка на отправку самому себе, если совпадает, выводится следующее смс
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию, если верно то успешно, если нет, то вывод смс о нестандартной отправке
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Примеры вызовов функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')