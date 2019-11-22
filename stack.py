'''Module'''
class Stack:
    '''
    Stack
    '''
    def __init__(self):
        self.items = []

    def push(self, value):
        '''Add value in the list'''
        self.items.append(value)

    def pop(self):
        '''Return last element'''
        return self.items.pop()
