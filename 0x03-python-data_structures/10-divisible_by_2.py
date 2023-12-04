#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    divisible_by_2 = []
    for i in my_list:
        if (i % 2) == 0:
            divisible_by_2.append(True)
        else:
            divisible_by_2.append(False)
    return divisible_by_2
