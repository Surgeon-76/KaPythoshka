
vestch = ['бумага', 'ножницы', 'камень']
timur, ruslan = input(), input()
if timur in vestch:
    timur_ind = vestch.index(timur)
if ruslan in vestch:
    ruslan_ind = vestch.index(ruslan)
if ruslan_ind == timur_ind:
    print('ничья')
if (ruslan_ind == 2 and timur_ind == 1) or (timur_ind == 2 and ruslan_ind == 0) or (ruslan_ind == 1 and timur_ind == 0): 
    print('Руслан')
elif (timur_ind == 2 and ruslan_ind ==1) or (ruslan_ind == 2 and timur_ind == 0) or (timur_ind == 1 and ruslan_ind == 0): 
    print('Тимур')
