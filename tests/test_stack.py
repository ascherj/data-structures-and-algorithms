import unittest
from data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that a Stack object can be instantiated properly.
        """
        stack = Stack()
        self.assertEqual(stack.data, [])
        self.assertIsInstance(stack, Stack)

    def test_push(self):
        """
        Test that an item can be pushed onto the stack.
        """
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.data, [1])

    def test_pop(self):
        """
        Test that an item can be popped off the stack.
        """
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)

    def test_pop_empty(self):
        """
        Test that None is returned when trying to pop from an empty stack.
        """
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_peek(self):
        """
        Test that an item can be peeked at the top of the stack.
        """
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)

    def test_peek_empty(self):
        """
        Test that None is returned when trying to peek at the top of an empty stack.
        """
        stack = Stack()
        self.assertIsNone(stack.peek())

    def test_is_empty(self):
        """
        Test that is_empty returns True when the stack is empty.
        """
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_is_not_empty(self):
        """
        Test that is_empty returns False when the stack is not empty.
        """
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_str(self):
        """
        Test that the string representation of the stack is returned.
        """
        stack = Stack()
        stack.push(1)
        self.assertEqual(str(stack), "[1]")
