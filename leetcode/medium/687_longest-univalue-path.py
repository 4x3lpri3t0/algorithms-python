# https://leetcode.com/problems/longest-univalue-path/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longest_univalue_path(self, root: TreeNode) -> int:
        return self.get_max_path_length(-1, 0, root)

    # TODO: Fix!
    def get_max_path_length(self, previousVal, currentLength, root: TreeNode) -> int:
        # if root.val == previousVal:
        #     currentLength += 1
        # else:
        #     currentLength = 0

        # leftMax = currentLength
        # rightMax = currentLength
        # if root.left is not None:
        #     leftMax = max(leftMax, self.getMaxPathLength(
        #         root.val, currentLength, root.left))
        # if root.right is not None:
        #     rightMax = max(rightMax, self.getMaxPathLength(
        #         root.val, currentLength, root.right))
        # if root.val == root.left.val and root.left.val == root.right.val:
        #     return leftMax + rightMax + 1
        # return max(leftMax, rightMax)
        return
