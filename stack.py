""" docstring"""

class Stack:
    """stack object"""
    def __init__(self):
        self.items = []

    def push(self, value):
        """add new element in stack"""
        self.items.append(value)

    def pop(self):
        """return last item"""
        return self.items.pop()
