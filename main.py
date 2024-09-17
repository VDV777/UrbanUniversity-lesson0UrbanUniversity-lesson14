# Пункты задачи:
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
import re


def send_email(message: str, recipient: str, sender='university.help@gmail.com') -> None:

    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if (re.match(email_pattern, recipient) is None) and (re.match(email_pattern, sender) is None):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.


send_email('Hello World!!!', '123@mail.com', 'vdv6nick@.mail.com')
