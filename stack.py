"""Classic Stack based on one of the base Python containers."""


class Stack:
    """Stack class"""
    def __init__(self):
        self.arr = []

    def push(self, value):
        """Add item to the container"""
        self.arr.append(value)

    def pop(self):
        """Remove last item in the container"""
        if not self.arr:
            raise IndexError
        return self.arr.pop()
