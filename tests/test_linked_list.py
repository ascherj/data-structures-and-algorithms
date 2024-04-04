import unittest
from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that a LinkedList object can be instantiated properly.
        """
        linked_list = LinkedList()
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertIsInstance(linked_list, LinkedList)

    def test_get(self):
        """
        Test that a value can be retrieved from the linked list.
        """
        linked_list = LinkedList()
        linked_list.insertHead(1)
        self.assertEqual(linked_list.get(0), 1)

    def test_get_out_of_bounds(self):
        """
        Test that an IndexError is raised when trying to retrieve a value from an index that is out of bounds.
        """
        linked_list = LinkedList()
        with self.assertRaises(IndexError):
            linked_list.get(0)

    def test_insert_head(self):
        """
        Test that a value can be inserted at the head of the linked list.
        """
        linked_list = LinkedList()
        linked_list.insertHead(1)
        self.assertEqual(linked_list.head.val, 1)
        self.assertEqual(linked_list.tail.val, 1)

    def test_insert_tail(self):
        """
        Test that a value can be inserted at the tail of the linked list.
        """
        linked_list = LinkedList()
        linked_list.insertTail(1)
        self.assertEqual(linked_list.head.val, 1)
        self.assertEqual(linked_list.tail.val, 1)

    def test_insert_multiple(self):
        """
        Test that multiple values can be inserted into the linked list.
        """
        linked_list = LinkedList()
        linked_list.insertHead(1)
        linked_list.insertTail(2)
        self.assertEqual(linked_list.head.val, 1)
        self.assertEqual(linked_list.tail.val, 2)
        self.assertEqual(linked_list.head.next.val, 2)
        self.assertEqual(linked_list.tail.next, None)

    def test_remove_head(self):
        """
        Test that a value can be removed from the head of the linked list.
        """
        linked_list = LinkedList()
        linked_list.insertHead(1)
        linked_list.remove(0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_remove_tail(self):
        """
        Test that a value can be removed from the tail of the linked list.
        """
        linked_list = LinkedList()
        linked_list.insertTail(1)
        linked_list.remove(0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_remove_middle(self):
        """
        Test that a value can be removed from the middle of the linked list.
        """
        linked_list = LinkedList()
        linked_list.insertHead(1)
        linked_list.insertTail(2)
        linked_list.insertTail(3)
        linked_list.remove(1)
        self.assertEqual(linked_list.head.val, 1)
        self.assertEqual(linked_list.tail.val, 3)
        self.assertEqual(linked_list.head.next.val, 3)
        linked_list.remove(1)
        self.assertEqual(linked_list.tail.val, linked_list.head.val)
        self.assertIsNone(linked_list.head.next)
        self.assertIsNone(linked_list.tail.next)
