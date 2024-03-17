#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        biggest_integer = my_list[0]
        for i in my_list:
            if i > biggest_integer:
                biggest_integer = i
                return biggest_integer
