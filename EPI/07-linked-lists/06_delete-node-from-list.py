from typing import Optional


class ListNode(object):
    def __init__(self, x=None, next=None):
        self.data = x
        self.next = next


def print_list(L: Optional[ListNode]) -> None:
    while L:
        print(L.data, end=" ")
        L = L.next
    print()


# Assumes node_to_delete is not tail.
def deletion_from_list(node_to_delete: ListNode) -> None:
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next


# TODO: Validate
