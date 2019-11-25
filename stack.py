"""module docstring"""
class Stack:
    """class docstring"""
    def __init__(self):
        """docstring"""
        self.array = []

    def push(self, value):
        """docstring"""
        self.array.append(value)

    def pop(self):
        """docstring"""
        if not self.array:
            raise IndexError
        return self.array.pop()
