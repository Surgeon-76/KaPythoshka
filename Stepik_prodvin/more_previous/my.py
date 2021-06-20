num = [el for el in [int(i) for i in input().split()]]
print(len([num[j] for j in range(1, len(num)) if num[j] > num[j-1]]))
