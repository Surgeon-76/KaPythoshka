list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
new_list = []

def expand_list(list1, new_list):
    for i in list1:
        if type(i) == list:
            expand_list(i, new_list)
        else:
            new_list.append(i)
    return new_list
expand_list(list1, new_list)
print(sum(new_list) / len(new_list))