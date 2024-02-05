#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num_printed = 0
        for item in my_list:
            if num_printed < x:
                print(item, end="")
                num_printed += 1
            else:
                break
        print()
        return num_printed
    except IndexError:
        print()
        return num_printed
