num = input().split()
num2 = []
for i in range(len(num)):
    print(num[i])
    if num2.count(num[i]) == 0:
        num2.append(num[i])  
print(len(num2))
