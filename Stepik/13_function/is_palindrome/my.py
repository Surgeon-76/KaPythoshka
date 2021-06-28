# объявление функции
def is_palindrome(text):
    for i in ' .,!?-':
        text = text.replace(i, '')
    text = text.lower()
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))