num = list(input())
if len(num) == 6:
    print(int(''.join((num[0:1] + num[-1:-6:-1]))))
else:
    print(int(''.join((num[::-1]))))
