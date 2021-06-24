variants = [['камень', 'камень'], ['ящерица', 'ножницы'], ['Спок', 'ящерица'], ['ножницы', 'бумага'], ['бумага', 'Спок']]
winner = ['ничья', 'Руслан', 'Тимур','Руслан', 'Тимур']
y = 0
"""
def choice_of_index(timur, ruslan, y):
    return variants.index(timur)[y] - variants.index(ruslan)[y]
"""
timur, ruslan = input(), input()
print(variants[variants.index(timur)][y])

"""
if (choice_of_index(timur, ruslan, y) != 1) or (choice_of_index(timur, ruslan, y) != 4) or (choice_of_index(timur, ruslan, y) != -4) or (choice_of_index(timur, ruslan, y) != -1):
    y = 1
print(winner[variants[y].index(timur) - variants[y].index(ruslan)])
"""
