#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list) or idx < 0:
        return
    copy_list = my_list[:]
    copy_list[idx] = element
    return copy_list
