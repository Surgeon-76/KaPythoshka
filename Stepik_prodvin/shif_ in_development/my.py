num = [el for el in [int(i) for i in input().split()]]
for i in range(len(num)):
    num[i], num[-1] = num[-1], num[i]
print(*num)    