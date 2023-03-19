from tabulate import tabulate


def greeting():
    print("\nТелефонный справочник\n")


def menu():
    print("\nМеню:\n1) Добавить контакт\n2) Посмотреть записанные контакты\n3) Найти контакт\n4) Изменить контакт\n5) Удалить контакт\n6) Завершить работу\nВведите номер пункта меню: ")


def print_phonebook(data):
    print(tabulate(data, headers=["Фамилия",
          "Имя", "Телефон"]))


def second_menu():
    print("\n1) Продолжить работу с программой\n2) Завершить работу")


def ask_last_name():
    print("Введите Фамилию: ")


def ask_first_name():
    print("Введите Имя: ")


def ask_phone():
    print("Введите Телефон: ")


def complete():
    print("\nЗапись прошла успешно!")


def ask_find_word():
    print("Введите слово для поиска: ")


def print_finded_line(finded_line):
    print("Вот что мы нашли:\n", tabulate(finded_line, headers=["Фамилия",
          "Имя", "Телефон"]))


def print_no_finded_line():
    print("К сожалению, ничего не найдено.")


def change_contact():
    print("Хотите изменить контакт? Давайте его найдем. Введите слово для поиска:")


def menu_of_change_contact():
    print("\nМеню:\n1) Изменить фамилию\n2) Изменить имя\n3) Изменить номер телефона\n4) Вернуться в меню выше")


def suссess_result():
    print("Данные успешно изменены!")


def ask_number_of_contact():
    print("Какой контакт хотите изменить? Введите порядковый номер: ")


def delete_contact():
    print("Хотите удалить контакт? Давайте его найдем. Введите слово для поиска:")


def ask_number_of_contact_to_delete():
    print("Какой контакт хотите удалить? Введите порядковый номер: ")


def delete_menu():
    print("Точно удаляем?\n1) Точно!\n2) Нет, я передумал!\nВаш выбор:")


def bye():
    print("До свидания!")