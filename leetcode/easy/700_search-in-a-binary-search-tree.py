# https://leetcode.com/problems/search-in-a-binary-search-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def search_BST(self, root: TreeNode, val: int) -> TreeNode:
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root
