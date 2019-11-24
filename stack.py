"""
Stack implementation
"""
class Stack:
    """
    Stack
    methods:
        push
        pop
    """
    def __init__(self):
        self._stack = []

    def push(self, value):
        """

        :param value: value to add in stack
        :return: none
        """
        self._stack.append(value)

    def pop(self):
        """
        :return: deleted element
        """
        if len(self._stack) == 0:
            raise IndexError
        return self._stack.pop()
