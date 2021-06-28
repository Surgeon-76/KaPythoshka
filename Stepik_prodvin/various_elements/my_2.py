num = input().split()
i = 0
while i in range(len(num)):
    for j in range(len(num)):
        if j > (len(num) -1):
            break
        if num.count(num[j]) > 1:
            del num[j]
        #print(j)
    i += 1
        
print(len(num))

