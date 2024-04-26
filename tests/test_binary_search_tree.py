import unittest
from data_structures.binary_search_tree import BinarySearchTree, TreeMap

class TestBinarySearchTree(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that a BinarySearchTree object can be instantiated properly.
        """
        bst = BinarySearchTree()
        self.assertIsNone(bst.root)
        self.assertIsInstance(bst, BinarySearchTree)

    def test_insert(self):
        """
        Test that a key-value pair can be inserted into the binary search tree.
        """
        bst = BinarySearchTree()
        bst.insert(1)
        self.assertEqual(bst.root.val, 1)

    def test_insert_multiple(self):
        """
        Test that multiple values can be inserted into the binary search tree.
        """
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        self.assertEqual(bst.root.val, 1)
        self.assertEqual(bst.root.right.val, 2)

    def test_search(self):
        """
        Test that a value can be searched for in the binary search tree.
        """
        bst = BinarySearchTree()
        bst.insert(1)
        self.assertEqual(bst.search(1), True)
        self.assertEqual(bst.search(2), False)

    def test_get_min(self):
        """
        Test that the minimum value can be retrieved from the binary search tree.
        """
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        self.assertEqual(bst.getMin(), 1)

    def test_get_max(self):
        """
        Test that the maximum value can be retrieved from the binary search tree.
        """
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        self.assertEqual(bst.getMax(), 3)

    def test_remove(self):
        """
        Test that a value can be removed from the binary search tree.
        """
        bst = BinarySearchTree()
        bst.insert(1)
        bst.remove(1)
        self.assertIsNone(bst.root)

    def test_remove_missing(self):
        """
        Test that nothing happens when trying to remove a value that does not exist in the binary search tree.
        """
        bst = BinarySearchTree()
        bst.insert(1)
        bst.remove(2)
        self.assertEqual(bst.root.val, 1)

    def test_remove_with_children(self):
        """
        Test that a value with children can be removed from the binary search tree.
        """
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.remove(2)
        self.assertEqual(bst.root.val, 3)
        self.assertEqual(bst.root.left.val, 1)

    def test_remove_with_children_and_grandchildren(self):
        """
        Test that a value with children and grandchildren can be removed from the binary search tree.
        """
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        bst.insert(4)
        bst.insert(6)
        bst.insert(8)
        bst.remove(5)
        self.assertEqual(bst.root.val, 6)
        self.assertEqual(bst.root.left.val, 3)
        self.assertEqual(bst.root.left.left.val, 2)
        self.assertEqual(bst.root.left.right.val, 4)
        self.assertEqual(bst.root.right.val, 7)
        self.assertEqual(bst.root.right.right.val, 8)

    def test_inorder_traversal(self):
        """
        Test that the binary search tree can be traversed in order.
        """
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        self.assertEqual(bst.inorderTraversal(), [1, 2, 3])

class TestTreeMap(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that a TreeMap object can be instantiated properly.
        """
        tree_map = TreeMap()
        self.assertIsNone(tree_map.root)
        self.assertIsInstance(tree_map, TreeMap)

    def test_insert(self):
        """
        Test that a key-value pair can be inserted into the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        self.assertEqual(tree_map.root.key, 1)
        self.assertEqual(tree_map.root.val, 1)

    def test_insert_multiple(self):
        """
        Test that multiple key-value pairs can be inserted into the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        tree_map.insert(2, 2)
        self.assertEqual(tree_map.root.key, 1)
        self.assertEqual(tree_map.root.val, 1)
        self.assertEqual(tree_map.root.right.key, 2)
        self.assertEqual(tree_map.root.right.val, 2)

    def test_search(self):
        """
        Test that a key can be searched for in the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        self.assertEqual(tree_map.search(1), True)
        self.assertEqual(tree_map.search(2), False)

    def test_get_val_at_key(self):
        """
        Test that a value can be retrieved from the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        self.assertEqual(tree_map.getValAtKey(1), 1)

    def test_get_missing(self):
        """
        Test that -1 is returned when trying to retrieve a value that does not exist in the tree map.
        """
        tree_map = TreeMap()
        self.assertEqual(tree_map.getValAtKey(1), -1)

    def test_get_min(self):
        """
        Test that the minimum value can be retrieved from the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(2, "two")
        tree_map.insert(1, "one")
        tree_map.insert(3, "three")
        self.assertEqual(tree_map.getMin(), "one")

    def test_get_max(self):
        """
        Test that the maximum value can be retrieved from the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(2, "two")
        tree_map.insert(1, "one")
        tree_map.insert(3, "three")
        self.assertEqual(tree_map.getMax(), "three")

    def test_remove(self):
        """
        Test that a key-value pair can be removed from the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        tree_map.remove(1)
        self.assertIsNone(tree_map.root)

    def test_remove_missing(self):
        """
        Test that nothing happens when trying to remove a key-value pair that does not exist in the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(1, 1)
        tree_map.remove(2)
        self.assertEqual(tree_map.root.key, 1)
        self.assertEqual(tree_map.root.val, 1)

    def test_remove_with_children(self):
        """
        Test that a key-value pair with children can be removed from the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(2, 2)
        tree_map.insert(1, 1)
        tree_map.insert(3, 3)
        tree_map.remove(2)
        self.assertEqual(tree_map.root.key, 3)
        self.assertEqual(tree_map.root.left.key, 1)

    def test_remove_with_children_and_grandchildren(self):
        """
        Test that a key-value pair with children and grandchildren can be removed from the tree map.
        """
        tree_map = TreeMap()
        tree_map.insert(5, 5)
        tree_map.insert(3, 3)
        tree_map.insert(7, 7)
        tree_map.insert(2, 2)
        tree_map.insert(4, 4)
        tree_map.insert(6, 6)
        tree_map.insert(8, 8)
        tree_map.remove(5)
        self.assertEqual(tree_map.root.key, 6)
        self.assertEqual(tree_map.root.left.key, 3)
        self.assertEqual(tree_map.root.left.left.key, 2)
        self.assertEqual(tree_map.root.left.right.key, 4)
        self.assertEqual(tree_map.root.right.key, 7)
        self.assertEqual(tree_map.root.right.right.key, 8)

    def test_get_inorder_keys(self):
        """
        Test that the tree map can be traversed in order.
        """
        tree_map = TreeMap()
        tree_map.insert(2, 2)
        tree_map.insert(1, 1)
        tree_map.insert(3, 3)
        self.assertEqual(tree_map.getInorderKeys(), [1, 2, 3])
