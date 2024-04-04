class Queue:
    def __init__(self) -> None:
        """
        Initializes an empty Queue.
        """
        self.data = []

    def enqueue(self, data: any) -> None:
        """
        Enqueues data into the queue.

        Args:
            data (any): The data to enqueue into the queue.
        """
        self.data.append(data)

    def dequeue(self) -> any:
        """
        Dequeues data from the queue.

        Returns:
            any: The data dequeued from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.data:
            return self.data.pop(0)
        raise IndexError("Queue is empty")

    def peek(self) -> any:
        """
        Peeks at the front of the queue.

        Returns:
            any: The data at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.data:
            return self.data[0]
        raise IndexError("Queue is empty")

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not bool(self.data)

    def __str__(self) -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: A string representation of the queue.
        """
        return str(self.data)
