from typing import Optional


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node.right:
        # Successor is the leftmost element in node's right subtree.
        node = node.right
        while node.left:
            node = node.left
        return node
    
    # Find the closest ancestor whose left subtree contains node.
    while node.parent and node.parent.right is node: # Up until node is left child (or root).
        node = node.parent
    
    # A return value of None means node does not have successor,
    # i.e., node is the rightmost node in the tree.
    return node.parent

# TODO: Validate + Test