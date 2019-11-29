"""Stack module."""


class Stack:
    """Stack class."""

    def __init__(self):
        """Initialize an empty list."""
        self.stack = []

    def push(self, value):
        """Append a value to stack"""
        self.stack.append(value)

    def pop(self):
        """:returns the last added value of stack"""
        return self.stack.pop()
