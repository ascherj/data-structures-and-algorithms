import unittest
from data_structures.binary_search_tree import TreeMap

class TestBinarySearchTree(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that a BinarySearchTree object can be instantiated properly.
        """
        tree_map = TreeMap()
        self.assertIsNone(tree_map.root)
        self.assertIsInstance(tree_map, TreeMap)

    def test_insert(self):
        """
        Test that a key-value pair can be inserted into the binary search tree.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        self.assertEqual(tree_map.root.key, 1)
        self.assertEqual(tree_map.root.val, 1)

    def test_insert_multiple(self):
        """
        Test that multiple key-value pairs can be inserted into the binary search tree.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        tree_map.insert(2, 2)
        self.assertEqual(tree_map.root.key, 1)
        self.assertEqual(tree_map.root.val, 1)
        self.assertEqual(tree_map.root.right.key, 2)
        self.assertEqual(tree_map.root.right.val, 2)

    def test_get(self):
        """
        Test that a value can be retrieved from the binary search tree.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        self.assertEqual(tree_map.get(1), 1)

    def test_get_missing(self):
        """
        Test that -1 is returned when trying to retrieve a value that does not exist in the binary search tree.
        """
        tree_map = TreeMap()
        self.assertEqual(tree_map.get(1), -1)

    def test_get_min(self):
        """
        Test that the minimum value can be retrieved from the binary search tree.
        """
        tree_map = TreeMap()
        tree_map.insert(2, 2)
        tree_map.insert(1, 1)
        tree_map.insert(3, 3)
        self.assertEqual(tree_map.getMin(), 1)

    def test_get_max(self):
        """
        Test that the maximum value can be retrieved from the binary search tree.
        """
        tree_map = TreeMap()
        tree_map.insert(2, 2)
        tree_map.insert(1, 1)
        tree_map.insert(3, 3)
        self.assertEqual(tree_map.getMax(), 3)

    def test_remove(self):
        """
        Test that a key-value pair can be removed from the binary search tree.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        tree_map.remove(1)
        self.assertIsNone(tree_map.root)

    def test_remove_missing(self):
        """
        Test that nothing happens when trying to remove a key-value pair that does not exist in the binary search tree.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        tree_map.remove(2)
        self.assertEqual(tree_map.root.key, 1)
        self.assertEqual(tree_map.root.val, 1)

    def test_get_inorder_keys(self):
        """
        Test that the binary search tree can be traversed in order.
        """
        tree_map = TreeMap()
        tree_map.insert(2, 2)
        tree_map.insert(1, 1)
        tree_map.insert(3, 3)
        self.assertEqual(tree_map.getInorderKeys(), [1, 2, 3])
