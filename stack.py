"""
Classic stack
"""

class Stack:
    """Class"""
    def __init__(self):
        self.arr = []

    def push(self, value):
        """Add"""
        self.arr.append(value)

    def pop(self):
        """Del"""
        if len(self.arr) == 0:
            raise IndexError

        return self.arr.pop()
