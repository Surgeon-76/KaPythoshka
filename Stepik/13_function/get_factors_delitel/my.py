# объявление функции
def get_factors(num):
    myList = []
    for i in range(1, n+1):
        if n % i == 0:
            myList.append(i)
    return myList    

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))