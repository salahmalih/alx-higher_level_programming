#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    new_list = []
    for i in my_list:
            if i not in  new_list:
                sum = sum + int(i)
                new_list.append(i)
    return sum
