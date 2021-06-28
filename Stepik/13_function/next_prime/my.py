# объявление функции
def get_next_prime(num):
    k = num
    flag = True
    while flag:
        if len([n for n in range(1, k + 1) if k % n == 0]) != 2 or k == num:
            k += 1
        else:
            flag = False     
    return k

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))