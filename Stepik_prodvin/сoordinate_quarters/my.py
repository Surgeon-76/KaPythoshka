coord, num = [], [0, 0, 0, 0]
for i in range(int(input())):
    coord = [int(i) for i in input().split()]
    if coord[0] > 0 and coord[1] > 0:num[0] += 1
    elif coord[0] < 0 and coord[1] > 0:num[1] += 1
    elif coord[0] < 0 and coord[1] < 0:num[2] += 1
    elif coord[0] > 0 and coord[1] < 0:num[3] += 1
print('Первая четверть:', num[0])    
print('Вторая четверть:', num[1])  
print('Третья четверть:', num[2])  
print('Четвертая четверть:', num[3])