word = [s for s in input()]
count = 0
num = []
for i in range(len(word)):
    if word[i] == 'P' or word[i] == 'Р':
        count += 1
    if word[i] == 'O' or word[i] == 'О':
        num.append(count)
        count = 0    
num.append(count)
print(max(num))