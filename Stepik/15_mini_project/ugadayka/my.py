from random import*
def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


number = randint(1, 100)
print('Добро пожаловать в числовую угадайку!')

while True:
    response = input('Введите число от 1 до 100:')
    if not is_valid(response):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    val = int(response)
    
    if val < number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif val > number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')