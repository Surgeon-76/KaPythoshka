from random import*

#функция генератор
def generate_password(length, pwr):
    shuffle(pwr)                     #перемешаем всё...
    password = ''
    for j in range(length):
        password += choice(pwr)
    return password

#определение переменных
pwr = []
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

#считывание данных и определение алгоритма паролей
n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
if (input('Включить цифры? (д = да, н = нет) ').strip().lower()) == ('д' and 'l'):
    pwr.extend(digits)    
if (input('Включить прописные буквы? (д = да, н = нет) ').strip().lower()) == ('д' and 'l'):
    pwr.extend(lowercase_letters)
if (input('Включить строчные буквы? (д = да, н = нет) ').strip().lower()) == ('д' and 'l'):
    pwr.extend(uppercase_letters)
if (input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip().lower()) == ('д' and 'l'):
    pwr.extend(punctuation)
if (input('Исключить символы il1Lo0O? (д = да, н = нет)').strip().lower()) == ('д' and 'l'):
    for c in 'il1Lo0O':
        pwr.remove(c)

#сам генератор
for _ in range(n):
    print(generate_password(length, pwr))