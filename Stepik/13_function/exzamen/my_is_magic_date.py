# объявление функции
def is_magic(date):
    magic_date = [int(n) for n in(date.split('.'))]
    return magic_date[0] * magic_date[1] == magic_date[2] % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))