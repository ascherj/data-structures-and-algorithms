class ListNode:
    def __init__(self, val: any) -> None:
        """
        Initializes a ListNode with a value.
        """
        self.val = val
        self.next = None

    def __str__(self) -> str:
        """
        Returns a string representation of the ListNode.
        """
        return str(self.val)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def get(self, index: int) -> any:
        """
        Gets the value at the specified index in the linked list.

        Args:
            index (int): The index of the value to get.

        Returns:
            any: The value at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """

        if index < 0:
            raise IndexError("Index out of bounds")

        current = self.head
        while index > 0 and current:
            current = current.next
            index -= 1
        if not current:
            raise IndexError("Index out of bounds")
        return current.val

    def insertHead(self, val: any) -> None:
        """
        Inserts a value at the head of the linked list.

        Args:
            val (any): The value to insert at the head of the linked list.
        """

        node = ListNode(val)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def insertTail(self, val: any) -> None:
        """
        Inserts a value at the tail of the linked list.

        Args:
            val (any): The value to insert at the tail of the linked list.
        """

        node = ListNode(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node

    def remove(self, index: int) -> bool:
        """
        Removes the value at the specified index in the linked list.

        Args:
            index (int): The index of the value to remove.

        Returns:
            bool: True if the value was removed, False otherwise.
        """

        if index < 0 or not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True

        current = self.head
        while index > 1 and current:
            current = current.next
            index -= 1
        if not current or not current.next:
            return False
        current.next = current.next.next
        if not current.next:
            self.tail = current
        return True

    def getValues(self) -> list[any]:
        """
        Returns a list of all the values in the linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
