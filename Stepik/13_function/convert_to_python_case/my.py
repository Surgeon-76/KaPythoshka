# объявление функции
def convert_to_python_case(text):
    snake_style = ''
    for i in text:
        if i.isupper() and text.index(i) != 0:
            snake_style += '_'
        snake_style += i.lower()
    return snake_style
  #MyMethodThatDoSomething не  
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))