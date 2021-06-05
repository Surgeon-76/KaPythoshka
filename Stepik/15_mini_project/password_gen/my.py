from random import*

#функция генератор
def generate_password(length, pwr):
    shuffle(pwr)
    print(pwr)
    password = ''
    for j in range(length):
        password += choice(pwr)
    return password

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
    chars += digits    
if (input('Включить прописные буквы? (д = да, н = нет) ').strip().lower()) == ('д' and 'l'):
    chars += lowercase_letters
if (input('Включить строчные буквы? (д = да, н = нет) ').strip().lower()) == ('д' and 'l'):
    chars += uppercase_letters
if (input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip().lower()) == ('д' and 'l'):
    chars += punctuation
if (input('Исключить символы il1Lo0O? (д = да, н = нет)').strip().lower()) == ('д' and 'l'):
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
pwr.extend(chars)

#сам генератор
for _ in range(n):
    #shuffle(pwr)
    print(generate_password(length, pwr))