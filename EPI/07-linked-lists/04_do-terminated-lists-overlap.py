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


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    l0_len, l1_len = length(l0), length(l1)
    if l0_len > l1_len:
        l0, l1 = l1, l0  # Swap so `l0` is always the longer list
    # Advance the longer list to get equal length lists.
    for _ in range(
        l0_len - l1_len  # No need to abs() since we now length of l0 >= lenght of l1
    ):
        l1 = l1.next

    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next
    return l0  # None implies there is no overlap between l0 nad l1.


# TODO: Validate
