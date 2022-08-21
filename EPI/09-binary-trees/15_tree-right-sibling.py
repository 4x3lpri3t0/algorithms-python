class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def construct_right_sibling(tree: BinaryTreeNode) -> None:
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            # Populate left child's next field.
            start_node.left.next = start_node.right
            # Populate right child's next field if start_node is not the last node of level.
            start_node.right.next = start_node.next and start_node.next.left
            start_node = start_node.next
            
        while tree and tree.left:
            populate_children_next_field(tree)
            tree = tree.left

# TODO: Validate + Test