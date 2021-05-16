# объявление функции
def get_next_prime(num):
    k = n
    while not len([n for n in range(1, k + 1) if num % n == 0]) == 2:
        k += 1
    


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))