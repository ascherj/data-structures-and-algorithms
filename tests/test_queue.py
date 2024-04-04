import unittest
from data_structures.queue import Queue

class TestQueue(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that a Queue object can be instantiated properly.
        """
        queue = Queue()
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
        self.assertEqual(queue.size, 0)
        self.assertIsInstance(queue, Queue)

    def test_enqueue(self):
        """
        Test that an item can be enqueued into the queue.
        """
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.size, 1)
        self.assertEqual(queue.head.val, 1)
        self.assertEqual(queue.tail.val, 1)

    def test_dequeue(self):
        """
        Test that an item can be dequeued from the queue.
        """
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)
        self.assertEqual(queue.size, 0)

    def test_dequeue_multiple(self):
        """
        Test that an item can be dequeued from a queue with multiple items.
        """
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.head.val, 2)
        self.assertEqual(queue.tail.val, 2)
        self.assertEqual(queue.size, 1)

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
        self.assertEqual(queue.size, 1)

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
        Test that the string representation of the queue is correct.
        """
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(str(queue), "[1, 2]")
