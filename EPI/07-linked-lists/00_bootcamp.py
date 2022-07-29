# Singly LL
# L => [1] -> [2] -> [...] -> [n]
# Head: first node
# Tail: last node

# Doubly LL
# L => [1] <-> [2] <-> [...] <-> [n]
# (each node has a link to its predecessor)

# Inserting/Deleting elements in LL: TC of O(1)
# Obtaining kth element: O(n)

# Last node is null


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# ================
# = LL boot camp =
# ================

# Two types of LL problems:
# 1) Implement your own list
# 2) Exploit standard list library

# Implementing a basic list API
# - search
# - insert
# - delete

# Search key:
def search_list(L: ListNode, key: int) -> ListNode:
    while L and L.data != key:
        L = L.next
    # If key was not present in the list, L will have become null.
    return L


# Insert new node (after specified node):
def insert_after(node: ListNode, new_node: ListNode) -> None:
    new_node.next = node.next
    node.next = new_node


# Delete next node (assuming current node is not the tail):
def delete_after(node: ListNode) -> None:
    node.next = node.next.next


# Insert and delete: local operations - TC O(1)
# Search: traverses the entire list - TC O(n)
