from typing import List


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
def binary_tree_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> BinaryTreeNode:
    
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
    
    # Builds the subtree with preorder[preorder_start:preorder_end] and inorder[inorder_start:inorder_end].
    def binary_tree_from_preorder_inorder_helper(
        preorder_start,
        preorder_end,
        inorder_start,
        inorder_end):
        
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            # Recursively builds the left subtree.
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1,
                preorder_start + 1 + left_subtree_size,
                inorder_start, root_inorder_idx),
            # Recursively builds the right subtree.
            binary_tree_from_preorder_inorder(
                preorder_start + 1 + left_subtree_size,
                preorder_end,
                root_inorder_idx + 1,
                inorder_end))
    
    return binary_tree_from_preorder_inorder_helper(preorder_start=0,
                                                    preorder_end=len(preorder),
                                                    inorder_start=0,
                                                    inorder_end=len(inorder))

# TODO: Validate + Test