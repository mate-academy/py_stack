"""stack module"""
class Stack:
    """
    Defines "stack" data structure,
    contains methods:
    push
    pop
    """
    def __init__(self):
        self.stack = []


    def push(self, value):
        """Adds an element on top of the stack"""
        self.stack.append(value)

    def pop(self):
        """Remove and return top element of a stack"""
        if len(self.stack) == 0:
            raise IndexError
        return self.stack.pop()
