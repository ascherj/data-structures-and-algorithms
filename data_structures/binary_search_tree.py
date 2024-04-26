from data_structures.tree_node import TreeNode, TreeMapNode

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def create_node(self, key: int, val: any=None) -> TreeNode:
        return TreeNode(key)

    def get_comparison_key(self, node: TreeNode) -> int:
        return node.val

    def insert(self, key: int, val: any=None) -> None:
        if not self.root:
            self.root = self.create_node(key, val)
            return

        node = self.root
        while True:
            node_key = self.get_comparison_key(node)
            direction = 1 if key > node_key else -1
            if direction < 0:
                if not node.left:
                    node.left = self.create_node(key, val)
                    break
                else:
                    node = node.left
            elif direction > 0:
                if not node.right:
                    node.right = self.create_node(key, val)
                    break
                else:
                    node = node.right
            else:
                break

    def search(self, key: int) -> bool:
        node = self.root
        node_key = self.get_comparison_key(node)
        while node:
            if node_key == key:
                return True
            if key < node_key:
                node = node.left
            else:
                node = node.right
        return False


    def getMin(self) -> int:
        node = self.root
        while node and node.left:
            node = node.left
        return node.val if node else -1

    def getMax(self) -> int:
        node = self.root
        while node and node.right:
            node = node.right
        return node.val if node else -1

    def remove(self, key: int) -> None:

        def getMinNode(root: TreeNode) -> TreeNode:
            if not root or not root.left:
                return root
            return getMinNode(root.left)

        def removeHelper(root: TreeNode, key: int) -> TreeNode:
            if not root:
                return None

            node_key = self.get_comparison_key(root)

            if key == node_key:
                if not root.left and not root.right:
                    return None
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                else:
                    min_val_node = getMinNode(root.right)
                    self._overwrite_node(root, min_val_node)
                    root.right = removeHelper(root.right, root.val)

            if node_key < root.val:
                root.left = removeHelper(root.left, node_key)

            if node_key > root.val:
                root.right = removeHelper(root.right, node_key)

            return root

        self.root = removeHelper(self.root, key)

    def _overwrite_node(self, node_to_overwrite: TreeNode, new_node: TreeNode) -> None:
        node_to_overwrite.val = new_node.val

    def inorderTraversal(self) -> list[int]:

        def inorderTraversalHelper(node: TreeNode) -> list[int]:
            if not node:
                return []
            node_key = self.get_comparison_key(node)
            return inorderTraversalHelper(node.left) + [node_key] + inorderTraversalHelper(node.right)

        return inorderTraversalHelper(self.root)

class TreeMap(BinarySearchTree):

    def __init__(self):
        self.root = None

    def create_node(self, key: int, val: any) -> TreeMapNode:
        return TreeMapNode(key, val)

    def get_comparison_key(self, node: TreeMapNode) -> int:
        return node.key

    def insert(self, key: int, val: any) -> None:
        super().insert(key, val)

    def search(self, key: int) -> bool:
        return super().search(key)

    def getMin(self) -> any:
        return super().getMin()


    def getMax(self) -> any:
        return super().getMax()

    def remove(self, key: int) -> None:
        super().remove(key)

    def _overwrite_node(self, node_to_overwrite: TreeMapNode, new_node: TreeMapNode) -> None:
        node_to_overwrite.key = new_node.key
        node_to_overwrite.val = new_node.val

    def getInorderKeys(self) -> list[int]:
        return super().inorderTraversal()

    def getValAtKey(self, key: int) -> any:
        node = self.root
        while node:
            if node.key == key:
                return node.val
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return -1
