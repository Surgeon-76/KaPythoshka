# объявление функции
def print_digit_sum(num):
    print(sum([m for m in [int(i) for i in str(n)]]))
    
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)