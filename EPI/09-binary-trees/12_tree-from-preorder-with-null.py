from typing import List


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    def reconstruct_preorder_helper(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None
        
        # Note that reconstruct_preorder_helper updates preorder_iter.
        # So the order of following two calls are critical.
        left_subtree = reconstruct_preorder_helper(preorder_iter)
        right_subtree = reconstruct_preorder_helper(preorder_iter)
        
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)

    return reconstruct_preorder_helper(iter(preorder))

# TODO: Validate + Test