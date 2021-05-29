# объявление функции
def convert_to_python_case(text):
    snake_style = ''
    for i in range(len(text)):
        if text[i].isupper() and i != 0:
            snake_style += '_'
        snake_style += text[i].lower()
    return snake_style
    
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))