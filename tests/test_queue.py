import unittest
from data_structures.queue import Queue

class TestQueue(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that a Queue object can be instantiated properly.
        """
        queue = Queue()
        self.assertEqual(queue.data, [])
        self.assertIsInstance(queue, Queue)

    def test_enqueue(self):
        """
        Test that an item can be enqueued into the queue.
        """
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.data, [1])

    def test_dequeue(self):
        """
        Test that an item can be dequeued from the queue.
        """
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)

    def test_dequeue_empty(self):
        """
        Test that an IndexError is raised when trying to dequeue from an empty queue.
        """
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_peek(self):
        """
        Test that an item can be peeked at the front of the queue.
        """
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.peek(), 1)

    def test_peek_empty(self):
        """
        Test that an IndexError is raised when trying to peek at the front of an empty queue.
        """
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_is_empty(self):
        """
        Test that is_empty returns True when the queue is empty.
        """
        queue = Queue()
        self.assertTrue(queue.is_empty())

    def test_is_not_empty(self):
        """
        Test that is_empty returns False when the queue is not empty.
        """
        queue = Queue()
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_str(self):
        """
        Test that the string representation of the queue is returned.
        """
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(str(queue), "[1]")
