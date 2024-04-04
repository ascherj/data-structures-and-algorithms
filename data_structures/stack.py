class Stack:
    def __init__(self) -> None:
        """
        Initializes an empty Stack.
        """
        self.data = []

    def push(self, data: any) -> None:
        """
        Pushes data onto the stack.

        Args:
            data (any): The data to push onto the stack.
        """
        self.data.append(data)

    def pop(self) -> any:
        """
        Pops data off the stack.

        Returns:
            any: The data popped off the stack.
        """
        if self.data:
            return self.data.pop()
        return None

    def peek(self) -> any:
        """
        Peeks at the top of the stack.

        Returns:
            any: The data at the top of the stack.
        """
        if self.data:
            return self.data[-1]
        return None

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not bool(self.data)

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        return str(self.data)
