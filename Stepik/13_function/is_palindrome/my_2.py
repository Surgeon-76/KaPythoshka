# объявление функции
def is_palindrome(text):
    text = [i.lower() for i in text if i.isalpha()]
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))