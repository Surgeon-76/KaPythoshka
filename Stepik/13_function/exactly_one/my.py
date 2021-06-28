# объявление функции
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        flag = True
        n = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                n += 1
        if n != 1:
            flag = False
    else:
        flag = False
    return flag

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))