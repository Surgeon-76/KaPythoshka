# объявление функции
def is_password_good(password):
    return len(password) >= 8 and password.islower() == False and password.isupper() == False and (password.isalnum() == True and password.isalpha()== False
    and password.isdigit() == False)

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))