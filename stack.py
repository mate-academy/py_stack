"""stack module"""


class Stack:
    """stack class"""
    def __init__(self):
        self.array = []

    def push(self, value):
        """push to stack"""
        self.array.append(value)

    def pop(self):
        """pop from stack"""
        if not self.array:
            raise IndexError
        result = self.array.pop()
        return result
