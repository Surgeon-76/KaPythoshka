# объявление функции
def is_one_away(word1, word2):
    return len([i for i in word1 if i not in word2]) == 1 and len(word1) == len(word2)

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))