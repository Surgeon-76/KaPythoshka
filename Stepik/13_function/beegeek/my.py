# объявление функции
def is_valid_password(password):
    pword = [i for i in password.split(':')]
    return pword[0] == pword[0][::-1] and len([n for n in range(1, int(pword[1])+1) 
    if int(pword[1]) % n == 0]) == 2 and int(pword[2]) % 2 == 0 and len(pword) == 3

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))

