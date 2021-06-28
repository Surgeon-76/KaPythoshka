variants = [['камень', 'камень'], ['ящерица', 'ножницы'], ['Спок', 'ящерица'], ['ножницы', 'бумага'], ['бумага', 'Спок']]
winner = ['ничья', 'Тимур', 'Руслан','Руслан', 'Тимур']
y = 0
"""
def index_search(data_str, array):
    index_s = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if data_str == array[i][j]:
                index_s.append([i, j])
                #index_s.append(j)
    return index_s 
"""   
"""
def index_circle_or_star(timur_index, ruslan_index):
    for i in range(0, 4, 2):
        print('i  = ', i)
        for j in range(1, 4, 2):
            print('j = ', j)
            if ((timur_index[i] - ruslan_index[i] == 1) or (timur_index[i] - ruslan_index[i] == -1) or (timur_index[i] - ruslan_index[i] == 4) or (timur_index[i] - ruslan_index[i] == -4)) and (timur_index[j] == ruslan_index[j]):
                return j
            else:
                return 0
"""
def index_search(data_str, array):
    return [[index1,index2] for index1,value1 in enumerate(array) for index2,value2 in enumerate(value1) if value2 == data_str]

def index_circle_or_star(timur_index, ruslan_index):
    for it in range(2):
        #print('I =', i)
        for jt in range(2):
            for ir in range(2):
                for jr in range(2):
                    #print('I =', i, 'J =', j, sep=':')
                    #print(timur_index[i][j], ruslan_index[i][j], sep=':')
                    #print('timur_index[i][0] - ruslan_index[i][0] =', timur_index[i][0] - ruslan_index[i][0])
                    #print('timur_index[i][1] == ruslan_index[i][1]', timur_index[i][j], ruslan_index[i][j])
                    if ((timur_index[it][0] - ruslan_index[ir][0] == 1) or (timur_index[it][0] - ruslan_index[ir][0] == -1) or (timur_index[it][0] - ruslan_index[ir][0] == 4) or (timur_index[it][0] - ruslan_index[ir][0] == -4)) and (timur_index[it][1] == ruslan_index[ir][1]):
                        return timur_index[it][1]
            
"""
def choice_of_index(timur, ruslan, y):
    return variants.index(timur)[y] - variants.index(ruslan)[y]
"""
timur, ruslan = input(), input()
timur_index = index_search(timur, variants)
print(timur_index)
print('==')
ruslan_index = index_search(ruslan, variants)
print(ruslan_index)
#index_circle_or_star(timur_index, ruslan_index)
y = index_circle_or_star(timur_index, ruslan_index)
print(y)
#print(variants[variants.index(timur)][y])

"""
if (choice_of_index(timur, ruslan, y) != 1) or (choice_of_index(timur, ruslan, y) != 4) or (choice_of_index(timur, ruslan, y) != -4) or (choice_of_index(timur, ruslan, y) != -1):
    y = 1
print(winner[variants[y].index(timur) - variants[y].index(ruslan)])
"""
