'''
Base class for mutators
'''

class Mutator(object):
    '''
    TBD
    '''

    def __init__(self):
        pass

    def strip_escapes(self, line):
        line = line.replace('\\', '')