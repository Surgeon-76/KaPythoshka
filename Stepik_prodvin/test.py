my_list = [1, 2, 2, [23, 4, [3, 2]]]
new_list = []

def expand_list(my_list, new_list):
    for i in my_list:
        if type(i) == list:
            expand_list(i, new_list)
        else:
            new_list.append(i)
    return new_list

print(expand_list(my_list, new_list))