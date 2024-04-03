import unittest
from data_structures.array import Array, StaticArray, DynamicArray

class TestArray(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that an Array object cannot be instantiated.
        """
        with self.assertRaises(TypeError):
            Array()

class TestStaticArray(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that a StaticArray object can be instantiated properly.
        """
        array = StaticArray(3)
        self.assertEqual(array.capacity, 3)
        self.assertEqual(array.count, 0)
        self.assertEqual(array.items, [None, None, None])
        self.assertEqual(str(array), "[None, None, None]")
        self.assertIsInstance(array, Array)

    def test_insert(self):
        """
        Test that an item can be inserted into the array.
        """
        array = StaticArray(3)
        array.insert(1)
        self.assertEqual(array.count, 1)
        self.assertEqual(array.get(0), 1)

    def test_insert_full(self):
        """
        Test that an IndexError is raised when trying to insert an item into a full array.
        """
        array = StaticArray(3)
        array.insert(1)
        array.insert(2)
        array.insert(3)
        with self.assertRaises(IndexError):
            array.insert(4)

    def test_get(self):
        """
        Test that an item can be retrieved from the array.
        """
        array = StaticArray(3)
        array.insert(1)
        self.assertEqual(array.get(0), 1)

    def test_get_out_of_bounds(self):
        """
        Test that an IndexError is raised when trying to retrieve an item from an index that is out of bounds.
        """
        array = StaticArray(3)
        with self.assertRaises(IndexError):
            array.get(0)

    def test_delete(self):
        """
        Test that an item can be deleted from the array.
        """
        array = StaticArray(3)
        array.insert(1)
        array.insert(2)
        array.insert(3)
        self.assertEqual(array.delete(1), 2)
        self.assertEqual(array.count, 2)
        self.assertEqual(array.get(0), 1)
        self.assertEqual(array.get(1), 3)

    def test_delete_empty(self):
        """
        Test that an IndexError is raised when trying to delete an item from an empty array.
        """
        array = StaticArray(3)
        with self.assertRaises(IndexError):
            array.delete(0)

    def test_search(self):
        """
        Test that an item can be searched for in the array.
        """
        array = StaticArray(3)
        array.insert(1)
        array.insert(2)
        array.insert(3)
        self.assertEqual(array.search(2), 1)
        self.assertEqual(array.search(4), -1)

    def test_string_representation(self):
        """
        Test that the string representation of the array is returned.
        """
        array = StaticArray(3)
        array.insert(1)
        array.insert(2)
        self.assertEqual(str(array), "[1, 2, None]")

class TestDynamicArray(unittest.TestCase):
    def test_instantiation(self):
        """
        Test that a DynamicArray object can be instantiated properly.
        """
        array = DynamicArray(3)
        self.assertEqual(array.capacity, 3)
        self.assertEqual(array.count, 0)
        self.assertEqual(array.items, [None, None, None])
        self.assertEqual(str(array), "[]")
        self.assertIsInstance(array, Array)

    def test_insert(self):
        """
        Test that an item can be inserted into the array.
        """
        array = DynamicArray(3)
        array.insert(1)
        self.assertEqual(array.count, 1)
        self.assertEqual(array.get(0), 1)

    def test_insert_resize(self):
        """
        Test that the array is resized when it is full.
        """
        array = DynamicArray(3)
        array.insert(1)
        array.insert(2)
        array.insert(3)
        array.insert(4)
        self.assertEqual(array.capacity, 6)
        self.assertEqual(array.count, 4)
        self.assertEqual(array.get(0), 1)
        self.assertEqual(array.get(1), 2)
        self.assertEqual(array.get(2), 3)
        self.assertEqual(array.get(3), 4)

    def test_get(self):
        """
        Test that an item can be retrieved from the array.
        """
        array = DynamicArray(3)
        array.insert(1)
        self.assertEqual(array.get(0), 1)

    def test_get_out_of_bounds(self):
        """
        Test that an IndexError is raised when trying to retrieve an item from an index that is out of bounds.
        """
        array = DynamicArray(3)
        with self.assertRaises(IndexError):
            array.get(0)

    def test_delete(self):
        """
        Test that an item can be deleted from the array.
        """
        array = DynamicArray(3)
        array.insert(1)
        array.insert(2)
        array.insert(3)
        self.assertEqual(array.delete(1), 2)
        self.assertEqual(array.count, 2)
        self.assertEqual(array.get(0), 1)
        self.assertEqual(array.get(1), 3)

    def test_delete_empty(self):
        """
        Test that an IndexError is raised when trying to delete an item from an empty array.
        """
        array = DynamicArray(3)
        with self.assertRaises(IndexError):
            array.delete(0)

    def test_delete_resize(self):
        """
        Test that the array is resized when it is less than half full.
        """
        array = DynamicArray(3)
        array.insert(1)
        array.insert(2)
        array.insert(3)
        array.insert(4)
        array.delete(1)
        array.delete(1)
        self.assertEqual(array.capacity, 3)
        self.assertEqual(array.count, 2)
        self.assertEqual(array.get(0), 1)
