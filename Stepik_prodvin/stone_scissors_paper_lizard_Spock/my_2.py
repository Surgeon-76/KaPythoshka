variants = [['камень', 'камень'], ['ящерица', 'ножницы'], ['Спок', 'ящерица'], ['ножницы', 'бумага'], ['бумага', 'Спок']]
winner = ['ничья', 'Руслан', 'Руслан','Руслан', 'Тимур']
y = 0

def index_search(data_str, array):#определение индексного массива для по результатам хода Тимура и Руслана
    return [[index1,index2] for index1,value1 in enumerate(array) for index2,value2 in enumerate(value1) if value2 == data_str]

def index_circle_or_star(timur_index, ruslan_index):#вычисление индекса для списка winner[] на основе индексов вложенных списков("по кругу" игра, либо "по звезде"(см. рисунок-схему в комментариях к заданию))
    for it in range(2):
        for jt in range(2):
            for ir in range(2):
                for jr in range(2):
                    if ((timur_index[it][0] - ruslan_index[ir][0] == 1) or (timur_index[it][0] - ruslan_index[ir][0] == -1) or (timur_index[it][0] - ruslan_index[ir][0] == 4) or (timur_index[it][0] - ruslan_index[ir][0] == -4)) and (timur_index[it][1] == ruslan_index[ir][1]):
                        return timur_index[it][0] - ruslan_index[ir][0]
                    elif timur == ruslan: 
                        return 0

# основное тело программы
timur, ruslan = input(), input()
y = index_circle_or_star(index_search(timur, variants), index_search(ruslan, variants))
print(winner[y])
