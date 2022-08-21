from typing import Optional


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def find_kth_node_binary_tree(tree: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k: # k-th node **must be in right** subtree of tree.
            k -= left_size + 1
            tree = tree.right
        elif left_size == k - 1: # k-th is iter itself.
            return tree
        else: # k-th node **must be in left** subtree of iter.
            tree = tree.left
    
    return None # Unreachable if k is between 1 and the tree size.

# TODO: Validate + Test