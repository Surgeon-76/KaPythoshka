# объявление функции
def get_month(language, number):
    if language == 'en':
        month = ['','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']  
    else:
        month = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    return month[number]
    
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))