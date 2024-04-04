from data_structures.list_node import ListNode

class Queue:
    def __init__(self) -> None:
        """
        Initializes an empty Queue.
        """
        self.head = None
        self.tail = None
        self.size = 0


    def enqueue(self, data: any) -> None:
        """
        Enqueues data into the queue.

        Args:
            data (any): The data to enqueue into the queue.
        """
        node = ListNode(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def dequeue(self) -> any:
        """
        Dequeues data from the queue.

        Returns:
            any: The data dequeued from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.head:
            data = self.head.val
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return data
        raise IndexError("Queue is empty")

    def peek(self) -> any:
        """
        Peeks at the front of the queue.

        Returns:
            any: The data at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.head:
            return self.head.val
        raise IndexError("Queue is empty")

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not bool(self.size)

    def __str__(self) -> str:
        """
        Returns a string representation of the queue.
        """
        current = self.head
        items = []
        while current:
            items.append(current.val)
            current = current.next
        return str(items)
