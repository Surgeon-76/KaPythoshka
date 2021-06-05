#функция количества буквенных элементов в слове
def length_words(words):
    return len([k for k in words if k.isalpha()])

#основной цикл программы
f_text = []
text = input('Введите текст для обработки:\n').split()

for i in text:
    print(i, length_words(i))
    
    
 #   length_words(i)
    

