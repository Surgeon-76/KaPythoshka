variants = [['камен', 'камень'], ['ящерица', 'ножницы'], ['Спок', 'ящерица'], ['ножницы', 'бумага'], ['бумага', 'Спок']]
winner = ['ничья', 'Руслан', 'Тимур','Руслан', 'Тимур']
y = 0
def index_search(data_str, array):
    for subarray in array:
        if data_str in subarray:
            print(array.index(subarray), '-', subarray.index(data_str))

"""
def choice_of_index(timur, ruslan, y):
    return variants.index(timur)[y] - variants.index(ruslan)[y]
"""
timur, ruslan = input(), input()
index_search(timur, variants)
print('==')
index_search(ruslan, variants)
#print(variants[variants.index(timur)][y])

"""
if (choice_of_index(timur, ruslan, y) != 1) or (choice_of_index(timur, ruslan, y) != 4) or (choice_of_index(timur, ruslan, y) != -4) or (choice_of_index(timur, ruslan, y) != -1):
    y = 1
print(winner[variants[y].index(timur) - variants[y].index(ruslan)])
"""
"""
array = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
for subarray in array:
    if 'a' in subarray:
        print(array.index(subarray), '-', subarray.index('a'))
"""
