'''
This module contains a list of all mutators. This list must be kept up to date
If mutator classes are added, removed or renamed.
'''

import mutators.boolean
import mutators.arithmetic

def get():
    '''
    Returns a list containing an instance of each type of mutator
    '''

    ret = []

    ret.append(mutators.boolean.Mutator())
    ret.append(mutators.arithmetic.Mutator())

    return ret