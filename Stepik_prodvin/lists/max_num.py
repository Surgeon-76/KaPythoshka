list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
def expand_list(list1, maximum):
    for i in list1:
        if type(i) == list:
            for j in i:
                if j > maximum:
                    maximum = j
            
    return maximum
maximum = expand_list(list1, maximum)
print(maximum)