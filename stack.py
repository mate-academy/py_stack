"""
stack module
"""


class Stack:
    """
    Classic stack based on one of the base Python containers.
    """

    def __init__(self):
        self.__storage = []

    def push(self, value):
        """
        Added value to stack.
        :param value: Any
        :return: None
        """
        self.__storage.append(value)

    def pop(self):
        """
        Remove value from stack.
        :return: Any
        """
        return self.__storage.pop()

    def is_empty(self):
        """
        Check if stack is empty.
        :return: bool
        """
        return len(self.__storage) == 0
