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


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return dummy_head.next


# TODO: Validate
