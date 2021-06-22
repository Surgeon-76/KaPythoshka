icebox, num = [], []
s = 'anton'
for i in range(int(input())):
    icebox.extend(input())
    n = 0
    for j in range(len(s)):
        if s[j] in icebox:
            n += 1
            ind = icebox.index(s[j])
            if ind != 0:
                del icebox[:ind]
            elif ind == 0:
                del icebox[ind]
    if n == 5:
        num.append(i+1)
    icebox.clear()
print(*num)