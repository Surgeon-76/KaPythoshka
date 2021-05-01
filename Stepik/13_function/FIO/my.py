# объявление функции
def print_fio(name, surname, patronymic):
    print(name[0].upper() + surname[0].upper() + patronymic[0].upper())

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)