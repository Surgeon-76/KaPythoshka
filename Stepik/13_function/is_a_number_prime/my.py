# объявление функции
def is_prime(num):
    if len([n for n in range(1, num + 1) if num % n == 0]) == 2 and n != 1:
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))