# объявление функции
def get_days(month):
     year = [31,28,31,30,31,30,31,31,30,31,30,31]
     return year[month - 1]

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))