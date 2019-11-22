"""
docstring
"""


class Stack:
    """
    class doc
    """

    def __init__(self):
        """
        self
        """
        self.stack = []

    def push(self, value):
        """

        :param value:
        :return:
        """
        self.stack.append(value)

    def pop(self):
        """

        :return:
        """
        if not self.stack:
            raise IndexError
        return self.stack.pop()
