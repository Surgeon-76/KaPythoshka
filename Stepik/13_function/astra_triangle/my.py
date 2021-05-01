# объявление функции
def draw_triangle(fill, base):
    for i in range(base):
        print(*[fill for n in range((base // 2 + 1) - abs(base // 2 - i))], sep = '')

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)