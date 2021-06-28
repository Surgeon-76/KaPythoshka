num = [int(input()) for i in range(int(input()))]
flag = False
set_num = int(input())
for i in range(len(num)):
    for j in range(len(num)):
        if i == j:continue
        if (num[i] * num[j]) == set_num:
            flag = True        
print ('%s' %('ДА' if flag else 'НЕТ'))