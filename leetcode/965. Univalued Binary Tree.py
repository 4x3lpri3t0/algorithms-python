# https://leetcode.com/problems/univalued-binary-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_unival_tree(self, root: TreeNode) -> bool:
        val = root.val
        q = []
        q.append(root)
        while len(q) > 0:
            # TODO: Use collections.dequeue !!! pop(0) is LINEAR
            cur = q.pop(0)
            if cur.val != val:
                return False
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        return True
