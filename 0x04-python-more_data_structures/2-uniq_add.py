#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for digit in my_list:
        if digit not in new_list:
            sum += digit
            new_list.append(digit)

    return sum
