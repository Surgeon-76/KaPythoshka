from math import*

# put your python code here
def steps(num):
    return ceil(log2(num))

n = int(input())
print(steps(n))