#функция количества буквенных элементов в слове
def length_words(words):
    return len([k for k in words if k.isalpha()])

#основной цикл программы
f_text = []
for i in input().split():
    temp = ''
    for j in i:
        symb_ord = 0
        if j.isalpha():
            symb_ord = ord(j) + length_words(i)
            if (ord(j) < 90 and symb_ord > 90) or (90 < ord(j) < 122 and symb_ord > 122):
                symb_ord -= 26
            temp += chr(symb_ord)
        else:
            temp += j
    f_text.append(temp) 
print(*f_text)


