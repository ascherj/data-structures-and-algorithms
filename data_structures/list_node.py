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
