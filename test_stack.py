import pytest

import stack


def test_push():
    s = stack.Stack()
    s.push(42)
    assert s.pop() == 42


def test_double_push():
    s = stack.Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1


def test_five_push():
    s = stack.Stack()
    for i in range(5):
        s.push(i)
    for i in range(4):
        s.pop()
    assert s.pop() == 0


def test_empty():
    s = stack.Stack()
    with pytest.raises(IndexError):
        s.pop()
