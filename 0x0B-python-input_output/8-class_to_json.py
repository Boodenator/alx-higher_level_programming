#!/usr/bin/python3
'''function definition returns the dictionary description with simple data structure
'''


def class_to_json(obj):
    '''module class_to_json
       returns builds a dictionary
    '''
    return obj.__dict__
