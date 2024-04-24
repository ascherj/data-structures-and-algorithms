class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeMapNode(TreeNode):
    def __init__(self, key, val, left=None, right=None):
        super().__init__(val, left, right)
        self.key = key
