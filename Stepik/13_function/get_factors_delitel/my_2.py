# объявление функции
def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]    

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))