def uniq_add(my_list=[]):
    unique_nums = set(my_list)
    total = 0
    for num in unique_nums:
        total += num
    return total