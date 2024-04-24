from data_structures.tree_node import TreeMapNode

class TreeMap:

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: any) -> None:
        """
        Inserts a key-value pair into the binary search tree.

        Args:
            key (int): The key to insert into the binary search tree.
            val (any): The value to insert into the binary search tree.
        """
        if not self.root:
            self.root = TreeMapNode(key, val)
            return

        node = self.root
        while True:
            if key < node.key:
                if not node.left:
                    node.left = TreeMapNode(key, val)
                    break
                else:
                    node = node.left
            elif key > node.key:
                if not node.right:
                    node.right = TreeMapNode(key, val)
                    break
                else:
                    node = node.right
            else:
                node.val = val
                break


    def get(self, key: int) -> any:
        """
        Gets the value associated with the specified key in the binary search tree.

        Args:
            key (int): The key to search for in the binary search tree.

        Returns:
            any: The value associated with the specified key if found, otherwise -1.
        """
        node = self.root
        while node:
            if node.key == key:
                return node.val
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return -1


    def getMin(self) -> any:
        """
        Gets the value at the minimum key in the binary search tree.

        Returns:
            any: The value at the minimum key in the binary search tree.
        """
        node = self.root
        while node and node.left:
            node = node.left
        return node.val if node else -1


    def getMax(self) -> any:
        """
        Gets the value at the maximum key in the binary search tree.

        Returns:
            any: The value at the maximum key in the binary search tree.
        """
        node = self.root
        while node and node.right:
            node = node.right
        return node.val if node else -1

    def remove(self, key: int) -> None:
        """
        Removes the key-value pair associated with the specified key from the binary search tree.

        Args:
            key (int): The key to remove from the binary search tree.
        """

        def getMinNode(root: TreeMapNode | None) -> TreeMapNode | None:
            """
            Gets the minimum node in the binary search tree.

            Args:
                root (TreeMapNode): The root of the binary search tree.

            Returns:
                TreeMapNode: The minimum node in the binary search tree.
            """
            if not root or not root.left:
                return root
            return getMinNode(root.left)

        def removeHelper(root: TreeMapNode | None, key: int) -> TreeMapNode | None:
            """
            Helper function to remove a key-value pair from the binary search tree.

            Args:
                root (TreeMapNode): The root of the binary search tree.
                key (int): The key to remove from the binary search tree.

            Returns:
                TreeMapNode: The root of the binary search tree after removing the key-value pair.
            """
            if not root:
                return None

            if key == root.key:
                if not root.left and not root.right:
                    return None
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                else:
                    min_val_node = getMinNode(root.right)
                    root.key = min_val_node.key
                    root.val = min_val_node.val
                    root.right = removeHelper(root.right, root.key)

            if key < root.key:
                root.left = removeHelper(root.left, key)

            if key > root.key:
                root.right = removeHelper(root.right, key)

            return root

        self.root = removeHelper(self.root, key)

    def getInorderKeys(self) -> list[int]:
        """
        Gets the keys of the binary search tree in inorder traversal.

        Returns:
            list[int]: The keys of the binary search tree in inorder traversal.
        """

        def inorderTraversal(node: TreeMapNode | None) -> list[int]:
            """
            Traverses the binary search tree in inorder traversal.

            Args:
                node (TreeMapNode): The node to start the traversal from.

            Returns:
                list[int]: The keys of the binary search tree in inorder traversal.
            """
            if not node:
                return []
            return inorderTraversal(node.left) + [node.key] + inorderTraversal(node.right)

        return inorderTraversal(self.root)
