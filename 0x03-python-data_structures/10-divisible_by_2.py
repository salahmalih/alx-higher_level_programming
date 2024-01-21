#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_boll = my_list.copy()
    for i in range(len(list_boll)):
        if list_boll[i] % 2 == 0:
            list_boll[i] = True
        else:
            list_boll[i] = False
    return list_boll
