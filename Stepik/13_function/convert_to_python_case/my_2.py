# объявление функции
def convert_to_python_case(text):
    return ['_' + l.lower() for l in text if  [s for s in text if s.isupper() and s != text[0]]]
    
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))