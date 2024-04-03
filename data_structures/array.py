from abc import ABC, abstractmethod

class Array(ABC):
    def __init__(self, capacity: int) -> None:
        """
        Initializes an empty Array with a specified capacity.

        Args:
            capacity (int): The initial capacity of the array.
        """
        self.capacity = capacity
        self.count = 0
        self.items = [None] * capacity

    def get(self, index: int) -> any:
        """
        Gets the item at the specified index.

        Args:
            index (int): The index of the item to get.

        Returns:
            any: The item at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")
        return self.items[index]

    def delete(self, index: int) -> any:
        """
        Deletes the item at the specified index.

        Args:
            index (int): The index of the item to delete.

        Returns:
            any: The deleted item at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self.count:
            raise IndexError("Index is out of bounds")
        item_to_delete = self.items[index]

        for i in range(index, self.count - 1):
            self.items[i] = self.items[i + 1]
        self.count -= 1
        return item_to_delete

    def search(self, item: any) -> int:
        """
        Searches for an item in the array.

        Args:
            item (any): The item to search for.

        Returns:
            int: The index of the item if found, otherwise -1.
        """
        for i in range(self.count):
            if self.items[i] == item:
                return i
        return -1

    @abstractmethod
    def insert(self, item: any) -> None:
        """
        Inserts an item at the end of the array.

        Args:
            item (any): The item to be inserted.
        """
        pass

    def __str__(self) -> str:
        """
        Returns a string representation of the array.

        Returns:
            str: A string representation of the array.
        """
        return str(self.items[:self.count])

class StaticArray(Array):
    def insert(self, item: any) -> None:
        """
        Inserts an item at the end of the array.

        Args:
            item (any): The item to be inserted.

        Raises:
            IndexError: If the array is full.
        """
        if self.count == self.capacity:
            raise IndexError("Array is full")
        self.items[self.count] = item
        self.count += 1

    def __str__(self) -> str:
        """
        Returns a string representation of the array.

        Returns:
            str: A string representation of the array.
        """
        return str(self.items)

class DynamicArray(Array):
    def insert(self, item: any) -> None:
        """
        Inserts an item at the end of the array. Resizes the array if it is full.

        Args:
            item (any): The item to be inserted.
        """
        # Resize the array if it is full
        if self.count == self.capacity:
            self._resize(self.capacity * 2)

        self.items[self.count] = item
        self.count += 1

    def delete(self, index: int) -> any:
        """
        Deletes the item at the specified index. Resizes the array if the count is less than half the capacity.

        Args:
            index (int): The index of the item to delete.

        Returns:
            any: The deleted item at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        item_to_delete = super().delete(index)

        # Resize the array if the count is less than half the capacity
        if self.count < self.capacity // 2:
            self._resize(self.capacity // 2)

        return item_to_delete

    def _resize(self, new_capacity: int) -> None:
        """
        Resizes the array to a new capacity.

        Args:
            new_capacity (int): The new capacity of the array.
        """
        new_items = [None] * new_capacity
        for i in range(self.count):
            new_items[i] = self.items[i]
        self.capacity = new_capacity
        self.items = new_items
