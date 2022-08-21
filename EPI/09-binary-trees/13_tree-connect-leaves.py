from typing import List


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def create_list_of_leaves(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if not tree:
        return []
    
    if not tree.left and not tree.right:
        return [tree]
    
    # First do the left subtree, and then do the right subtree.
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)

# TODO: Validate + Test