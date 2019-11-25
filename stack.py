"""Implement a classic stack"""


class Stack:
    """Implementation of a classic stack based on one of the base Python containers"""
    def __init__(self):
        self.array = []

    def push(self, value):
        """Python push realization"""
        self.array.append(value)

    def pop(self):
        """Python pop realization"""
        if self.array:
            return self.array.pop()
        raise IndexError
