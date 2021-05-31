# объявление функции
def is_pangram(text):
    return len(list(set([s for s in text.replace(' ', '').lower() if ord(s) in range(97, 123)]))) == 26

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))