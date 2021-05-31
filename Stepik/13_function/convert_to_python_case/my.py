# объявление функции
def convert_to_python_case(text):
    snake_style = ''
<<<<<<< HEAD
    for i in text:
        if i.isupper() and text.index(i) != 0:
=======
    for i in range(len(text)):
        if text[i].isupper() and i != 0:
>>>>>>> 338356adfea3bc4f75fbc533da8df9a1a1fbb4b2
            snake_style += '_'
        snake_style += text[i].lower()
    return snake_style
  #MyMethodThatDoSomething не  
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))