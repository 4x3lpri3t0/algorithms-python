# https://leetcode.com/problems/univalued-binary-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        q = []
        q.append(root)
        while len(q) > 0:
            cur = q.pop(0)
            if cur.val != val:
                return False
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        return True
