class Solution:
    def invertTree(self, root):

        if root is None:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root