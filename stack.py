"""module"""


class Stack:
    """stack"""
    def __init__(self):
        self.stack = []

    def push(self, value):
        """add value to the end"""
        self.stack.append(value)

    def pop(self):
        """pop last value"""
        if not self.stack:
            raise IndexError
        return self.stack.pop()
