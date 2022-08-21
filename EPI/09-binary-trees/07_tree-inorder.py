from typing import List

'''
Non-recursive function for inorder traversal.

* Use a stack to store nodes being processed.
'''

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []
    
    in_process = [(tree, False)]
    while in_process:
        node, left_subtree_traversed = in_process.pop()
        if node:
            if left_subtree_traversed:
                result.append(node.data)
            else:
                in_process.append((node.right, False))
                in_process.append((node, True))
                in_process.append((node.left, False))
    
    return result

# TODO: Validate + Test