# объявление функции
def find_all(target, symbol):
    return [i for i in range(len(target)) if symbol == s[i]]
# считываем данные
s = input()
char = input()

# вызываем функцию
find_all(s, char)
print(find_all(s, char))