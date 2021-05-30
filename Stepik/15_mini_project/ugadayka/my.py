from random import*
def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


num_rnd = randint(1, 100)
print('Добро пожаловать в числовую угадайку!')
while True:
    