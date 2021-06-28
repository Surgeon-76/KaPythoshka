# объявление функции
def get_shipping_cost(quantity):
    return 120 * (quantity - 1) + 1000
# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))