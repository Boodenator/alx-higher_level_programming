#!/usr/bin/python3
''' Module: 1-my_list
'''


class MyList(list):
    ''' Representing a MyList
    '''

    def print_sorted(self):
        '''
        prints the sorted list
        '''
        print(sorted(self))
