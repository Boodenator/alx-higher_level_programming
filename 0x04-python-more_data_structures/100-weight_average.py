#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    denomenator = 0
    if my_list:
        for i in range(len(my_list)):
            numerator += my_list[i][0] * my_list[i][1]
            denomenator += my_list[i][1]
        new_average = numerator / denomenator
        return new_average
    else:
        return 0
