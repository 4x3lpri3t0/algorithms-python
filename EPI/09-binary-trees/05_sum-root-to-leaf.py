class BinaryNodeTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        

def sum_root_to_leaf(tree: BinaryNodeTree) -> int:
    def sum_root_to_leaf_helper(tree, partial_path_sum=0):
        if not tree:
            return 0
        
        partial_path_sum = partial_path_sum * 2 + tree.data # (* 2 because the paths share nodes -> not necessary to repeat computations)
        if not tree.left and not tree.right: # Leaf
            return partial_path_sum
        # Non-leaf
        return (sum_root_to_leaf_helper(tree.left, partial_path_sum) +
                sum_root_to_leaf_helper(tree.right, partial_path_sum))
    
    return sum_root_to_leaf_helper(tree)

# TODO: Validate + Test
